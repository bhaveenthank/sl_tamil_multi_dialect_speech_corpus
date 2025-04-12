import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
import wave
import os
import numpy as np

# Record and save the audio 
def record_audio(word_num):
    fs = 16000  # Sample rate 
    duration = 2  # Duration 
    
    # Inform the user that recording is starting
    messagebox.showinfo("Recording", f"Recording word {word_num}")
    
    # Start the recording
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait 
    
    # Create new folder for the current speaker 
    folder_name = f"{name_var.get()}_{age_var.get()}_{hometown_var.get()}_{gender_var.get()}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Save the recorded audio to a .wav file
    file_name = f"{folder_name}/Word_{word_num}.wav"
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(np.int16(audio * 32767).tobytes())  
    
    print(f"Saved {file_name}")

# Start recording the 20 words separately
def start_recording():
    # Collect speaker information
    if not name_var.get() or not age_var.get() or not hometown_var.get() or not gender_var.get():
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    # Loop to record each word separately
    for i in range(1, 21):
        record_audio(i)
    
    messagebox.showinfo("Completed", "All 20 words have been recorded!")

# GUI
root = tk.Tk()
root.title("Word Recording App")

# Labels and input fields
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Age").grid(row=1, column=0)
tk.Label(root, text="Hometown").grid(row=2, column=0)
tk.Label(root, text="Gender").grid(row=3, column=0)

name_var = tk.StringVar()
age_var = tk.StringVar()
hometown_var = tk.StringVar()
gender_var = tk.StringVar()

tk.Entry(root, textvariable=name_var).grid(row=0, column=1)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)
tk.Entry(root, textvariable=hometown_var).grid(row=2, column=1)
tk.Entry(root, textvariable=gender_var).grid(row=3, column=1)

# Button to start the process
tk.Button(root, text="Start Recording", command=start_recording).grid(row=4, column=1)

root.mainloop()
