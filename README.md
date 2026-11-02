# Simulation_Healthcare_IoT
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

| Parameter   | Description          | Unit |
| ----------- | -------------------- | ---- |
| Heart Rate  | Simulated heart rate | BPM  |
| Temperature | Simulat              |      |
