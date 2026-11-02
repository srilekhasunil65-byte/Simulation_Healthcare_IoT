# Smart Healthcare Patient Monitoring System

### IoT-Based Multi-Patient Monitoring Simulation

A software-based IoT healthcare monitoring project designed to simulate multiple patients, collect vital-sign readings, transmit data through MQTT, store readings in an SQLite database, and display patient information through a web dashboard.

> **Project Type:** Software-Based IoT Simulation
> **Domain:** Healthcare | Internet of Things | Network Communication
> **Status:** Academic Project

---

## 1. Project Overview

The Smart Healthcare Patient Monitoring System is an IoT-based software simulation that demonstrates how patient health information can be collected, transmitted, stored, and monitored through a centralized platform.

The system uses a Python-based patient simulator to generate sample health readings, including heart rate, body temperature, and oxygen saturation (SpO₂). MQTT communication is used to transmit the simulated readings, while SQLite stores the received data.

A Flask-based web dashboard provides a centralized interface to view patient information and monitoring results.

This project demonstrates the integration of healthcare monitoring concepts with IoT communication protocols, database management, and network simulation technologies.

## 2. Project Objectives

* Simulate health readings for multiple patients.
* Demonstrate IoT-based data communication.
* Implement MQTT publish-subscribe communication.
* Store patient readings using SQLite.
* Display monitoring information through a Flask dashboard.
* Explore CoAP communication.
* Explore IPv6 and 6LoWPAN networking using Contiki-NG and Cooja.

## 3. Technology Stack

| Category               | Technology         |
| ---------------------- | ------------------ |
| Programming Language   | Python             |
| Web Framework          | Flask              |
| Frontend               | HTML, CSS          |
| Database               | SQLite             |
| Messaging Protocol     | MQTT               |
| MQTT Library           | Paho MQTT          |
| IoT Protocol           | CoAP               |
| CoAP Library           | aiocoap            |
| Network Simulation     | Contiki-NG         |
| Simulation Environment | Cooja              |
| Network Technology     | IPv6, 6LoWPAN, RPL |

## 4. System Architecture

```text
       MULTI-PATIENT SIMULATOR
                 |
                 v
         SIMULATED VITAL DATA
                 |
                 v
          MQTT PUBLISHER
                 |
                 v
          MQTT BROKER
                 |
                 v
          MQTT SUBSCRIBER
                 |
                 v
          SQLITE DATABASE
                 |
                 v
          FLASK WEB SERVER
                 |
                 v
          WEB DASHBOARD
```

Additional networking components:

* CoAP Server and Client – implementation for IoT resource communication.
* Contiki-NG and Cooja – IPv6 and 6LoWPAN network simulation exploration.

## 5. Patient Parameters

The simulator generates the following sample readings:

| Parameter   | Description                 | Unit        |
| ----------- | --------------------------- | ----------- |
| Heart Rate  | Simulated heart rate        | BPM         |
| Temperature | Simulated body temperature  | °C          |
| SpO₂        | Simulated oxygen saturation | %           |
| Timestamp   | Reading generation time     | Date & Time |

Five sample patient profiles are used for demonstration.

**Note:** All patient profiles and health readings are simulated data.

## 6. Project Modules

### 6.1 Multi-Patient Simulator

Generates sample vital-sign readings for multiple patients using Python.

### 6.2 MQTT Publisher

Publishes simulated patient readings to an MQTT broker.

### 6.3 MQTT Subscriber

Receives MQTT messages and stores the readings in the SQLite database.

### 6.4 Database Management

Uses SQLite to store patient details and monitoring records.

### 6.5 Flask Dashboard

Displays patient information and their latest monitoring readings through a web interface.

### 6.6 CoAP Communication

Includes CoAP client and server implementations for exploring resource-based IoT communication.

### 6.7 Contiki-NG and Cooja

Explores IoT networking concepts such as IPv6, 6LoWPAN, RPL, and simulated network nodes.

## 7. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Smart-Healthcare-Patient-Monitoring
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Start MQTT Subscriber

Open Terminal 1:

```bash
python mqtt_subscriber.py
```

### Step 5: Start Patient Simulator

Open Terminal 2:

```bash
python sensor_simulator.py/multi_patient_simulator.py
```

**Note:** Update this command if the simulator folder is renamed during project organization.

### Step 6: Start Flask Dashboard

Open Terminal 3:

```bash
python app.py
```

### Step 7: Open the Dashboard

Open your browser:

```text
http://127.0.0.1:5000
```

## 8. Communication Workflow

1. The simulator generates sample patient readings.
2. The MQTT publisher sends the readings to the MQTT broker.
3. The MQTT subscriber receives the published messages.
4. The subscriber stores the received readings in SQLite.
5. The Flask application retrieves the stored information.
6. The dashboard displays the available patient monitoring data.

## 9. Network Simulation

Contiki-NG and Cooja are used to explore IoT networking concepts.

The simulation environment includes:

* IEEE 802.15.4
* 6LoWPAN
* IPv6 addressing
* RPL routing
* UDP-based communication experiments

The Cooja environment was used to compile and run native simulation motes and inspect network activity.

## 10. Future Enhancements

* Integration with physical IoT sensors.
* Secure MQTT communication using TLS.
* Patient authentication and access control.
* Alert notifications for abnormal readings.
* Advanced patient history visualization.
* Cloud-based data storage.
* Hospital system integration.

## 11. Project Limitations

* The current project uses simulated patient readings instead of physical medical sensors.
* The sample patient profiles are not real patient registrations.
* CoAP client-server connectivity requires further verification.
* Cooja UDP client reachability requires further testing.
* The system is intended for academic demonstration, not clinical use.

## 12. Disclaimer

This project is developed for educational and academic purposes. All patient information and health readings are simulated. The system is not intended for medical diagnosis, treatment, or emergency healthcare decisions.

## 13. Author

**Sri Lekha**

B.Sc. Computer Science – Cyber Security

**Project:** Smart Healthcare Patient Monitoring System – IoT Simulation

---

*Developed as an academic project to explore the integration of IoT communication, database management, web technologies, and network simulation.*

