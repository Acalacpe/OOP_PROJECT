import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

from evaluator import StrengthEvaluator
from analyzer import PasswordAnalyzer
from Suggestor import Suggestor
from feedback import get_feedback
from crackTime import findCrackTime
from generator import Generator


def run_app():

    def analyze():
        password = password_var.get()

        feedback_text.set("")
        suggested_var.set("")

        if not password:
            meter.configure(amountused=0, bootstyle="danger")
            percent_var.set("📊 Score: 0/50")
            strength_var.set("💪 Strength: Very Weak")
            strength_label.configure(foreground="red")
            entropy_var.set("🧠 Entropy: 0")
            crack_time_var.set("⏱ Crack Time: 0")
            feedback_text.set("")
            suggested_var.set("")
            return

        analyzer = PasswordAnalyzer(password)
        evaluator = StrengthEvaluator(password)

        strength, score, entropy = evaluator.evaluate()

        display_score = max(0, min(score, 50))

        meter.configure(amountused=display_score)
        percent_var.set(f"📊 Score: {display_score}/50")
        entropy_var.set(f"🧠 Entropy: {round(entropy, 2)}")

        if strength in ["Very Weak", "Weak"]:
            meter.configure(bootstyle="danger")
        elif strength == "Medium":
            meter.configure(bootstyle="warning")
        else:
            meter.configure(bootstyle="success")

        strength_var.set(f"💪 Strength: {strength}")

        color_map = {
            "Very Weak": "red",
            "Weak": "red",
            "Medium": "orange",
            "Strong": "green"
        }

        strength_label.configure(
            foreground=color_map.get(strength, "white")
        )

        crack_time_var.set(f"⏱ Crack Time: {findCrackTime(password)}")

        feedback_list = []

        if strength == "Strong":
            suggested_var.set("")
        else:
            feedback_list = get_feedback(password, analyzer)
            suggested_var.set(Suggestor.suggestPass(password))

        if feedback_list:
            feedback_text.set("\n".join([f"• {item}" for item in feedback_list]))
        elif strength != "Strong":
            feedback_text.set("")

    def generate_random():
        generated_var.set(Generator.generate())

    def copy_text(var):
        root.clipboard_clear()
        root.clipboard_append(var.get())
        root.update()

    root = ttk.Window(themename="cyborg")
    root.title("OOP Project")
    root.geometry("600x750")

    main = ttk.Frame(root, padding=20)
    main.pack(fill=BOTH, expand=True)

    ttk.Label(main, text="🔐 Password Analyzer", font=("Arial", 22, "bold")).pack(pady=10)

    password_var = StringVar()
    ttk.Entry(main, textvariable=password_var, width=40).pack(pady=10)

    ttk.Button(main, text="Analyze", command=analyze, bootstyle="success").pack(pady=5)

    meter = ttk.Meter(
        main,
        metersize=200,
        amountused=0,
        amounttotal=50,
        metertype="semi",
        bootstyle="danger"
    )
    meter.pack(pady=15)

    percent_var = StringVar()
    ttk.Label(main, textvariable=percent_var).pack()

    strength_var = StringVar()

    strength_label = ttk.Label(
        main,
        textvariable=strength_var,
        font=("Arial", 14, "bold"),
        foreground="red"
    )
    strength_label.pack()

    entropy_var = StringVar()
    ttk.Label(main, textvariable=entropy_var).pack(pady=5)

    crack_time_var = StringVar()
    ttk.Label(main, textvariable=crack_time_var, bootstyle="info").pack(pady=5)

    ttk.Separator(main).pack(fill=X, pady=10)

    ttk.Label(main, text="🔍 Feedback", font=("Arial", 12, "bold")).pack()

    feedback_text = StringVar()
    ttk.Label(
        main,
        textvariable=feedback_text,
        wraplength=500,
        justify=LEFT
    ).pack(pady=5)

    ttk.Separator(main).pack(fill=X, pady=10)

    ttk.Label(main, text="💡 Suggested Password").pack()

    suggested_var = StringVar()
    ttk.Entry(main, textvariable=suggested_var, width=40, state="readonly").pack(pady=5)

    ttk.Button(
        main,
        text="Copy",
        command=lambda: copy_text(suggested_var),
        bootstyle="primary"
    ).pack(pady=5)

    ttk.Separator(main).pack(fill=X, pady=10)

    ttk.Label(main, text="🎲 Generate Password").pack()

    generated_var = StringVar()
    ttk.Entry(main, textvariable=generated_var, width=40, state="readonly").pack(pady=5)

    btn_frame = ttk.Frame(main)
    btn_frame.pack(pady=5)

    ttk.Button(
        btn_frame,
        text="Generate",
        command=generate_random,
        bootstyle="warning"
    ).pack(side=LEFT, padx=5)

    ttk.Button(
        btn_frame,
        text="Copy",
        command=lambda: copy_text(generated_var),
        bootstyle="primary"
    ).pack(side=LEFT, padx=5)

    meter.configure(amountused=0, bootstyle="danger")
    percent_var.set("📊 Score: 0/50")
    strength_var.set("💪 Strength: Very Weak")
    entropy_var.set("🧠 Entropy: 0")
    crack_time_var.set("⏱ Crack Time: 0")
    feedback_text.set("")
    suggested_var.set("")

    root.mainloop()