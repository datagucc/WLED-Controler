# 🟡🎛 TouchDesigner controlling WLED 

This repository provides a custom **TouchDesigner Base COMP** named `control_WLED_v1` that allows you to control your WLED-powered LED strips directly from TouchDesigner.

## ✨ Features

This component lets you dynamically control WLED via HTTP JSON requests and UDP requests with real-time interaction through TouchDesigner parameters.

### Available Parameters

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `IP_WLED`   | String      | The IP address of the WLED device (e.g., `192.168.1.5`) |
| `Segment`   | Integer     | The total number of LEDs in your strip (e.g., `300` for a 5-meter strip) |
| `Couleur`   | RGB         | The RGB color to send to the LED strip |
| `Favorite`  | Integer     | The ID of a preset saved in your WLED controller |
| `Speed`     | Integer (0-255) | Controls the animation speed of the effect |
| `Effect_A`  | Float (0.0-1.0) | Controls the intensity or additional parameter of the effect (fade, length, etc.) |
| `Brightness`| Integer (0-255) | Sets the brightness of the LED strip |
| `Blackout`  | Toggle      | Instantly turns off the LEDs when activated |

## 🧠 How It Works

- All parameter changes automatically trigger Python scripts within the component that format and send JSON requests to your WLED device.
- These requests apply the appropriate effect, color, speed, and more to the LED strip.
- A custom blackout toggle sends an `off` command when needed and restores previous settings when turned off.


---

## 🧠 Features

- 🔘 **MIDI Integration**  
  Use your MIDI controller buttons to trigger lighting effects (b1 to b8 mapped).
  
- 🌈 **Visual Sync**  
  Send the dominant color from a TOP (e.g. webcam or rendered scene) directly to WLED.

- 📡 **Preset Trigger**  
  Trigger any saved WLED preset using a single parameter in TouchDesigner.

- 🧰 **Flexible Architecture**  
  Python scripting inside TD allows full customization and automation.

- 🔁 **Blackout Logic**  
  Turn LEDs off with a button and restore previous state upon release.

---

## ⚙️ Requirements

- [WLED](https://kno.wled.ge/) (running on ESP32 or ESP8266) connected to your Wi-Fi
- [TouchDesigner](https://derivative.ca/) (tested with 2023+)
- Python module: `requests` (already included in TD or install manually)
- Local network access to WLED device
- Ensure HTTP control is enabled in WLED (enabled by default)

---

## 🚀 Getting Started

1. Open your TouchDesigner project.
2. Drop or import the `control_WLED_v5` base component.
3. Enter the IP address of your WLED in the `IP_WLED` parameter.
4. Adjust other parameters to interact in real-time with your LEDs.

---

## 🚀 How It Works

1. **Set WLED IP**  
   In the `control_WLED` base COMP, enter your WLED's local IP.

2. **Trigger a Preset**  
   Set the `favorite` parameter (int from 0–15) to call the corresponding WLED effect.

3. **Use MIDI**  
   MIDI buttons b1 to b8 map to different effect values via a Python CHOP Execute.

4. **Visual-Based Color Control**  
   Use a TOP (camera, visuals, etc.) and extract the average color using `TOP to CHOP` to control LED color live.

---

## 📝 Customization

- Modify `/scripts/send_preset.py` to adjust how presets are triggered.
- Update `midi_mapping.py` to change how MIDI inputs control effects.
- Add or edit presets in `wled_presets.json` using the WLED API format.

---


## 📦 Project Structure

WLED_TD_Controller/
├── project.toe              # Main TouchDesigner file
├── wled_presets.json        # JSON preset definitions for WLED
├── scripts/
│   ├── send_preset.py       # Sends JSON request to activate WLED preset
│   ├── color_sync.py        # Sync LED color with TOP average color
│   └── midi_mapping.py      # Maps MIDI button presses to effects
├── docs/
│   └── README.md            # Project documentation
└── requirements.txt         # Python dependencies (e.g. requests)

---

## 📸 Example Use Cases

- Sync LED colors to your webcam or visual composition
- Automate light shows for a DJ set or installation
- Control WLED entirely from TouchDesigner without external UI

---

## 🧪 Future Ideas

- Add audio-reactive effects (microphone input)
- Web UI interface for remote control
- Save/load user presets from TD UI

---

## 🗣 Feedback & Contributions

Feel free to fork this project, suggest improvements, or create pull requests for better integrations or new features.

---
## 🧠 Credits

Made with ❤️ using [WLED](https://kno.wled.ge/) and [TouchDesigner](https://derivative.ca/).  
Built for creative coding, performance, and fun.

---
