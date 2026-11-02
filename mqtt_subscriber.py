import paho.mqtt.client as mqtt
import json
from database import create_database, insert_patient_data

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "smarthealthcare/patient/P001"

create_database()

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("MQTT Subscriber Connected!")
        client.subscribe(TOPIC)
        print("Subscribed to:", TOPIC)
    else:
        print("Connection Failed:", reason_code)

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())

        insert_patient_data(
            data["patient_id"],
            data["heart_rate"],
            data["temperature"],
            data["spo2"],
            data["timestamp"]
        )

        print("Patient Data Received and Saved!")
        print(data)

    except Exception as error:
        print("Error:", error)

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="PatientSubscriberSri"
)

client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    client.loop_forever()
except KeyboardInterrupt:
    print("Subscriber Stopped.")
finally:
    client.disconnect()