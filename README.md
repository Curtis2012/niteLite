# niteLite

An ESPHome-based night light for ESP32, fully controlled/configured from Home
Assistant. Drives a 4-pin RGB LED and exposes ambient light level as a
sensor.

> The original MicroPython version (`main.py`, `boot.py`, `config.py`) is kept
> for reference but is superseded by `nitelite.yaml`. Flashing ESPHome
> firmware replaces MicroPython entirely on the device.

## Hardware
- ESP32 dev board (MINI32 V1.0.0, ESP-WROOM-32)
- 4-pin RGB LED (common-cathode assumed) - R/G/B legs on GPIO16/GPIO17/GPIO18,
  common leg to GND (through appropriate current-limiting resistors on each
  color leg)
- Photocell (LDR) on GPIO35 (ADC1), with a series resistor (e.g. 5K) to form a
  voltage divider

If your RGB LED is common-anode instead (common leg to 3.3V), add
`inverted: true` to each of the three `output:` entries in `nitelite.yaml`.

## Home Assistant features
- **Light entity ("NiteLite")**: standard HA light card - full RGB color
  picker (palette) and brightness slider, on/off from HA.
- **Default state**: on first-ever boot the light initializes to white at
  50% brightness. After that, ESPHome restores the last on/off/color state
  across reboots.
- **Random Color effect**: select "Random Color" from the light's Effect
  dropdown in HA. While active, the LED periodically jumps to a new random
  color.
- **NiteLite Random Interval** (number entity): sets how many seconds each
  color is shown for while the Random Color effect is running (1-300s,
  default 10s).
- **NiteLite Photocell** (sensor entity): raw ADC reading (0-4095) of ambient
  light level. Exposed for use in your own HA automations/schedules (e.g. to
  turn the light on/off based on darkness or time of day) - the device itself
  does not gate on/off based on light level.

## Setup
1. Copy `secrets.yaml.example` to `secrets.yaml` and fill in real values
   (Wi-Fi credentials, MQTT broker host, OTA password). `secrets.yaml` is
   gitignored.
2. Install ESPHome (`pip install esphome` or use the Home Assistant ESPHome
   add-on).
3. Flash: `esphome run nitelite.yaml` (first flash needs USB; later updates
   go over-the-air).
4. The device connects to the local MQTT broker (plain, no TLS/auth) and is
   discovered by Home Assistant's MQTT integration automatically.

## Files
- `nitelite.yaml`: ESPHome device configuration
- `secrets.yaml.example`: template for required secrets
- `main.py`, `config.py`, `boot.py`: legacy MicroPython firmware (reference only)
