# 🎧 DSP Audio Signal Analysis Project

Real-time audio signal processing system using Arduino and Python.

---

# 📌 Project Overview

This project is designed to capture and analyze live sound signals using a microphone sensor connected to Arduino.  
The sound data is transmitted to a Python application where it is processed and visualized in real time using a graphical user interface.

The system can classify sound intensity into different emotional states such as:

- 😌 Calm
- 🙂 Normal
- 😡 Angry

---

# 🚀 Features

- Real-time sound signal acquisition
- Live waveform visualization
- Dynamic sound level analysis
- Emotional state classification
- Dark mode graphical interface
- Arduino & Python integration

---

# 🛠️ Technologies Used

## Hardware
- Arduino Uno
- Microphone Sensor

## Software
- Python
- Tkinter
- Matplotlib
- NumPy
- PySerial

---

# 📂 Project Files

| File | Description |
|------|-------------|
| `python_gui.py` | Main Python GUI application |
| `arduino_code.ino` | Arduino sound acquisition code |
| `technical_report.pdf` | Full project technical report |
| `audio_presentation.pptx` | Project presentation slides |
| `recording.mp4` | Demo video of the system |
| `banar.jpeg` | Project banner |
| `login.jpeg` | Login interface screenshot |

---

# ⚙️ How It Works

1. The microphone sensor captures sound signals.
2. Arduino reads analog sound values.
3. Peak-to-peak sound levels are calculated.
4. Data is sent to Python via serial communication.
5. Python processes the signal.
6. Live waveform is displayed.
7. Sound intensity is classified in real time.

---

# 🔌 Circuit Connection

- Microphone OUT → A0 on Arduino
- VCC → 5V
- GND → GND

---

# ▶️ How to Run

## Arduino
1. Upload `arduino_code.ino` to Arduino Uno.
2. Connect the microphone sensor properly.
3. Open serial communication at `9600 baud`.

## Python
Install required libraries:

```bash
pip install pyserial numpy matplotlib
