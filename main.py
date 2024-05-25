import tkinter as tk
from tkinter import messagebox
import math

icon = 'C:\\Users\\P3sL\\Desktop\\math project\\math-16.ico'


def circle_calculator(root):
    global entry
    entry = 0  

    def calculate(*args):
        try:
            if entry_diameter.get():
                diameter = float(entry_diameter.get())
                radius = diameter / 2
                circumference = 2 * math.pi * radius
                area = math.pi * radius ** 2
                entry_radius.delete(0, tk.END)
                entry_circumference.delete(0, tk.END)
                entry_Area.delete(0, tk.END)
                entry_radius.insert(0, str(radius))
                entry_circumference.insert(0, str(round(circumference, 2)))
                entry_Area.insert(0, str(round(area, 2)))
            elif entry_radius.get():
                radius = float(entry_radius.get())
                diameter = 2 * radius
                circumference = 2 * math.pi * radius
                area = math.pi * radius ** 2
                entry_diameter.delete(0, tk.END)
                entry_circumference.delete(0, tk.END)
                entry_Area.delete(0, tk.END)
                entry_diameter.insert(0, str(diameter))
                entry_circumference.insert(0, str(round(circumference, 2))) 
                entry_Area.insert(0, str(round(area, 2)))
            elif entry_circumference.get():
                circumference = float(entry_circumference.get())
                radius = circumference / (2 * math.pi)
                diameter = 2 * radius
                area = math.pi * radius ** 2
                entry_radius.delete(0, tk.END)
                entry_diameter.delete(0, tk.END)
                entry_Area.delete(0, tk.END)
                entry_radius.insert(0, str(round(radius, 2)))
                entry_diameter.insert(0, str(round(diameter, 2)))
                entry_Area.insert(0, str(round(area, 2)))
            elif entry_Area.get():
                area = float(entry_Area.get())
                radius = (area / math.pi) ** 0.5
                diameter = 2 * radius
                circumference = 2 * math.pi * radius
                entry_radius.delete(0, tk.END)
                entry_diameter.delete(0, tk.END)
                entry_circumference.delete(0, tk.END)
                entry_radius.insert(0, str(round(radius, 2)))
                entry_diameter.insert(0, str(round(diameter, 2)))
                entry_circumference.insert(0, str(round(circumference, 2)))
        except ValueError:
            messagebox.showerror("خطأ", "الرجاء إدخال قيمة صحيحة")

    def show_solution():
        global entry
        diameter = float(entry_diameter.get()) if entry_diameter.get() else None
        radius = float(entry_radius.get()) if entry_radius.get() else None
        circumference = float(entry_circumference.get()) if entry_circumference.get() else None
        area = float(entry_Area.get()) if entry_Area.get() else None

        explanation = ""
        if entry == 1:
            explanation += "مدخلاتك كانت تفيد بأن القطر = {}\n".format(diameter)
            explanation += "ولحساب نصف القطر نستخدم المعادلة التالية:\n"
            explanation += "نصف القطر = القطر ÷ 2\n"
            explanation += "نصف القطر = {} ÷ 2\n".format(diameter)
            explanation += "ليصبح نصف القطر = {}\n\n".format(float(diameter) / 2)
            explanation += "ولحساب المحيط نستخدم المعادلة التالية:\n"
            explanation += "المحيط = 2 × π × نصف القطر\n"
            explanation += "المحيط = 2 × 3.14 × {}\n".format(float(diameter) / 2)
            explanation += "ليصبح المحيط = {:.2f}\n\n".format(2 * 3.14 * (float(diameter) / 2))
            explanation += "وبالنسبة لحساب المساحة، نقوم بالتالي:\n"
            explanation += "المساحة = π × نصف القطر^2\n"
            explanation += "المساحة = 3.14 × ({:.2f})^2\n".format(float(diameter) / 2)
            explanation += "ليصبح المساحة = {:.2f}\n".format(3.14 * (float(diameter) / 2) ** 2)

        if entry == 2:
            explanation += "مدخلاتك كانت تفيد بأن نصف القطر = {}\n".format(radius)
            explanation += "ولحساب القطر الكامل نستخدم المعادلة التالية:\n"
            explanation += "القطر = نصف القطر × 2\n"
            explanation += "القطر = {} × 2\n".format(radius)
            explanation += "ليصبح القطر كاملاً = {}\n\n".format(float(radius) * 2)
            explanation += "ولحساب المحيط نستخدم المعادلة التالية:\n"
            explanation += "المحيط = 2 × π × نصف القطر\n"
            explanation += "المحيط = 2 × 3.14 × {}\n".format(radius)
            explanation += "ليصبح المحيط = {:.2f}\n\n".format(2 * 3.14 * float(radius))
            explanation += "وبالنسبة لحساب المساحة، نقوم بالتالي:\n"
            explanation += "المساحة = π × نصف القطر^2\n"
            explanation += "المساحة = 3.14 × ({:.2f})^2\n".format(float(radius))
            explanation += "ليصبح المساحة = {:.2f}\n".format(3.14 * float(radius) ** 2)


        if entry == 3:
            explanation += "مدخلاتك كانت تفيد بأن المحيط = {}\n".format(circumference)
            explanation += "ولحساب نصف القطر نستخدم المعادلة التالية:\n"
            explanation += "نصف القطر = المحيط ÷ (2 × π)\n"
            explanation += "نصف القطر = {} ÷ (2 × 3.14)\n".format(circumference)
            radius = float(circumference) / (2 * 3.14)
            explanation += "ليصبح نصف القطر = {:.2f}\n".format(radius)
            diameter = 2 * radius
            explanation += "وبالتالي، نحتاج إلى حساب القطر كاملاً عبر ضرب نصف القطر في 2:\n"
            explanation += "القطر = 2 × نصف القطر\n"
            explanation += "القطر = {:.2f} × 2\n".format(radius)
            explanation += "ليصبح القطر = {:.2f}\n\n".format(diameter)
            explanation += "ثم، لحساب المساحة، نستخدم العلاقة التالية:\n"
            explanation += "المساحة = π × نصف القطر^2\n"
            explanation += "المساحة = 3.14 × ({:.2f})^2\n".format(radius)
            explanation += "ليصبح المساحة = {:.2f}\n".format(3.14 * radius ** 2)


        if entry == 4:
            explanation += "مدخلاتك كانت تفيد بأن المساحة = {}\n".format(area)
            explanation += "ولحساب نصف القطر نستخدم المعادلة التالية:\n"
            explanation += "نصف القطر = √(المساحة ÷ π)\n"
            explanation += "نصف القطر = √({} ÷ 3.14)\n".format(area)
            radius = (area / 3.14) ** 0.5
            explanation += "ليصبح نصف القطر = {:.2f}\n".format(radius)
            diameter = 2 * radius
            explanation += "ومن ثم، يمكن حساب القطر الكامل ببساطة عبر ضرب نصف القطر في 2:\n"
            explanation += "القطر = 2 × نصف القطر\n"
            explanation += "القطر = 2 × {:.2f}\n".format(radius)
            explanation += "ليصبح القطر = {:.2f}\n\n".format(diameter)
            explanation += "ثم، لحساب المحيط، نستخدم العلاقة التالية:\n"
            explanation += "المحيط = 2 × π × نصف القطر\n"
            explanation += "المحيط = 2 × 3.14 × {:.2f}\n".format(radius)
            explanation += "ليصبح المحيط = {:.2f}\n".format(2 * 3.14 * radius)
            explanation += "أخيرًا، لحساب المساحة، يمكن استخدام القطر الكامل كالتالي:\n"
            explanation += "المساحة = π × (نصف القطر)^2\n"
            explanation += "المساحة = 3.14 × ({:.2f})^2\n".format(radius)
            explanation += "ليصبح المساحة = {:.2f}\n".format(3.14 * radius ** 2)

        solution_window = tk.Toplevel(root)
        solution_window.title("شرح الحل")
        label_solution = tk.Label(solution_window, text=explanation)
        label_solution.pack()

    def clear_fields():
        entry_diameter.delete(0, tk.END)
        entry_radius.delete(0, tk.END)
        entry_circumference.delete(0, tk.END)
        entry_Area.delete(0, tk.END)

    def return_to_main():
        root.deiconify()
        circle_window.destroy()

    circle_window = tk.Toplevel(root)
    circle_window.title("حساب الأبعاد الدائرية")
    circle_window.geometry("400x350")

    label_diameter = tk.Label(circle_window, text="قطر الدائرة:")
    label_diameter.pack()
    entry_diameter = tk.Entry(circle_window)
    entry_diameter.pack()
    entry_diameter.bind("<KeyRelease>", calculate)

    label_radius = tk.Label(circle_window, text="نصف القطر:")
    label_radius.pack()
    entry_radius = tk.Entry(circle_window)
    entry_radius.pack()
    entry_radius.bind("<KeyRelease>", calculate)

    label_circumference = tk.Label(circle_window, text="محيط الدائرة:")
    label_circumference.pack()
    entry_circumference = tk.Entry(circle_window)
    entry_circumference.pack()
    entry_circumference.bind("<KeyRelease>", calculate)

    label_Area = tk.Label(circle_window, text="المساحة:")
    label_Area.pack()
    entry_Area = tk.Entry(circle_window)
    entry_Area.pack()
    entry_Area.bind("<KeyRelease>", calculate)

    button_clear = tk.Button(circle_window, text="تصفير الحقول", command=clear_fields)
    button_clear.pack()


    return_button = tk.Button(circle_window, text="العودة للواجهة الرئيسية", command=return_to_main, bg="blue")
    return_button.pack()

    circle_window.iconbitmap(icon)
    circle_window.mainloop()
    
