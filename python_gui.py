import serial
import tkinter as tk
from tkinter import ttk
import numpy as np
import time
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- CONFIG ----------------
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600
MAX_POINTS = 120

# ---------------- DATA ----------------
sound_data = deque([0]*MAX_POINTS, maxlen=MAX_POINTS)
buffer = deque([0]*15, maxlen=15)

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)

baseline = []

# ---------------- LOGIN ----------------
login = tk.Tk()
login.title("User Info")

tk.Label(login, text="Name").pack()
name_entry = tk.Entry(login)
name_entry.pack()

tk.Label(login, text="Age").pack()
age_entry = tk.Entry(login)
age_entry.pack()

# ---------------- START APP ----------------
def start():

    global baseline

    user_name = name_entry.get()
    user_age = age_entry.get()

    login.destroy()

    root = tk.Tk()
    root.title(f"Voice Monitor - {user_name}")
    root.geometry("900x650")
    root.configure(bg="#0f1117")

    # ---------------- INFO ----------------
    info = tk.Label(
        root,
        text=f"{user_name} | Age: {user_age}",
        font=("Arial", 14),
        fg="white",
        bg="#0f1117"
    )
    info.pack()

    # ---------------- STATE ----------------
    state_label = tk.Label(
        root,
        text="Starting...",
        font=("Arial", 16),
        fg="white",
        bg="#0f1117"
    )
    state_label.pack(pady=10)

    # ---------------- PROGRESS ----------------
    progress = ttk.Progressbar(root, length=400, maximum=700)
    progress.pack(pady=10)

    # ---------------- GRAPH (FIXED) ----------------
    fig, ax = plt.subplots(figsize=(6,3.8))
    fig.tight_layout(pad=2.0)

    # 🔥 BLACK BACKGROUND
    fig.patch.set_facecolor("#0b0d12")
    ax.set_facecolor("#000000")

    line, = ax.plot(list(sound_data), color="#00ffcc")

    # 🔥 SCALE FIXED
    ax.set_ylim(0, 700)
    ax.set_xlim(0, MAX_POINTS)

    # styling
    ax.tick_params(colors="white")
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('black')
    ax.spines['right'].set_color('black')

    ax.set_title("Live Sound Graph", color="white")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # ---------------- STATE FUNCTION ----------------
    def get_state(value, base):

        if value < base + 10:
            return "Calm 😌", "green"

        elif value < base + 40:
            return "Normal 🙂", "blue"

        else:
            return "Angry 😡", "red"

    # ---------------- UPDATE ----------------
    def update():

        global baseline

        try:

            if ser.in_waiting:

                val = ser.readline().decode().strip()

                if val.isdigit():

                    val = int(val)

                    sound_data.append(val)
                    buffer.append(val)

                    avg = sum(buffer) / len(buffer)

                    # learning baseline
                    if len(baseline) < 50:
                        baseline.append(avg)
                        base = np.mean(baseline)
                    else:
                        base = np.mean(baseline[-50:])

                    state, color = get_state(avg, base)

                    state_label.config(
                        text=f"{state} | Level: {int(avg)}",
                        fg=color
                    )

                    progress["value"] = avg

                    # smooth graph
                    temp = list(sound_data)

                    smooth_graph = []

                    for i in range(len(temp)):

                        start = max(0, i-2)

                        smooth_graph.append(
                            sum(temp[start:i+1]) / len(temp[start:i+1])
                        )

                    line.set_ydata(smooth_graph)

                    # keep scale safe
                    ax.set_ylim(0, 700)

                    canvas.draw_idle()

        except:
            pass

        root.after(20, update)

    update()
    root.mainloop()

# ---------------- BUTTON ----------------
tk.Button(login, text="Start", command=start).pack(pady=10)

login.mainloop()