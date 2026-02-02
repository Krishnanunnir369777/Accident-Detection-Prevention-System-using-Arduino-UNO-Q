Transform your Arduino UNO Q into an intelligent vehicle safety assistant that continuously monitors the driver and surroundings to prevent accidents before they happen.

This project combines distance sensing, engine temperature monitoring, and AI-based driver drowsiness detection to automatically trigger alerts and safety actions such as slowing down the vehicle using a servo motor and sending emergency notifications.

✨ Features

👁 Driver Drowsiness Detection using camera + AI

📏 Obstacle Distance Detection to avoid frontal collisions

🌡 Engine Temperature Monitoring for overheating detection

🤖 Servo-based Speed Control for automatic deceleration

📲 Real-time Alerts via SMS in critical conditions

🔁 Arduino–Python Bridge Communication (App Lab compatible)

🧠 System Overview

The system works in real time using a hybrid architecture:

Arduino UNO Q handles sensors and actuators

Python (Arduino App Lab) runs AI and decision logic

Camera → Drowsiness Detection (AI)
                    ↓
Temperature Sensor → Safety Logic → Servo Control → Accident Prevention
                    ↓
Distance Sensor → Collision Avoidance
                    ↓
                SMS Alerts

🧩 Components Used
Hardware

Arduino UNO Q

Distance Sensor (Modulino Distance)

Temperature Sensor (Modulino Thermo)

Servo Motor (for speed control / braking simulation)

USB Camera (driver monitoring)

Vehicle power supply / USB power

Software & Libraries

Arduino IDE / Arduino App Lab

Python 3

OpenCV

MediaPipe

NumPy

Twilio API (SMS alerts)

Arduino RouterBridge

Arduino Modulino Libraries

⚙️ How It Works

Distance Monitoring

Continuously measures distance to the object in front

If distance drops below a safe threshold → vehicle slows down automatically

Temperature Monitoring

Monitors engine temperature in real time

If temperature exceeds limit → alert is triggered

Driver Drowsiness Detection

Uses camera + facial landmark detection

Calculates Eye Aspect Ratio (EAR)

If eyes remain closed for more than a few seconds → drowsiness detected

Accident Prevention

System sends commands back to Arduino

Servo motor reduces speed / simulates braking

Emergency SMS alert is sent to registered phone number

🛠️ Installation & Setup
Arduino Libraries
arduino-cli lib update-index
arduino-cli lib install Arduino_Modulino
arduino-cli lib install Arduino_RouterBridge
arduino-cli lib install Servo

Python Dependencies
pip install opencv-python mediapipe numpy requests twilio

▶️ Running the Project

Upload sketch.ino to Arduino UNO Q

Open Arduino App Lab

Run main.py

Connect the camera

Place an object in front of the distance sensor

Observe servo movement and alert messages
