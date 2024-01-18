import tkinter as tk
from threading import Thread
from facial_recognition import is_user_facing_camera
from system_commands import lock_computer
import time 

def start_script():
    global script_thread, status_label
    if script_thread is None or not script_thread.is_alive():
        script_thread = Thread(target=run_script)
        script_thread.start()
        status_label.config(text="Status: Running", fg="green")

def stop_script():
    global running, status_label
    running = False
    if script_thread is not None and script_thread.is_alive():
        script_thread.join()
    status_label.config(text="Status: Stopped", fg="red")

def run_script():
    global running, status_label
    running = True
    while running:
        if not is_user_facing_camera():
            lock_computer()
            # Aktualizacja statusu na GUI po zablokowaniu komputera
            app.after(0, lambda: status_label.config(text="Status: Stopped", fg="red"))
            running = False
            break
        time.sleep(5)

# Ustawienia GUI
app = tk.Tk()
app.title("Face Detection Control")
app.geometry("300x200")

script_thread = None
running = False

# Przyciski GUI
start_button = tk.Button(app, text="Start Script", command=start_script)
stop_button = tk.Button(app, text="Stop Script", command=stop_script)
status_label = tk.Label(app, text="Status: Stopped", fg="red")

start_button.pack(pady=10)
stop_button.pack(pady=10)
status_label.pack(pady=10)

# Uruchom GUI
app.mainloop()
