from arduino.app_utils import *
import requests
import time

# --- Twilio Configuration ---
TWILIO_SID = "AC243917588919687e209236e2f0525ca7"
TWILIO_AUTH_TOKEN = "90f2929edc93f8771c0bacb16c551dd8"
TWILIO_FROM = "+14472273953"
TO_NUMBER = "+916282675819"

# --- Thresholds & Cooldowns ---
TEMP_LIMIT = 32.0            # Alert if above 75°C
HEARTBEAT_INTERVAL = 1800    # 30-minute status update (1800s)
ALERT_COOLDOWN = 300         # 5-minute cooldown for emergency alerts

last_heartbeat_time = time.time()
last_alert_time = 0

def send_sms(message):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"
    payload = {"From": TWILIO_FROM, "To": TO_NUMBER, "Body": message}
    try:
        r = requests.post(url, data=payload, auth=(TWILIO_SID, TWILIO_AUTH_TOKEN))
        if r.status_code == 201:
            print(f"SMS Sent: {message}")
            return True
    except Exception as e:
        print(f"Twilio Error: {e}")
    return False

def process_temperature(current_temp):
    """Called by Arduino to report temperature and handle logic."""
    global last_heartbeat_time, last_alert_time
    curr_time = time.time()
    
    print(f"Monitoring Engine... Temp: {current_temp}°C")

    # 1. Emergency Overheat Logic
    if current_temp > TEMP_LIMIT:
        if curr_time - last_alert_time > ALERT_COOLDOWN:
            if send_sms(f"⚠️ CRITICAL: Engine Hot! {current_temp}C"):
                last_alert_time = curr_time

    # 2. 30-Minute Status Update
    if curr_time - last_heartbeat_time > HEARTBEAT_INTERVAL:
        if send_sms(f"✅ System OK: Temp {current_temp}C"):
            last_heartbeat_time = curr_time

    return "OK"

# Register the function so Arduino can call it
Bridge.provide("process_temperature", process_temperature)

print("Accident Rectification AI Monitoring Started...")
App.run()