import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("מגדלי טוויטר")


# חישוב היקף מלבן
def rectangle_perimeter(height, width):
    return (height + width) * 2


# חישוב שטח מלבן
def rectangle_area(height, width):
    return height * width


# חישוב היקף המשולש
def triangle_perimeter(height, width):
    a = ((width / 2) ** 2 + height ** 2) ** 0.5
    return 2 * a + width


# חישוב שטח המשולש
def triangle_area(height, width):
    return (height * width) / 2


def rectangle_selected(height, width):
    if height == width or abs(height - width) > 5:
        return f"שטח המלבן הוא: {rectangle_area(height, width)}"

    return f"היקף המלבן הוא: {rectangle_perimeter(height, width)} "


def print_tringle(height, width):
    if width % 2 == 0 or width > height * 2:
        return "The triangle cannot be printed"
    middle = height - 2
    if height > 2:
        if width > 3:
            groups = middle // int((width - 3) / 2)
            group1 = middle // int((width - 3) / 2) + middle % int((width - 3) / 2)
            line = "***"
        else:
            # group1 = 1
            # groups = 0
            line = "*"
            result = ""
            space = " " * int((width - 1) / 2)
            # count = 1
            result += space + "*" + "\n"

            for k in range(height - 2):
                result += space + line + "\n"
            line += "**"
            space = space[1:]
            result += space + line + "\n"
            return result

    else:
        groups = 0
        group1 = 0
        line = "*"
    result = ""
    space = " " * int((width - 1) / 2)
    count = 1
    result += space + "*" + "\n"
    space = space[1:]
    for k in range(group1):
        result += space + line + "\n"
    space = space[1:]
    line = line + "**"
    for i in range(height - 2 - group1):
        result += space + line + "\n"
        if count == groups:
            space = space[1:]
            line = line + "**"
            count = 0
        count += 1
    result += space + line + "\n"
    return result


print(print_tringle(40, 20))


def button1_click():
    height1 = int(height.get(1.0, 1.5))
    width1 = int(width.get(1.0, 1.5))
    output_value = rectangle_selected(height1, width1)
    result.delete(1.0, END)
    result.insert(tk.END, str(output_value))


def button_perimeter_click(height, width, button_perimeter, button_print):
    output_value = triangle_perimeter(height, width)
    result.delete(1.0, END)
    result.insert(tk.END, str(output_value))
    button_print.destroy()
    button_perimeter.destroy()


def button_print_click(height, width, button_perimeter, button_print):
    output_value = print_tringle(height, width)
    result.delete(1.0, END)
    result.insert(tk.END, str(output_value))
    button_print.destroy()
    button_perimeter.destroy()


def button2_click():
    height1 = int(height.get(1.0, 1.5))
    width1 = int(width.get(1.0, 1.5))

    button_perimeter = tk.Button(root, text="היקף המשולש",
                                 command=lambda: button_perimeter_click(height1, width1, button_perimeter,
                                                                        button_print))
    button_perimeter.pack()

    button_print = tk.Button(root, text="הדפסת המשולש",
                             command=lambda: button_print_click(height1, width1, button_perimeter, button_print))
    button_print.pack()


label_height = tk.Label(root, text="הכנס גובה")
label_height.pack()
height = tk.Text(root, height=1, width=6)
height.pack()
# height.insert(tk.END, "Hello, world!")
label_width = tk.Label(root, text="הכנס רוחב")
label_width.pack()
width = tk.Text(root, height=1, width=6)
width.pack()
label = tk.Label(root, text="בחר סוג מגדל")
label.pack()
button1 = tk.Button(root, text="אפשרות 1 (מלבן)",
                    command=lambda: button1_click())
button1.pack()

button2 = tk.Button(root, text="אפשרות 2 (משולש)",
                    command=lambda: button2_click())
button2.pack()
button3 = tk.Button(root, text="אפשרות 3 (יציאה)", command=root.quit)
button3.pack()
label_result = tk.Label(root, text="תוצאה")
label_result.pack()
result = tk.Text(root, height=20, width=100)
result.pack()
root.mainloop()
