#  Beam Stress Analyzer

Hey there! 
This is a simple Python GUI tool I built to help visualize **Shear Force** and **Bending Moment** diagrams for a simply supported beam with a central point load.

If you're a mechanical engineering student like me — or just curious about structural analysis — this lightweight tool might come in handy.

---

## What It Does

You enter:
- The **length of the beam** (in meters)
- The **magnitude of the point load** (in Newtons)

Then click **Analyze**, and boom 💥 — you'll see the corresponding **Shear Force Diagram (SFD)** and **Bending Moment Diagram (BMD)**, plotted right inside the app using Matplotlib.

No external CAD or simulation software needed.

---

## Tech Behind It

- **Python 3**
- **Tkinter** for the GUI
- **NumPy** for calculations
- **Matplotlib** for plotting the graphs

I kept things minimal and easy to run on any system.

---

## ▶How to Use

1. Clone or download the repo  
2. Install the required libraries:
   ```bash
   pip install numpy matplotlib
