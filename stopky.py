import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopky")
        self.root.geometry("400x200")
        self.root.configure(bg="black")
        
        self.running = False
        self.time_elapsed = 0
        
        # Zobrazení času nahoře
        self.label = tk.Label(root, text="00:00:00", font=("Courier", 40), fg="white", bg="black")
        self.label.pack(expand=True)

        # Vytvoření rámce pro tlačítka
        button_frame = tk.Frame(root, bg="black")
        button_frame.pack(expand=True)

        # Tlačítka ve středu
        self.start_button = tk.Button(button_frame, text="Start", command=self.start, font=("Courier", 12))
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, font=("Courier", 12))
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, font=("Courier", 12))
        self.reset_button.grid(row=0, column=2, padx=10)

    # def __init__(self, root):
    #     self.root = root
    #     self.root.title("Stopky")
    #     self.root.geometry("400x200")
    #     self.root.configure(bg="black")
        
    #     self.running = False
    #     self.time_elapsed = 0
        
    #     # Časový údaj nahoře
    #     self.label = tk.Label(root, text="00:00:00", font=("Courier", 40), fg="white", bg="black")
    #     self.label.pack(expand=True)

    #     # Rámec pro tlačítka ve spodní části, ve středu
    #     button_frame = tk.Frame(root, bg="black")
    #     button_frame.pack(side=tk.BOTTOM, pady=20)

    #     self.start_button = tk.Button(button_frame, text="Start", command=self.start, font=("Courier", 12))
    #     self.start_button.pack(side=tk.LEFT, padx=10)

    #     self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, font=("Courier", 12))
    #     self.stop_button.pack(side=tk.LEFT, padx=10)

    #     self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, font=("Courier", 12))
    #     self.reset_button.pack(side=tk.LEFT, padx=10)
    

    # def __init__(self, root):
    #     self.root = root
    #     self.root.title("Stopky")
    #     self.root.geometry("400x200")
    #     self.root.configure(bg="black")
        
    #     self.running = False
    #     self.time_elapsed = 0
        
    #     self.label = tk.Label(root, text="00:00:00", font=("Courier", 40), fg="white", bg="black")
    #     self.label.pack(expand=True)

    #     self.start_button = tk.Button(root, text="Start", command=self.start, font=("Courier", 12))
    #     self.start_button.pack(side=tk.LEFT, padx=10)

    #     self.stop_button = tk.Button(root, text="Stop", command=self.stop, font=("Courier", 12))
    #     self.stop_button.pack(side=tk.LEFT, padx=10)

    #     self.reset_button = tk.Button(root, text="Reset", command=self.reset, font=("Courier", 12))
    #     self.reset_button.pack(side=tk.LEFT, padx=10)
    

    def update_time(self):
        if self.running:
            self.time_elapsed += 1
            self.label.config(text=self.format_time())
            self.root.after(1000, self.update_time)

    def format_time(self):
        minutes, seconds = divmod(self.time_elapsed, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
