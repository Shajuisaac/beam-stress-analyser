import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def analyze():
    try:
        L = float(length_entry.get())
        F = float(force_entry.get())
        x = np.linspace(0, L, 1000)
        V = np.where(x < L/2, F/2, -F/2)
        M = np.where(x < L/2, F * x / 2, F * (L - x) / 2)

        fig, axs = plt.subplots(2, 1, figsize=(6, 5))
        axs[0].plot(x, V, label="Shear Force", color='blue')
        axs[1].plot(x, M, label="Bending Moment", color='red')
        axs[0].set_title('Shear Force Diagram')
        axs[1].set_title('Bending Moment Diagram')
        axs[0].set_ylabel('Force (N)')
        axs[1].set_ylabel('Moment (Nm)')
        axs[1].set_xlabel('Length (m)')
        for ax in axs:
            ax.grid(True)

        # Clear old plot
        for widget in plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except ValueError:
        print("Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("Beam Stress Analyzer")
root.geometry("650x700")

tk.Label(root, text="Beam Length (m):").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Label(root, text="Point Load (N):").pack()
force_entry = tk.Entry(root)
force_entry.pack()

tk.Button(root, text="Analyze", command=analyze).pack(pady=10)

plot_frame = tk.Frame(root)
plot_frame.pack()

root.mainloop()
