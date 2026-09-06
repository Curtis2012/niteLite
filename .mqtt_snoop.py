import time
import yaml
import paho.mqtt.client as mqtt

# Read from the local (gitignored) secrets.yaml so the real broker
# hostname never ends up hardcoded in a tracked file.
with open("secrets.yaml") as f:
    BROKER = yaml.safe_load(f)["mqtt_broker"]
TOPICS = ["homeassistant/#", "nitelite/#", "nitelite-7f1880/#"]
messages = []

def on_connect(client, userdata, flags, rc):
    for t in TOPICS:
        client.subscribe(t)

def on_message(client, userdata, msg):
    messages.append((msg.topic, msg.retain, msg.payload.decode(errors="replace")))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_start()
time.sleep(6)
client.loop_stop()
client.disconnect()

for topic, retain, payload in messages:
    if "nitelite" in topic.lower() or "nitelite" in payload.lower():
        print(f"[retain={retain}] {topic} = {payload}")
