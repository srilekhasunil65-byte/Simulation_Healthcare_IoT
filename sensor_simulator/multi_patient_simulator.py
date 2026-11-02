import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

import random
import time
import json
import paho.mqtt.client as mqtt

from datetime import datetime
from database import (
    create_database,
    register_patient,
    insert_patient_data
)

# MQTT Configuration
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "sri/smarthealthcare/patient"

# Create database
create_database()

# Sample simulated patients
patients = [
    ("Arun", 25, "Male"),
    ("Priya", 22, "Female"),
    ("Kumar", 45, "Male"),
    ("Meena", 35, "Female"),
    ("Divya", 28, "Female")
]

# Connect MQTT Publisher
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="SriHealthcarePublisher"
)

client.connect(BROKER, PORT, 60)
client.loop_start()

print("MQTT Publisher Connected!")
print("SMART HEALTHCARE MONITORING STARTED")

# Register patients
registered_patients = []

for name, age, gender in patients:
    patient_id = register_patient(name, age, gender)
    registered_patients.append(patient_id)

try:
    while True:

        for patient_id in registered_patients:

            heart_rate = random.randint(60, 120)
            temperature = round(random.uniform(36.0, 39.0), 1)
            spo2 = random.randint(90, 100)

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            data = {
                "patient_id": patient_id,
                "heart_rate": heart_rate,
                "temperature": temperature,
                "spo2": spo2,
                "timestamp": timestamp
            }

            # Save to SQLite
            insert_patient_data(
                patient_id,
                heart_rate,
                temperature,
                spo2,
                timestamp
              )

            # Publish through MQTT
            topic = f"{TOPIC}/{patient_id}"

            result = client.publish(
                topic,
                json.dumps(data),
                qos=1
            )

            result.wait_for_publish()

            print("\nPatient:", patient_id)
            print("Heart Rate:", heart_rate, "BPM")
            print("Temperature:", temperature, "°C")
            print("SpO2:", spo2, "%")
            print("MQTT Topic:", topic)
            print("Saved to Database and Published!")

        time.sleep(5)

except KeyboardInterrupt:
    print("\nMonitoring Stopped.")

finally:
    client.loop_stop()
    client.disconnect()
