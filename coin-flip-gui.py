# 🪙 Coin Flip Simulator (GUI Version)
# Built using Tkinter — Designed to be simple, elegant, and fun!
# Created by Prince 💙
import tkinter as tk
from PIL import Image, ImageTk
import random
import time

def flip_coin():
    flip_button.config(state="disabled")  # Disable button while flipping
    result_label.config(text="Flipping... 🌀")
    
    # Animation loop
    for _ in range(10):
        temp_image = random.choice([heads_img, tails_img])
        coin_label.config(image=temp_image)
        window.update()
        time.sleep(0.10)# Short delay for animation effect

    # Final result
    result = random.choice(["Heads", "Tails"])
    result_img = heads_img if result == "Heads" else tails_img
    coin_label.config(image=result_img)
    result_label.config(text=f"It's {result}! 🎉")
    flip_button.config(state="normal")

# 🪙 Set up the GUI window
window = tk.Tk()
window.title("🪙 Prince's Coin Flip Simulator")
window.config(bg="#121212")
window.geometry("400x450")

# Load images
heads_img = ImageTk.PhotoImage(Image.open("heads.png").resize((200, 200)))
tails_img = ImageTk.PhotoImage(Image.open("tails.png").resize((200, 200)))

# Heading
tk.Label(window, text="Flip the Coin!", font=("Segoe UI", 20), bg="#121212", fg="white").pack(pady=10)

# Coin image label
coin_label = tk.Label(window, image=heads_img, bg="#121212")
coin_label.pack(pady=20)

# Result label
result_label = tk.Label(window, text="", font=("Segoe UI", 16), bg="#121212", fg="#00FFCC")
result_label.pack(pady=10)

# Flip button
flip_button = tk.Button(window, text="🎲 Flip Coin", font=("Segoe UI", 14), bg="#00FFCC", fg="black", padx=20, pady=10, command=flip_coin)
flip_button.pack(pady=20)

window.mainloop()

# --- End of code ---
# Enjoy flipping coins!💖
# Make sure to have 'heads.png' and 'tails.png' in the same directory as this script.
# If you like this project, consider sharing it with friends! 😊