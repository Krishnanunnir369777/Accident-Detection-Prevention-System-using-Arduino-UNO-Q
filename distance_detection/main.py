from arduino.app_utils import *
import time

# --- Configuration ---
STOP_DISTANCE = 100  # Distance in mm to trigger stop

def process_distance(current_dist):
    """
    Receives distance from Arduino and returns the motor state.
    """
    print(f"Object detected at: {current_dist} mm")

    if current_dist < STOP_DISTANCE:
        print("STATUS: Object too close! Sending STOP command.")
        return "STOP"
    else:
        return "RUN"

# Register the function so the Arduino can call it
Bridge.provide("process_distance", process_distance)

print("Distance-based Safety System Started...")
App.run()