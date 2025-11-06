#include "hardware/adc.h"
#include "hardware/dma.h"

// ===== CONFIG =====
const uint CAPTURE_CHANNEL = 0;       // ADC channel 0 = A0
const uint SAMPLES_PER_BUFFER = 256;  // samples per DMA buffer
const float ADC_CLOCK_DIV = 0;        // 0 = max speed (~500 kS/s typical)
const uint MOVING_AVG_WINDOW = 8;     // window size for moving average

// ===== BUFFERS =====
uint16_t bufferA[SAMPLES_PER_BUFFER];
uint16_t bufferB[SAMPLES_PER_BUFFER];
uint16_t filtered_buf[SAMPLES_PER_BUFFER];

int dma_chan;
dma_channel_config dma_config;

// ===== FLAGS =====
volatile bool bufferA_full = false;
volatile bool bufferB_full = false;

// ===== DMA IRQ Handler =====
void dma_handler() {
  if (dma_hw->ints0 & (1u << dma_chan)) {
    dma_hw->ints0 = 1u << dma_chan; // clear interrupt

    static bool toggle = false;
    toggle = !toggle;

    if (toggle) {
      bufferA_full = true;
      dma_channel_set_write_addr(dma_chan, bufferB, true);  // switch to B
    } else {
      bufferB_full = true;
      dma_channel_set_write_addr(dma_chan, bufferA, true);  // switch to A
    }
  }
}

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // ===== ADC Setup =====
  adc_init();
  adc_gpio_init(26 + CAPTURE_CHANNEL);
  adc_select_input(CAPTURE_CHANNEL);

  adc_fifo_setup(
    true,  // Write each sample to FIFO
    true,  // Enable DMA request
    1,     // DREQ when at least 1 sample ready
    false, // No error bit
    false  // No byte shift
  );

  adc_set_clkdiv(ADC_CLOCK_DIV);  // fastest sampling
  adc_run(false);

  // ===== DMA Setup =====
  dma_chan = dma_claim_unused_channel(true);
  dma_config = dma_channel_get_default_config(dma_chan);
  channel_config_set_transfer_data_size(&dma_config, DMA_SIZE_16);
  channel_config_set_read_increment(&dma_config, false);
  channel_config_set_write_increment(&dma_config, true);
  channel_config_set_dreq(&dma_config, DREQ_ADC);

  dma_channel_configure(
    dma_chan,
    &dma_config,
    bufferA,
    &adc_hw->fifo,
    SAMPLES_PER_BUFFER,
    false
  );

  // ===== IRQ =====
  dma_channel_set_irq0_enabled(dma_chan, true);
  irq_set_exclusive_handler(DMA_IRQ_0, dma_handler);
  irq_set_enabled(DMA_IRQ_0, true);

  // ===== Start =====
  adc_run(true);
  dma_channel_start(dma_chan);

  Serial.println("Continuous ADC capture with moving average started...");
}

// ===== Simple Moving Average Function =====
void applyMovingAverage(uint16_t* src, uint16_t* dest, int length, int window) {
  uint32_t sum = 0;
  int half = window / 2;

  // Pre-fill sum for the first few samples
  for (int i = 0; i < window && i < length; i++) {
    sum += src[i];
  }

  for (int i = 0; i < length; i++) {
    // Sliding window update
    if (i >= half && (i + half) < length) {
      if (i > half) {
        sum -= src[i - half - 1];
        sum += src[i + half];
      }
      dest[i] = sum / window;
    } else {
      dest[i] = src[i]; // edges left unfiltered
    }
  }
}

void loop() {
  if (bufferA_full) {
    bufferA_full = false;
    applyMovingAverage(bufferA, filtered_buf, SAMPLES_PER_BUFFER, MOVING_AVG_WINDOW);
    for (int i = 0; i < SAMPLES_PER_BUFFER; i++) {
      Serial.println(filtered_buf[i]);
    }
  }

  if (bufferB_full) {
    bufferB_full = false;
    applyMovingAverage(bufferB, filtered_buf, SAMPLES_PER_BUFFER, MOVING_AVG_WINDOW);
    for (int i = 0; i < SAMPLES_PER_BUFFER; i++) {
      Serial.println(filtered_buf[i]);
    }
  }
}
