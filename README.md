# Math Project

## Overview
This project is developed by Saleh bin Ibrahim Almuhaimid and supervised by Mr. Wael El-Sherbiny. It is presented to Riyadh Schools and its affiliates. The project provides a user-friendly graphical interface using Python and the Tkinter library to perform various mathematical calculations related to circles.

## Features
- **Circle Calculator**: Computes the radius, diameter, circumference, and area of a circle based on any one of these input values.
- **Central Angle Calculator**: Determines the measure of an unknown central angle given the measures of other known angles.
- **Arc Length Calculator**: Calculates the length of an arc based on the angle and radius.
- **Relationship Between Central and Inscribed Angles**: Explains the relationship between an inscribed angle and its corresponding arc.

## Installation
1. Ensure you have Python installed on your machine. You can download it from [Python.org](https://www.python.org/downloads/).
2. Install Tkinter if it's not already installed. Tkinter usually comes pre-installed with Python. If needed, you can install it using:
   ```sh
   sudo apt-get install python3-tk
   ```
3. Download or clone the project repository.
   ```sh
   git clone <repository_url>
   ```
4. Place the icon file (`math-16.ico`) in the specified path or adjust the `icon` variable in the code to point to the correct location.

## Usage
1. Navigate to the project directory.
2. Run the main Python script:
   ```sh
   python main.py
   ```
3. The main window will appear with four options:
   - **Circle Calculator**: Opens a window to calculate circle dimensions.
   - **Central Angle Calculator**: Opens a window to calculate the unknown central angle.
   - **Arc Length Calculator**: Opens a window to calculate the arc length.
   - **Relationship Between Central and Inscribed Angles**: Opens a window explaining the relationship between these angles.

## File Structure
- `main.py`: The main script that initializes the Tkinter interface and provides navigation to different calculators.
- `math-16.ico`: The icon file used for the application windows.

## Code Explanation
### Main Window
The main window provides an introduction and four buttons to access different calculators:
```python
root = tk.Tk()
root.title("مقدمة")
root.geometry("1200x300")
root.iconbitmap(icon)

project_info_label = tk.Label(
    text_frame,
    text="تم العمل على هذا المشروع من قبل الطالب : صالح بن ابراهيم المحيميد\nوتم الاشراف عليه من قبل : أ. وائل الشربيني\nويقدم هذا العمل لمدارس الرياض ومنسوبيها",
    font=("Arial", 30),
    justify="center"
)
project_info_label.pack()
```
Each button is linked to a function that opens the corresponding calculator window.

### Circle Calculator
Calculates circle dimensions based on input:
```python
def calculate(*args):
    try:
        # Perform calculations based on provided input
        ...
    except ValueError:
        messagebox.showerror("خطأ", "الرجاء إدخال قيمة صحيحة")
```

### Central Angle Calculator
Determines the central angle given other angle measures:
```python
def show_angle_input():
    try:
        num_angles = int(num_angles_entry.get())
        ...
        def calculate_central_angle():
            try:
                angles_sum = sum(float(angle_entry.get()) for angle_entry in angle_inputs)
                central_angle = 360 - angles_sum
                ...
```

### Arc Length Calculator
Calculates the length of an arc:
```python
def calculate_arc_length():
    try:
        x = float(entry_x.get())
        r = float(entry_r.get())
        arc_length = (x / 360) * (2 * r * 3.14)
        result_label.config(text=f"Arc Length: {arc_length:.2f}")
    except ValueError:
        messagebox.showerror("خطأ", "الرجاء إدخال قيم صحيحة لـ x و r")
```

### Relationship Between Central and Inscribed Angles
Explains the relationship between an inscribed angle and its corresponding arc:
```python
def update_from_angle(event):
    try:
        angle = float(entry_angle.get())
        circumference = angle / 2
        entry_circumference.delete(0, tk.END)
        entry_circumference.insert(0, str(circumference))
    except ValueError:
        entry_circumference.delete(0, tk.END)
```

## License
This project is for educational purposes and is presented to Riyadh Schools and its affiliates.

## Acknowledgments
- Saleh bin Ibrahim Almuhaimid, Developer
- Mr. Wael El-Sherbiny, Supervisor

Feel free to contribute to the project by forking the repository and submitting pull requests.
