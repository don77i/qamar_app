import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("تطبيق قمر") 
root.geometry("520x450")
root.resizable(False, False)

# ----------------------------------------
# دالة لتدرج الألوان في الخلفية
def gradient_bg(frame, color1, color2):
    canvas = tk.Canvas(frame, width=520, height=450, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)
    r_ratio = (r2 - r1) / 450
    g_ratio = (g2 - g1) / 450
    b_ratio = (b2 - b1) / 450
    for i in range(450):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f"#{nr//256:02x}{ng//256:02x}{nb//256:02x}"
        canvas.create_line(0, i, 520, i, fill=color)
    return canvas

# ----------------------------------------
# دالة تأثير الظهور التدريجي
def fade_in(widget, alpha=0):
    widget.update()
    if alpha < 1:
        alpha += 0.05
        widget.attributes("-alpha", alpha)
        widget.after(50, fade_in, widget, alpha)

root.attributes("-alpha", 0)
fade_in(root)

# ----------------------------------------
# الصفحة 1 - الترحيب
def start_app():
    welcome_frame.pack_forget()
    fade_transition(question2_frame)  # الانتقال مباشرة إلى الصفحة 3 (السؤال الثاني)

welcome_frame = tk.Frame(root)
canvas1 = gradient_bg(welcome_frame, "#ffccff", "#ffe6f2")

label_welcome = tk.Label(
    welcome_frame,
    text="ها قمر 💖", 
    font=("Tajawal", 26, "bold"),
    bg="#ffe6f2",
    fg="#cc0066"
)
label_welcome.place(relx=0.5, rely=0.3, anchor="center")

start_button = tk.Button(
    welcome_frame,
    text="دوسي", 
    command=start_app,
    font=("Tajawal", 16),
    bg="#ff66b2",
    fg="white",
    activebackground="#ff3385",
    width=10,
    relief="flat",
    cursor="hand2"
)
start_button.place(relx=0.5, rely=0.55, anchor="center")

welcome_frame.pack(fill="both", expand=True)

# ----------------------------------------
# دالة للانتقال بين الصفحات مع مؤثر
def fade_transition(next_frame):
    current = root.winfo_children()[-1]
    current.pack_forget()
    next_frame.pack(fill="both", expand=True)
    fade_in(root)

# ----------------------------------------
# الصفحة 3 - السؤال الثاني (الآن تظهر ثانية)
def next_page():
    question2_frame.pack_forget()
    fade_transition(question1_frame)  # الانتقال إلى الصفحة 2 (السؤال الأول)

question2_frame = tk.Frame(root)
canvas3 = gradient_bg(question2_frame, "#ffd6eb", "#ffccff")

label_question2 = tk.Label(
    question2_frame,
    text="ممكن نتعرف؟ ", 
    font=("Tajawal", 20, "bold"),
    bg="#ffe6f2",
    fg="#99004d"
)
label_question2.place(relx=0.5, rely=0.35, anchor="center")

yes1 = tk.Button(
    question2_frame,
    text="اي",
    command=next_page,
    font=("Tajawal", 14),
    bg="#ff66b2",
    fg="white",
    width=10,
    relief="flat",
    cursor="hand2"
)
yes1.place(relx=0.5, rely=0.5, anchor="center")

yes2 = tk.Button(
    question2_frame,
    text="هم اي",
    command=next_page,
    font=("Tajawal", 14),
    bg="#ff66b2",
    fg="white",
    width=10,
    relief="flat",
    cursor="hand2"
)
yes2.place(relx=0.5, rely=0.6, anchor="center")

# ----------------------------------------
# الصفحة 2 - السؤال الأول (الآن تظهر ثالثة)
def send_answer():
    answer = answer_entry.get()
    if answer.strip():
        messagebox.showinfo("تم الإرسال", f"تم إرسال إجابتك: {answer} 💌")
    else:
        messagebox.showwarning("إجابة فارغة", "جاوبي أول يا قمر 😅")
        return
    question1_frame.pack_forget()
    fade_transition(final_frame)

question1_frame = tk.Frame(root)
canvas2 = gradient_bg(question1_frame, "#ffe6f2", "#ffd6eb")

label_question1 = tk.Label(
    question1_frame,
    text="زين ليش انتي هلكد حلوة ؟", 
    font=("Tajawal", 18, "bold"),
    bg="#ffe6f2",
    fg="#99004d"
)
label_question1.place(relx=0.5, rely=0.3, anchor="center")

answer_entry = tk.Entry(question1_frame, font=("Tajawal", 14), width=25, justify="center")
answer_entry.place(relx=0.5, rely=0.45, anchor="center")

send_button = tk.Button(
    question1_frame,
    text="إرسال الإجابة 💌",
    command=send_answer,
    font=("Tajawal", 14),
    bg="#ff66b2",
    fg="white",
    relief="flat",
    activebackground="#ff3385",
    width=14
)
send_button.place(relx=0.5, rely=0.6, anchor="center")

# ----------------------------------------
# الصفحة النهائية
final_frame = tk.Frame(root)
canvas4 = gradient_bg(final_frame, "#ffe6f2", "#ffcce0")

label_final = tk.Label(
    final_frame,
    text="يلا كافي ", 
    font=("Tajawal", 26, "bold"),
    bg="#ffe6f2",
    fg="#cc0066"
)
label_final.place(relx=0.5, rely=0.2, anchor="center")

try:
    image = Image.open("damon.jpg")
    image = image.resize((250, 250))
    img = ImageTk.PhotoImage(image)
    label_image = tk.Label(final_frame, image=img, bg="#ffe6f2")
    label_image.image = img
    label_image.place(relx=0.5, rely=0.6, anchor="center")
except:
    label_no_image = tk.Label(final_frame, text="(أضف صورة damon.jpg بجانب الملف)", bg="#ffe6f2", fg="gray")
    label_no_image.place(relx=0.5, rely=0.6, anchor="center")

# ----------------------------------------
root.mainloop()