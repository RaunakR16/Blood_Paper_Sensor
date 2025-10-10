#include "hardware/adc.h"
#include "hardware/dma.h"

// ===== CONFIG =====
const uint CAPTURE_CHANNEL = 0;    // ADC channel 0 = A0
const uint SAMPLES_PER_BUFFER = 256;  // Samples per DMA transfer
const float ADC_CLOCK_DIV = 0;     // 0 = fastest (about 500 kS/s typical)

// ===== BUFFERS =====
uint16_t bufferA[SAMPLES_PER_BUFFER];
uint16_t bufferB[SAMPLES_PER_BUFFER];

int dma_chan;
dma_channel_config dma_config;

// ===== FLAGS =====
volatile bool bufferA_full = false;
volatile bool bufferB_full = false;

// DMA IRQ Handler
void dma_handler() {
  // Determine which buffer finished
  if (dma_hw->ints0 & (1u << dma_chan)) {
    dma_hw->ints0 = 1u << dma_chan; // Clear interrupt

    // Flip between buffers
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
  adc_gpio_init(26 + CAPTURE_CHANNEL); // GPIO26 = ADC0 = A0
  adc_select_input(CAPTURE_CHANNEL);

  adc_fifo_setup(
    true,  // Write each sample to FIFO
    true,  // Enable DMA request (DREQ)
    1,     // DREQ when at least 1 sample ready
    false, // No error bit
    false  // No byte shift
  );

  adc_set_clkdiv(ADC_CLOCK_DIV);  // Fastest possible sampling
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
    bufferA,            // initial write address
    &adc_hw->fifo,      // read from ADC FIFO
    SAMPLES_PER_BUFFER, // transfer count
    false               // don’t start yet
  );

  // ===== DMA Interrupt =====
  dma_channel_set_irq0_enabled(dma_chan, true);
  irq_set_exclusive_handler(DMA_IRQ_0, dma_handler);
  irq_set_enabled(DMA_IRQ_0, true);

  // ===== Start Conversion =====
  adc_run(true);
  dma_channel_start(dma_chan);

  Serial.println("Continuous ADC capture started...");
}

void loop() {
  // When bufferA is full, print it
  if (bufferA_full) {
    bufferA_full = false;
    for (int i = 0; i < SAMPLES_PER_BUFFER; i++) {
      Serial.println(bufferA[i]);
    }
  }

  // When bufferB is full, print it
  if (bufferB_full) {
    bufferB_full = false;
    for (int i = 0; i < SAMPLES_PER_BUFFER; i++) {
      Serial.println(bufferB[i]);
    }
  }
}
