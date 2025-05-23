import tkinter as tk
from tkinter import messagebox
import os,csv

# Function to handle form submission
def submit_form():
    data = {
        "نام و نام خانوادگی": name_var.get(),
        "سن": age_var.get(),
        "شماره تماس": phone_var.get(),
        "جنسیت": gender_var.get(),
        "عنوان": title_var.get(),
        "مدرک": degree_var.get()
    }

    if not data["نام و نام خانوادگی"] or not data["سن"].isdigit():
        messagebox.showerror("خطا", "لطفاً اطلاعات را به‌درستی وارد کنید.")
        return

    messagebox.showinfo("ثبت موفق", f"کاربر با نام {data['نام و نام خانوادگی']} ثبت شد.")
    print(data)
    # Save to CSV file
    file_name = "data.csv"
    file_exists = os.path.isfile(file_name)

    with open(file_name, mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["نام و نام خانوادگی", "سن", "شماره تماس", "جنسیت", "عنوان", "مدرک"])
        writer.writerow([
            data["نام و نام خانوادگی"],
            data["سن"],
            data["شماره تماس"],
            data["جنسیت"],
            data["عنوان"],
            data["مدرک"]
        ])
        reset_form()


# Function to reset form fields
def reset_form():
    name_var.set("")
    age_var.set("")
    phone_var.set("")
    gender_var.set("مرد")
    title_var.set("")
    degree_var.set("دیپلم")

# Create main window
root = tk.Tk()
root.title("فرم ثبت‌نام")
root.geometry("750x650")  # Larger size for better layout
root.configure(bg="#f0f4f8")

# Variables
name_var = tk.StringVar()
age_var = tk.StringVar()
phone_var = tk.StringVar()
gender_var = tk.StringVar(value="مرد")
title_var = tk.StringVar()
degree_var = tk.StringVar(value="دیپلم")

# Degree options
degree_options = ["دیپلم", "کارشناسی", "کارشناسی ارشد", "دکترا"]

# Frame for form layout
form_frame = tk.Frame(root, bg="#f0f4f8")
form_frame.pack(pady=40)

# Helper: create label and entry from right to left
def add_label_entry(row, label_text, var):
    entry = tk.Entry(form_frame, textvariable=var, font=("B Nazanin", 13), justify="right", width=40)
    label = tk.Label(form_frame, text=label_text, bg="#f0f4f8", anchor="e", font=("B Nazanin", 14, "bold"))
    entry.grid(row=row, column=0, sticky="e", padx=(0, 10), pady=8)
    label.grid(row=row, column=1, sticky="w", padx=(10, 0), pady=8)

# Add fields
add_label_entry(0, ": نام و نام خانوادگی", name_var)
add_label_entry(1, ": سن", age_var)
add_label_entry(2, ": شماره", phone_var)
add_label_entry(3, ": عنوان", title_var)

# Gender row
gender_label = tk.Label(form_frame, text=": جنسیت", bg="#f0f4f8", font=("B Nazanin", 14, "bold"))
gender_label.grid(row=4, column=1, sticky="w", padx=(10, 0), pady=8)

gender_frame = tk.Frame(form_frame, bg="#f0f4f8")
gender_frame.grid(row=4, column=0, sticky="e", padx=(0, 10))

tk.Radiobutton(gender_frame, text="مرد", variable=gender_var, value="مرد",
               bg="#f0f4f8", font=("B Nazanin", 12)).pack(side="right", padx=5)
tk.Radiobutton(gender_frame, text="زن", variable=gender_var, value="زن",
               bg="#f0f4f8", font=("B Nazanin", 12)).pack(side="right", padx=5)

# Degree row
degree_label = tk.Label(form_frame, text=": مدرک تحصیلی", bg="#f0f4f8", font=("B Nazanin", 14, "bold"))
degree_label.grid(row=5, column=1, sticky="w", padx=(10, 0), pady=8)

degree_menu = tk.OptionMenu(form_frame, degree_var, *degree_options)
degree_menu.config(font=("B Nazanin", 13), width=37, bg="white", fg="#333")
degree_menu.grid(row=5, column=0, sticky="e", padx=(0, 10))

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=30)

submit_btn = tk.Button(btn_frame, text="ثبت‌نام", command=submit_form,
                       width=20, bg="#2ecc71", fg="white", font=("B Nazanin", 13, "bold"))
submit_btn.pack(side="right", padx=15)

reset_btn = tk.Button(btn_frame, text="پاک‌کردن", command=reset_form,
                      width=20, bg="#e74c3c", fg="white", font=("B Nazanin", 13, "bold"))
reset_btn.pack(side="right", padx=15)

# Run app
root.mainloop()
