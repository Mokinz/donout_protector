import tkinter as tk
from threading import Thread
from facial_recognition import is_user_facing_camera
from system_commands import lock_computer
import time 
from pynput import keyboard, mouse

script_thread = None
running = False

def restart_script_if_inactive():
    global last_input_time, running, script_thread
    while True:
        time.sleep(5)  # Sprawdza co 5 sekund
        if not running and time.time() - last_input_time < 5:
            # Jeśli skrypt nie jest uruchomiony i ostatnia aktywność mniej niż 5 sekund temu
            start_script()

def on_press(key):
    global last_input_time
    last_input_time = time.time()

def on_move(x, y):
    global last_input_time
    last_input_time = time.time()

# Listener na aktywność klawiatury i myszy
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_move=on_move)

keyboard_listener.start()
mouse_listener.start()


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
        if time.time() - last_input_time > 5:
            if not is_user_facing_camera():
                lock_computer()
                # Aktualizacja statusu na GUI po zablokowaniu komputera
                app.after(0, lambda: status_label.config(text="Status: Stopped", fg="red"))
                running = False
                break
            
        time.sleep(5)


restart_thread = Thread(target=restart_script_if_inactive, daemon=True)
restart_thread.start()


# Ustawienia GUI
app = tk.Tk()
app.title("Donut Protector")
app.geometry("150x180")


# Przyciski GUI
start_button = tk.Button(app, text="Start Script", command=start_script)
stop_button = tk.Button(app, text="Stop Script", command=stop_script)
status_label = tk.Label(app, text="Status: Stopped", fg="red")

start_button.pack(pady=10)
stop_button.pack(pady=10)
status_label.pack(pady=10)

# Uruchom GUI
app.mainloop()
