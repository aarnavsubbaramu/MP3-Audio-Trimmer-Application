import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

main_window = tk.Tk()
main_window.title("MP3 Trimmer App")

file_label = tk.Label(main_window, text = "Select MP3 file:")
file_label.pack()
file_button = tk.Button(main_window, text = "Browse", command = lambda: filedialog.askopenfilename())
file_button.pack()

start_label = tk.Label(main_window, text = "Start time (seconds):")
start_label.pack()
start_spinbox = tk.Spinbox(main_window, from_ = 0, to = 100, width = 5)
start_spinbox.pack()

end_label = tk.Label(main_window, text = "End time (seconds):")
end_label.pack()
end_spinbox = tk.Spinbox(main_window, from_ = 0, to = 100, width = 5)
end_spinbox.pack()

trim_button = tk.Button(main_window, text = "Trim MP3", command = lambda: trim_mp3())
trim_button.pack()

status_label = tk.Label(main_window, text = "")
status_label.pack()

def trim_mp3():
    file_path = filedialog.askopenfilename()

    start_time = int(start_spinbox.get())
    end_time = int(end_spinbox.get())

    audio = AudioSegment.from_mp3(file_path)

    trimmed_audio = audio[start_time * 1000: end_time * 1000]

    trimmed_file_path = file_path.replace(".mp3", "_trimmed.mp3")
    trimmed_audio.export(trimmed_file_path, format = "mp3")

    status_label.config(text = "MP3 trimmed successfully!")

main_window.mainloop()

