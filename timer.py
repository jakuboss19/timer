import tkinter as tk
import time
import os

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopky")

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = tk.Label(master, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)  # Přidané tlačítko Reset
        self.reset_button.pack()

        self.save_button = tk.Button(master, text="Uložit čas", command=self.save_time)
        self.save_button.pack()

        # Vytvoření rámu a canvasu s posuvníkem
        self.saved_times_frame = tk.Frame(master)
        self.saved_times_frame.pack(expand=True, fill='both', padx=10, pady=10)

        self.canvas = tk.Canvas(self.saved_times_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.saved_times_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.saved_times = []
        self.saved_time_labels = []
        self.load_saved_times()

    def update_time(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=self.format_time(self.elapsed_time))
            self.master.after(100, self.update_time)

    def start(self):
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            self.update_time()

    def stop(self):
        self.is_running = False

    def reset(self):
        """Vynuluje časovač a zobrazí 00:00:00."""
        self.is_running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

    def save_time(self):
        if self.elapsed_time > 0:
            formatted_time = self.format_time(self.elapsed_time)
            self.saved_times.insert(0, formatted_time)  
            self.update_saved_times_display()
            self.save_times_to_file()

    def delete_time(self, index):
        """Smaže čas z uložených časů podle indexu."""
        del self.saved_times[index]
        self.update_saved_times_display()
        self.save_times_to_file()

    def update_saved_times_display(self):
        # Vyčistí aktuální labely
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        # Vytvoří labely a tlačítka pro uložené časy
        for index, saved_time in enumerate(self.saved_times):
            time_frame = tk.Frame(self.inner_frame)
            time_frame.pack(fill="x", pady=2)

            label = tk.Label(time_frame, text=saved_time, font=("Helvetica", 12), bd=1, relief="solid")
            label.pack(side="left", fill="x", expand=True)

            delete_button = tk.Button(time_frame, text="Smazat", command=lambda idx=index: self.delete_time(idx))
            delete_button.pack(side="right")

        # Aktualizace oblasti canvasu
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def save_times_to_file(self):
        with open("saved_times.txt", "w") as f:
            for time in self.saved_times:
                f.write(time + "\n")

    def load_saved_times(self):
        if os.path.exists("saved_times.txt"):
            with open("saved_times.txt", "r") as f:
                self.saved_times = [line.strip() for line in f.readlines()]
                self.update_saved_times_display()

    def format_time(self, elapsed):
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()

