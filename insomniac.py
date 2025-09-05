#!/usr/bin/env python3
"""
Insomniac - Never let your computer sleep
A simple tool that keeps your system awake by subtly moving the mouse cursor.
Press Ctrl+C to stop.
"""

import time
import random
import signal
import sys
try:
    import pyautogui
except ImportError:
    print("pyautogui is not installed. Please install it first:")
    print("pip install pyautogui")
    sys.exit(1)


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n[*] Insomniac stopped. Your computer can sleep peacefully now.")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    
    pyautogui.FAILSAFE = False
    
    print("""
    ___                                 _            
   |_ _|_ __  ___  ___  _ __ ___  _ __ (_) __ _  ___ 
    | || '_ \/ __|/ _ \| '_ ` _ \| '_ \| |/ _` |/ __|
    | || | | \__ \ (_) | | | | | | | | | | (_| | (__ 
   |___|_| |_|___/\___/|_| |_| |_|_| |_|_|\__,_|\___|
    
    Keeping your computer awake...
    """)
    
    print("[*] Press Ctrl+C to stop")
    print("[*] Moving mouse every 3-5 seconds...")
    print("[*] Initial mouse position:", pyautogui.position())
    print("-" * 50)
    
    move_count = 0
    
    while True:
        current_x, current_y = pyautogui.position()
        
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        
        new_x = max(0, current_x + offset_x)
        new_y = max(0, current_y + offset_y)
        
        screen_width, screen_height = pyautogui.size()
        new_x = min(new_x, screen_width - 1)
        new_y = min(new_y, screen_height - 1)
        
        print(f"[{move_count+1}] Moving from ({current_x}, {current_y}) -> ({new_x}, {new_y}) [offset: ({offset_x:+d}, {offset_y:+d})]")
        
        pyautogui.moveTo(new_x, new_y, duration=0.25)
        
        move_count += 1
        
        sleep_time = random.uniform(3, 5)
        print(f"    Sleeping for {sleep_time:.1f} seconds...")
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()