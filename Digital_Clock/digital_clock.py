# ==========================
# DIGITAL CLOCK USING PYTHON
# ==========================

# Import required modules
import tkinter as tk       # For GUI window
import time                # For getting current time

# --------------------------
# Function to update time
# --------------------------
def update_time():
    """
    This function gets the current system time
    and updates the label every 1000 milliseconds (1 second)
    """

    # Fetch current time in HH:MM:SS AM/PM format
    current_time = time.strftime("%I:%M:%S %p")

    # Fetch current date
    current_date = time.strftime("%A, %d %B %Y")

    # Update label text
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Call this function again after 1 second
    time_label.after(1000, update_time)

# --------------------------
# Create main application window
# --------------------------
root = tk.Tk()

# Title of window
root.title("Digital Clock")

# Set window size
root.geometry("500x200")

# Disable resizing
root.resizable(False, False)

# Set background color
root.configure(bg="black")

# --------------------------
# Create Time Label
# --------------------------
time_label = tk.Label(
    root,
    font=("Digital-7", 60, "bold"),   # Digital style font
    background="black",
    foreground="cyan"
)

time_label.pack(pady=20)

# --------------------------
# Create Date Label
# --------------------------
date_label = tk.Label(
    root,
    font=("Arial", 14),
    background="black",
    foreground="white"
)
date_label.pack()

# --------------------------
# Start clock update
# --------------------------
update_time()

# --------------------------
# Run the application
# --------------------------
root.mainloop()
# End of digital_clock.py