def central_angle_calculator(root):
    def show_angle_input():
        try:
            num_angles = int(num_angles_entry.get())
            num_angles_entry.config(state="disabled")
            next_button.config(state="disabled")

            angle_inputs = []
            for i in range(num_angles):
                angle_label = tk.Label(angle_window, text=f"ادخل قياس الزاوية {i+1} المعروفة:")
                angle_label.pack()
                angle_entry = tk.Entry(angle_window)
                angle_entry.pack()
                angle_inputs.append(angle_entry)

            def calculate_central_angle():
                try:
                    angles_sum = sum(float(angle_entry.get()) for angle_entry in angle_inputs)
                    central_angle = 360 - angles_sum
                    messagebox.showinfo("النتيجة", f"قياس الزاوية المركزية يساوي = {central_angle}")
                except ValueError:
                    messagebox.showerror("خطأ", "الرجاء ادخال قيم صحيحة لقياسات الزوايا")

            calculate_button = tk.Button(angle_window, text="احسب", command=calculate_central_angle)
            calculate_button.pack()

        except ValueError:
            messagebox.showerror("خطأ", "الرجاء ادخال قيمة صحيحة لعدد الزوايا")

    def return_to_main():
        root.deiconify()
        angle_window.destroy()

    angle_window = tk.Toplevel(root)
    angle_window.title("حاسبة الزوايا")
    angle_window.geometry("300x400")
    angle_window.iconbitmap(icon)

    num_angles_label = tk.Label(angle_window, text="كم عدد قياسات الزوايا المعروفة؟")
    num_angles_label.pack()

    num_angles_entry = tk.Entry(angle_window)
    num_angles_entry.pack()

    next_button = tk.Button(angle_window, text="التالي", command=show_angle_input)
    next_button.pack()

    return_button = tk.Button(angle_window, text="العودة للواجهة الرئيسية", command=return_to_main , bg='blue')
    return_button.pack()

