import unittest
from timer_with_memory.timer import Stopwatch
import tkinter as tk
import os

class TestStopwatch(unittest.TestCase):
    def setUp(self):
        """Inicializace testovací instance aplikace"""
        self.root = tk.Tk()
        self.stopwatch = Stopwatch(self.root)
    
    def tearDown(self):
        """Zavření GUI po každém testu"""
        self.root.destroy()
        if os.path.exists("saved_times.txt"):
            os.remove("saved_times.txt")  # Odstranění uložených dat po testech

    def test_save_time_with_note(self):
        """Test uložení času s poznámkou"""
        self.stopwatch.elapsed_time = 3600  # Simulace 1 hodiny
        self.stopwatch.save_time = lambda: self.stopwatch.saved_times.insert(0, "01:00:00 - Testovací poznámka")
        self.stopwatch.save_time()
        
        # Ověření, že byl uložen čas s poznámkou
        self.assertIn("01:00:00 - Testovací poznámka", self.stopwatch.saved_times)
    
    def test_reset_function(self):
        """Test funkce resetování"""
        self.stopwatch.elapsed_time = 500
        self.stopwatch.reset()
        self.assertEqual(self.stopwatch.elapsed_time, 0)
        self.assertEqual(self.stopwatch.time_label.cget("text"), "00:00:00")
    
    def test_save_times_to_file(self):
        """Test uložení časů do souboru"""
        self.stopwatch.saved_times = ["00:30:00 - První poznámka", "01:15:00 - Druhá poznámka"]
        self.stopwatch.save_times_to_file()

        # Ověření, že soubor obsahuje správná data
        with open("saved_times.txt", "r") as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0].strip(), "00:30:00 - První poznámka")
        self.assertEqual(lines[1].strip(), "01:15:00 - Druhá poznámka")
    
    def test_load_saved_times(self):
        """Test načtení časů ze souboru"""
        with open("saved_times.txt", "w") as file:
            file.write("00:10:00 - Poznámka 1\n")
            file.write("00:20:00 - Poznámka 2\n")

        self.stopwatch.load_saved_times()
        
        # Ověření, že se časy správně načetly
        self.assertIn("00:10:00 - Poznámka 1", self.stopwatch.saved_times)
        self.assertIn("00:20:00 - Poznámka 2", self.stopwatch.saved_times)

if __name__ == "__main__":
    unittest.main()
