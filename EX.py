# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import time

# ==============================================================
#  COLOUR & STYLE CONSTANTS
# ==============================================================
BG_DARK      = "#1A1A2E"
BG_CARD      = "#16213E"
ACCENT       = "#E94560"
ACCENT_HOVER = "#C73652"
CORRECT_CLR  = "#0F9B58"
WRONG_CLR    = "#E94560"
TEXT_LIGHT   = "#EAEAEA"
TEXT_DIM     = "#8A8FAD"
TIMER_WARN   = "#F5A623"

# ==============================================================
#  SAMPLE QUESTIONS  (replace / expand as needed)
# ==============================================================
QUESTIONS = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Core Power Unit",
                    "Computer Personal Unit", "Central Program Utility"],
        "answer": 0   # index of the correct option
    },
    {
        "question": "Which protocol is used to load web pages?",
        "options": ["FTP", "SMTP", "HTTP", "SSH"],
        "answer": 2
    },
    {
        "question": "How many bits are in a byte?",
        "options": ["4", "8", "16", "32"],
        "answer": 1
    },
]

# ==============================================================
#  ROOT WINDOW
# ==============================================================
root = tk.Tk()
root.title("Cyberteks-IT Quiz App")
root.geometry("800x450")
root.resizable(False, False)
root.configure(bg=BG_DARK)

# Container holds all screens stacked on top of each other
container = tk.Frame(root, bg=BG_DARK)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Dictionary to store frame references by name
frames = {}

# ==============================================================
#  HELPER – bring a named frame to the front
# ==============================================================
def show_frame(name):
    frames[name].tkraise()

# ==============================================================
#  WELCOME SCREEN
# ==============================================================
welcome_frame = tk.Frame(container, bg=BG_DARK)
welcome_frame.grid(row=0, column=0, sticky="nsew")
frames["welcome"] = welcome_frame

tk.Label(
    welcome_frame,
    text="Cyberteks-IT Quiz App",
    fg=ACCENT,
    bg=BG_DARK,
    font=("Helvetica", 32, "bold"),
).pack(pady=(80, 10))

tk.Label(
    welcome_frame,
    text="Test your IT knowledge!",
    fg=TEXT_DIM,
    bg=BG_DARK,
    font=("Helvetica", 14),
).pack(pady=(0, 40))

tk.Button(
    welcome_frame,
    text="Start Quiz",
    bg=ACCENT,
    fg=TEXT_LIGHT,
    activebackground=ACCENT_HOVER,
    activeforeground=TEXT_LIGHT,
    font=("Helvetica", 18, "bold"),
    relief="flat",
    padx=24,
    pady=12,
    cursor="hand2",
    command=lambda: start_quiz(),   # ← calls start_quiz() on click
).pack()

# ==============================================================
#  QUIZ SCREEN  (built once; content is updated each question)
# ==============================================================
quiz_frame = tk.Frame(container, bg=BG_DARK)
quiz_frame.grid(row=0, column=0, sticky="nsew")
frames["quiz"] = quiz_frame

# -- Header row (question counter + timer) --
header = tk.Frame(quiz_frame, bg=BG_CARD, pady=8)
header.pack(fill="x")

counter_var = tk.StringVar(value="Question 1 / 3")
tk.Label(header, textvariable=counter_var,
         fg=TEXT_DIM, bg=BG_CARD,
         font=("Helvetica", 11)).pack(side="left", padx=20)

timer_var = tk.StringVar(value="⏱ 15s")
timer_label = tk.Label(header, textvariable=timer_var,
                        fg=TIMER_WARN, bg=BG_CARD,
                        font=("Helvetica", 11, "bold"))
timer_label.pack(side="right", padx=20)

# -- Question text --
question_var = tk.StringVar(value="")
tk.Label(quiz_frame, textvariable=question_var,
         fg=TEXT_LIGHT, bg=BG_DARK,
         font=("Helvetica", 16, "bold"),
         wraplength=700, justify="center").pack(pady=(30, 20))

# -- Answer buttons (4 options) --
option_buttons = []
btn_frame = tk.Frame(quiz_frame, bg=BG_DARK)
btn_frame.pack()

