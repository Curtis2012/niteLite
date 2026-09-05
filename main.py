# niteLite - ESP32 LED Flasher
# MicroPython code to flash an LED connected to GPIO16
# Reads a photocell on GPIO35 and controls LED based on light level


from machine import Pin, ADC
import time
from config import LED_PIN, PHOTOCELL_PIN, DARK_THRESHOLD, LIGHT_THRESHOLD


# Configure LED and photocell pins from config
led = Pin(LED_PIN, Pin.OUT)
photocell = ADC(Pin(PHOTOCELL_PIN))
photocell.atten(ADC.ATTN_11DB)  # Full range: 0-4095


print("niteLite LED Flasher Starting...")
print(f"LED connected to GPIO{LED_PIN}")
print(f"Photocell connected to GPIO{PHOTOCELL_PIN}")
print(f"Dark threshold: {DARK_THRESHOLD}, Light threshold: {LIGHT_THRESHOLD}")
print("Press Ctrl+C to stop")

try:
    while True:
        value = photocell.read()
        print(f"Photocell value: {value}")

        if value < DARK_THRESHOLD:
            led.on()
            print("LED ON (dark detected)")
        elif value > LIGHT_THRESHOLD:
            led.off()
            print("LED OFF (light detected)")
        # If value is between thresholds, keep previous state

        time.sleep(0.5)  # Adjust polling interval as needed

except KeyboardInterrupt:
    # Clean shutdown when Ctrl+C is pressed
    led.off()
    print("\nProgram stopped - LED turned off")
    print("niteLite shutdown complete")