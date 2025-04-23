# 🎛 TouchDesigner WLED Controller

A complete **TouchDesigner** project to control **WLED** lighting effects. This setup allows you to send JSON commands to an ESP32 running WLED, with full control via MIDI, visuals, and Python scripting.

---

## 📦 Project Structure
/WLED_TD_Controller/
│
├── project.toe                # Main TouchDesigner file
├── wled_presets.json          # WLED preset definitions
├── /scripts/
│   ├── send_preset.py         # Send preset ID via POST request
│   ├── color_sync.py          # Sends TOP color average to WLED
│   └── midi_mapping.py        # Maps MIDI buttons to effect values
│
├── /docs/
│   └── README.md              # This documentation
│
└── requirements.txt           # Python dependencies


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

- [WLED](https://kno.wled.ge/) (running on ESP32 or ESP8266)
- [TouchDesigner](https://derivative.ca/) (tested with 2023+)
- Python module: `requests` (already included in TD or install manually)
- Local network access to WLED device

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

## 🧠 Credits

Made with ❤️ using [WLED](https://kno.wled.ge/) and [TouchDesigner](https://derivative.ca/).  
Built for creative coding, performance, and fun.

---
