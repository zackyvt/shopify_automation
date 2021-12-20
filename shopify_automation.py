import tkinter as tk
from tkinter import ttk, filedialog

import main

def import_shopify_apps(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

file_path = ""

def open_file():
    global file_path
    file_path = filedialog.askopenfilename()
    shopify_apps_file_label.config(text="Shopify Apps URLs File: \n" + file_path.split("/")[-1])

def run():
    global file_path
    shopify_apps = import_shopify_apps(file_path)
    cycles = int(cycles_entry.get())
    api_key = captcha_key_entry.get()
    main.main(cycles, api_key, shopify_apps)

window = tk.Tk()

window.title("Shopify Automation")
window.geometry("380x185")
window.resizable(False, False)

captcha_key_label = ttk.Label(window, text="2Captcha API Key:")
captcha_key_entry = ttk.Entry(window)

cycles_label = ttk.Label(window, text="Number of Cycles:")
cycles_entry = ttk.Entry(window)

shopify_apps_file_label = ttk.Label(window, text="Path to Shopify Apps File: \n-")
shopify_apps_file_button = ttk.Button(window, text="Choose File", command=open_file)

start_button = ttk.Button(window, text="Run Automation", command=run)

captcha_key_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
captcha_key_entry.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")
cycles_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
cycles_entry.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")
shopify_apps_file_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
shopify_apps_file_button.grid(row=2, column=1, padx=10, pady=10, sticky="NSE")
start_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

window.mainloop()