for i in range(4):
    btn = tk.Button(
        btn_frame,
        text="",
        width=30,
        bg=BG_CARD,
        fg=TEXT_LIGHT,
        activebackground=ACCENT,
        activeforeground=TEXT_LIGHT,
        font=("Helvetica", 12),
        relief="flat",
        pady=8,
        cursor="hand2",
        command=lambda idx=i: check_answer(idx),  # passes button index
    )
    # 2-column grid: buttons 0,1 on the left; 2,3 on the right
    btn.grid(row=i // 2, column=i % 2, padx=10, pady=6, sticky="ew")
    option_buttons.append(btn)

# -- Feedback label --
feedback_var = tk.StringVar(value="")
feedback_label = tk.Label(quiz_frame, textvariable=feedback_var,
                           bg=BG_DARK, font=("Helvetica", 12, "bold"))
feedback_label.pack(pady=12)

# ==============================================================
#  RESULTS SCREEN
# ==============================================================
results_frame = tk.Frame(container, bg=BG_DARK)
results_frame.grid(row=0, column=0, sticky="nsew")
frames["results"] = results_frame

result_text = tk.StringVar(value="")
tk.Label(results_frame, textvariable=result_text,
         fg=TEXT_LIGHT, bg=BG_DARK,
         font=("Helvetica", 22, "bold")).pack(pady=(80, 20))

score_text = tk.StringVar(value="")
tk.Label(results_frame, textvariable=score_text,
         fg=ACCENT, bg=BG_DARK,
         font=("Helvetica", 40, "bold")).pack()

tk.Button(
    results_frame,
    text="Play Again",
    bg=ACCENT,
    fg=TEXT_LIGHT,
    activebackground=ACCENT_HOVER,
    activeforeground=TEXT_LIGHT,
    font=("Helvetica", 14, "bold"),
    relief="flat",
    padx=20, pady=10,
    cursor="hand2",
    command=lambda: start_quiz(),
).pack(pady=30)

# ==============================================================
#  QUIZ STATE  (simple variables shared across functions)
# ==============================================================
current_q   = 0   # index of the current question
score       = 0   # running score
timer_id    = None  # holds the after() id so we can cancel it
time_left   = 15  # seconds per question

# ==============================================================
#  QUIZ LOGIC FUNCTIONS
# ==============================================================
def start_quiz():
    """Reset state and load the first question."""
    global current_q, score
    current_q = 0
    score     = 0
    load_question()
    show_frame("quiz")

def load_question():
    """Populate the quiz screen with the current question."""
    global time_left, timer_id

    # Cancel any previous countdown
    if timer_id is not None:
        root.after_cancel(timer_id)

    q_data = QUESTIONS[current_q]

    # Update header counter
    counter_var.set(f"Question {current_q + 1} / {len(QUESTIONS)}")

    # Update question text
    question_var.set(q_data["question"])

    # Update option buttons and re-enable them
    for i, btn in enumerate(option_buttons):
        btn.config(text=q_data["options"][i],
                   bg=BG_CARD, fg=TEXT_LIGHT,
                   state="normal")

    # Clear feedback
    feedback_var.set("")

    # Start countdown
    time_left = 15
    countdown()

def countdown():
    """Decrement the timer each second; auto-advance on timeout."""
    global time_left, timer_id
    timer_var.set(f"⏱ {time_left}s")

    if time_left <= 5:
        timer_label.config(fg=WRONG_CLR)   # goes red when nearly out of time
    else:
        timer_label.config(fg=TIMER_WARN)

    if time_left > 0:
        time_left -= 1
        timer_id = root.after(1000, countdown)  # schedule next tick in 1 s
    else:
        # Time is up – treat as a wrong answer
        feedback_var.set("⏰  Time's up!")
        feedback_label.config(fg=WRONG_CLR)
        disable_buttons()
        root.after(1200, next_question)

def check_answer(idx):
    """Called when the player clicks an option button."""
    global score
    cancel_timer()
    correct = QUESTIONS[current_q]["answer"]

    if idx == correct:
        score += 1
        feedback_var.set("✔  Correct!")
        feedback_label.config(fg=CORRECT_CLR)
        option_buttons[idx].config(bg=CORRECT_CLR)
    else:
        feedback_var.set("✘  Wrong answer!")
        feedback_label.config(fg=WRONG_CLR)
        option_buttons[idx].config(bg=WRONG_CLR)
        option_buttons[correct].config(bg=CORRECT_CLR)  # highlight correct

    disable_buttons()
    root.after(1200, next_question)   # short pause then move on

def next_question():
    """Advance to the next question or show results."""
    global current_q
    current_q += 1
    if current_q < len(QUESTIONS):
        load_question()
    else:
        show_results()

def show_results():
    """Display the final score screen."""
    cancel_timer()
    pct = int(score / len(QUESTIONS) * 100)
    result_text.set(f"You scored {score} out of {len(QUESTIONS)}  ({pct}%)")
    score_text.set("🏆" if pct >= 70 else "📚  Keep practising!")
    show_frame("results")

# -- Utility helpers --
def disable_buttons():
    for btn in option_buttons:
        btn.config(state="disabled")

def cancel_timer():
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

# ==============================================================
#  START ON WELCOME SCREEN
# ==============================================================
show_frame("welcome")
root.mainloop()