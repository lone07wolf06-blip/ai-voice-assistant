import tkinter as tk
from tkinter import scrolledtext

class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Assistant")
        self.master.geometry("600x400")

        self.command_history = scrolledtext.ScrolledText(self.master, width=70, height=10)
        self.command_history.pack(pady=10)

        self.status_label = tk.Label(self.master, text="Status: Ready", fg="green")
        self.status_label.pack(pady=5)

        self.preferences_button = tk.Button(self.master, text="Preferences", command=self.open_preferences)
        self.preferences_button.pack(pady=5)

        self.transcription_label = tk.Label(self.master, text="Real-time Transcription:")
        self.transcription_label.pack(pady=5)
        self.transcription_display = tk.Label(self.master, text="", bg="white", width=70, anchor='w')
        self.transcription_display.pack(pady=5)

    def open_preferences(self):
        # This function will eventually open the preferences window
        print('Open Preferences')

    def update_transcription(self, text):
        self.transcription_display.config(text=text)

    def add_command_to_history(self, command):
        self.command_history.insert(tk.END, command + '\n')
        self.command_history.yview(tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    root.mainloop()