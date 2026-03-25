import tkinter as tk
from tkinter import messagebox
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Currency Converter")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50") # Dark professional theme

        # No API Key required for this specific endpoint
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"

        self.setup_ui()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="CURRENCY CONVERTER", font=("Arial", 18, "bold"), 
                 bg="#2c3e50", fg="#ecf0f1", pady=30).pack()

        # Input Container
        content_frame = tk.Frame(self.root, bg="#2c3e50")
        content_frame.pack(pady=10, padx=30, fill="both")

        # Amount Input
        tk.Label(content_frame, text="Amount:", font=("Arial", 10, "bold"), 
                 bg="#2c3e50", fg="#bdc3c7").pack(anchor="w")
        self.amount_entry = tk.Entry(content_frame, font=("Arial", 14), bd=0, highlightthickness=2)
        self.amount_entry.config(highlightbackground="#34495e", highlightcolor="#3498db")
        self.amount_entry.pack(fill="x", pady=(5, 15))
        self.amount_entry.insert(0, "100")

        # From Currency
        tk.Label(content_frame, text="From (e.g., USD):", font=("Arial", 10, "bold"), 
                 bg="#2c3e50", fg="#bdc3c7").pack(anchor="w")
        self.from_entry = tk.Entry(content_frame, font=("Arial", 14), bd=0, highlightthickness=2)
        self.from_entry.config(highlightbackground="#34495e", highlightcolor="#3498db")
        self.from_entry.pack(fill="x", pady=(5, 10))
        self.from_entry.insert(0, "USD")

        # Swap Button
        swap_btn = tk.Button(content_frame, text="⇅ SWAP", font=("Arial", 9, "bold"), 
                            bg="#34495e", fg="#ecf0f1", command=self.swap_currencies, 
                            relief="flat", cursor="hand2")
        swap_btn.pack(pady=5)

        # To Currency
        tk.Label(content_frame, text="To (e.g., INR):", font=("Arial", 10, "bold"), 
                 bg="#2c3e50", fg="#bdc3c7").pack(anchor="w")
        self.to_entry = tk.Entry(content_frame, font=("Arial", 14), bd=0, highlightthickness=2)
        self.to_entry.config(highlightbackground="#34495e", highlightcolor="#3498db")
        self.to_entry.pack(fill="x", pady=(5, 20))
        self.to_entry.insert(0, "INR")

        # Convert Button
        convert_btn = tk.Button(self.root, text="CONVERT", font=("Arial", 12, "bold"), 
                               bg="#3498db", fg="white", command=self.convert, 
                               padx=40, pady=10, relief="flat", cursor="hand2")
        convert_btn.pack(pady=10)

        # Result Area
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"), 
                                    bg="#2c3e50", fg="#2ecc71")
        self.result_label.pack(pady=20)

    def swap_currencies(self):
        from_val = self.from_entry.get()
        to_val = self.to_entry.get()
        self.from_entry.delete(0, tk.END)
        self.from_entry.insert(0, to_val)
        self.to_entry.delete(0, tk.END)
        self.to_entry.insert(0, from_val)

    def convert(self):
        try:
            amt = float(self.amount_entry.get())
            from_curr = self.from_entry.get().upper()
            to_curr = self.to_entry.get().upper()

            # Using public API (No key needed)
            response = requests.get(f"{self.api_url}{from_curr}")
            data = response.json()

            if "rates" in data:
                rate = data["rates"][to_curr]
                total = amt * rate
                self.result_label.config(text=f"{amt} {from_curr} = {total:.2f} {to_curr}")
            else:
                messagebox.showerror("Error", "Invalid Currency Code.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
        except Exception:
            messagebox.showerror("Error", "Network connection failed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()