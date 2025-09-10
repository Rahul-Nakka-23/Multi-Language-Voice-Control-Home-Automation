# 🏠 Multi-Language-Voice-Control-Home-Automation

An Android app to control home appliances (bulbs, fans, etc.) via Raspberry Pi using voice commands and mobile controls.  
The project supports **multilingual voice input** (English, Hindi, Telugu, Kannada) and provides a clean mobile UI to toggle loads individually or all at once.

---

## ✨ Features

- 🎤 **Voice Control** via Raspberry Pi + Google Speech API
- 📱 **Mobile App Control** with Material Design UI
- 🌐 **REST API** communication between App ↔ Raspberry Pi
- ⚡ Control up to **4 individual loads** (Load1–Load4) + **All Loads On/Off**
- 🌙 Supports **Dark Mode** (Material3 theme)
- 🔐 Future-ready for adding **authentication**

---

## 📱 Android App

Built in **Kotlin** with:

- Material3 UI
- Retrofit + OkHttp for network requests
- Coroutines for async operations
- ViewBinding for easy UI handling

**App Screens:**

1. Enter and save Raspberry Pi IP Address
2. Toggle Load1–4 On/Off
3. Control All Loads On/Off

---

## 🤖 Raspberry Pi Setup

The Raspberry Pi runs a Python server connecting GPIO pins → relay module → appliances.

Two approaches:

1. **Voice-based control** using Google Speech Recognition
2. **HTTP API** with Flask server (so the Android app can send commands)

**GPIO Mapping (as per project):**

| Load  | GPIO Pin |
|-------|----------|
| Load1 | 27       |
| Load2 | 17       |
| Load3 | 22       |
| Load4 | 23       |

**Start the Flask Server:**

```bash
sudo python3 flask_control.py
```
## 🛠 Project Structure
```bash
HomeAutomationApp/
│
├── app/
│   ├── build.gradle                 # Module-level Gradle config
│   └── src/main/
│       ├── AndroidManifest.xml      # App manifest + permissions
│       ├── java/com/example/homeautomation/
│       │   └── MainActivity.kt      # Main logic
│       └── res/
│           ├── layout/activity_main.xml  # UI Layout
│           ├── values/strings.xml       # App strings
│           ├── values/colors.xml        # Theme colors
│           ├── values/themes.xml        # Light theme
│           ├── mipmap-anydpi-v26/ic_launcher.xml  # App icon
│
├── build.gradle                    # Project-level Gradle config
├── settings.gradle                 # Project name + modules
├── proguard-rules.pro              # ProGuard config for release build
└── README.md                       # This file
```