def arc_length(root):
    def calculate_arc_length():
        try:
            x = float(entry_x.get())
            r = float(entry_r.get())
        
            arc_length = (x / 360) * (2 * r * 3.14)
            
            result_label.config(text=f"Arc Length: {arc_length:.2f}")
        except ValueError:
            messagebox.showerror("خطأ", "الرجاء إدخال قيم صحيحة لـ x و r")

    def show_solution():
        try:
            x = float(entry_x.get())
            r = float(entry_r.get())
            
            equation = f"المعادلة: {x} / 360 * (2 * {r} * 3.14)"
            explanation = f"طريقة الحل:\n{x} / 360 * (2 * {r} * 3.14)\n\n"
            
            result = (x / 360) * (2 * r * 3.14)
            solution = f"الناتج: {result:.2f}"
            
            messagebox.showinfo("شرح الحل", explanation + solution)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def return_to_main():
        root.deiconify()
        arc_window.destroy()

    arc_window = tk.Toplevel(root)
    arc_window.title("إيجاد طول القوس")
    arc_window.iconbitmap(icon)

    label_x = tk.Label(arc_window, text="ادخل قيمة x:")
    label_x.grid(row=0, column=0, padx=10, pady=5)

    entry_x = tk.Entry(arc_window)
    entry_x.grid(row=0, column=1, padx=10, pady=5)

    label_r = tk.Label(arc_window, text="ادخل قيمة r:")
    label_r.grid(row=1, column=0, padx=10, pady=5)

    entry_r = tk.Entry(arc_window)
    entry_r.grid(row=1, column=1, padx=10, pady=5)

    calculate_button = tk.Button(arc_window, text="احسب", command=calculate_arc_length)
    calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    result_label = tk.Label(arc_window, text="")
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    solution_button = tk.Button(arc_window, text="شرح الحل", command=show_solution)
    solution_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    return_button = tk.Button(arc_window, text="العودة للواجهة الرئيسية", command=return_to_main , bg="blue")
    return_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

