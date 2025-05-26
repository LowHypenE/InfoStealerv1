# 🖥️ Silent PC Audit Tool

This Python-based tool silently collects detailed system information from a Windows PC and sends it to a specified Discord webhook. It runs in stealth mode (no visible console) and includes screenshot capture, webcam image (if available), clipboard data, running processes, and connected hardware details.

## 🚀 Features

* Hidden console window (stealth mode)
* Sends reports automatically every 2 hours
* Captures:

  * System info (OS, processor, uptime, etc.)
  * IP address and connected Wi-Fi SSID
  * Installed antivirus software
  * Top CPU-consuming processes
  * Connected devices
  * Clipboard content
  * Screenshot of current display
  * Webcam photo (if available)
* Sends images and report to Discord webhook
* Mentions @everyone on each report

---

## 📁 File Structure

```
Silent-PC-Audit/
├── main.py              # Main script (reporting logic)
├── README.md            # Project documentation
├── requirements.txt     # Required dependencies
```

---

## ⚙️ Requirements

* Python 3.8 or newer
* Windows OS

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Packaging (Optional)

You can convert it into an executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile main.py
```

---

## 🔁 Auto Execution

This script is designed to:

* Run in the background
* Send new data every 2 hours

---

## 📜 Legal Notice

> This project is for **educational** and **ethical research** purposes only. Unauthorized surveillance or data collection is illegal. Do **not** use this tool without **explicit consent** from the machine owner.\\

 <\<USE AT YOUR OWN RISK. DO NOT DISTRIBUTE UNDER YOUR NAME OR TAKE CREDIT FOR THIS CONTENTS>>
