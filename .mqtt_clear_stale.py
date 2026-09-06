import paho.mqtt.publish as publish

BROKER = "cscrpi4B.local"

# Orphaned retained topics from the old name_add_mac_suffix attempt
# (superseded by the nitelite2.yaml device). Empty retained payload clears them.
STALE_TOPICS = [
    "homeassistant/sensor/nitelite-7f1880/nitelite_photocell/config",
    "homeassistant/number/nitelite-7f1880/nitelite_random_interval/config",
    "homeassistant/light/nitelite-7f1880/nitelite/config",
    "nitelite-7f1880/number/nitelite_random_interval/state",
    "nitelite-7f1880/sensor/nitelite_photocell/state",
    "nitelite-7f1880/light/nitelite/state",
]

for topic in STALE_TOPICS:
    publish.single(topic, payload=None, retain=True, hostname=BROKER)
    print(f"cleared {topic}")
