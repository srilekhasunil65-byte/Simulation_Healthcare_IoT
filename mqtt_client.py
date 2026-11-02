import paho.mqtt.client as mqtt
import json
import random
import time
from datetime import datetime

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "smarthealthcare/patient/P001"

def generate_data():
    return {
        "patient_id": "P001",
        "heart_rate": random.randint(60, 120),
        "temperature": round(random.uniform(36.0, 39.0), 1),
        "spo2": random.randint(90, 100),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="PatientPublisherSri"
)

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("MQTT Publisher Connected!")

    while True:
        data = generate_data()
        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)
        time.sleep(3)

except KeyboardInterrupt:
    print("Publisher Stopped.")

except Exception as error:
    print("MQTT Error:", error)

finally:
    client.loop_stop()
    client.disconnect()