def surrounding_corner(root):
    def update_from_angle(event):
        try:
            angle = float(entry_angle.get())
            circumference = angle / 2
            entry_circumference.delete(0, tk.END)  
            entry_circumference.insert(0, str(circumference))  
        except ValueError:
            entry_circumference.delete(0, tk.END)  

    def update_from_circumference(event):
        try:
            circumference = float(entry_circumference.get())
            angle = circumference * 2
            entry_angle.delete(0, tk.END)  
            entry_angle.insert(0, str(angle))  
        except ValueError:
            entry_angle.delete(0, tk.END)  

    def show_solution():
        explanation = "لحساب المحيطيه، نقوم بقسمة قيمة القوس على 2، ولحساب القوس نقوم بضرب قيمة المحيطيه في 2."
        messagebox.showinfo("شرح الحل", explanation)

    root.withdraw()
    angle_window = tk.Toplevel(root)
    angle_window.title("حساب القوس والمحيطيه")

    label_angle = tk.Label(angle_window, text="القوس:")
    label_angle.pack()
    entry_angle = tk.Entry(angle_window)
    entry_angle.pack()
    entry_angle.bind("<KeyRelease>", update_from_angle)  

    label_circumference = tk.Label(angle_window, text="المحيطيه:")
    label_circumference.pack()
    entry_circumference = tk.Entry(angle_window)
    entry_circumference.pack()
    entry_circumference.bind("<KeyRelease>", update_from_circumference)  

    button_solution = tk.Button(angle_window, text="شرح الحل", command=show_solution)
    button_solution.pack()

    def return_to_main():
        root.deiconify()
        angle_window.destroy()

    angle_window.geometry("200x200")
    return_button = tk.Button(angle_window, text="العودة للواجهة الرئيسية", command=return_to_main, bg="blue")
    return_button.pack()

    angle_window.iconbitmap(icon)
    angle_window.mainloop()



def open_circle_calculator():
    root.withdraw()
    circle_calculator(root)

def open_central_angle_calculator():
    root.withdraw()
    central_angle_calculator(root)

def open_arc_length():
    root.withdraw()
    arc_length(root)

def open_surroundingـcorner():
    root.withdraw()
    surrounding_corner(root)

root = tk.Tk()
root.title("مقدمة")
root.geometry("1200x300")
root.iconbitmap(icon)

text_frame = tk.Frame(root)
text_frame.pack(pady=20)

project_info_label = tk.Label(
    text_frame,
    text="تم العمل على هذا المشروع من قبل الطالب : صالح بن ابراهيم المحيميد\nوتم الاشراف عليه من قبل : أ. وائل الشربيني\nويقدم هذا العمل لمدارس الرياض ومنسوبيها",
    font=("Arial", 30),
    justify="center"
)
project_info_label.pack()

# تصميم الأزرار
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

open_calculator_button = tk.Button(button_frame, text="حساب الدائرة", command=open_circle_calculator, width=20, height=2, font=("Arial", 14))
open_calculator_button.grid(row=0, column=0, padx=10)

open_angle_calculator_button = tk.Button(button_frame, text="إيجاد قياس الزاويه المركزيه المجهوله", command=open_central_angle_calculator, width=25, height=2, font=("Arial", 14))
open_angle_calculator_button.grid(row=0, column=1, padx=10)

open_arc_length_button = tk.Button(button_frame, text="إيجاد طول القوس", command=open_arc_length, width=20, height=2, font=("Arial", 14))
open_arc_length_button.grid(row=0, column=2, padx=10)

open_arc_length_button = tk.Button(button_frame, text="إيجاد طول القوس", command=open_arc_length, width=20, height=2, font=("Arial", 14))
open_arc_length_button.grid(row=0, column=2, padx=10)

surroundingـcorner_button = tk.Button(button_frame, text="العلاقه يين الزاويه المحيطيه والقوس المقابل" , command=open_surroundingـcorner, width=25, height=2, font=("Arial", 14))
surroundingـcorner_button.grid(row=0, column=3, padx=10)


root.mainloop()
