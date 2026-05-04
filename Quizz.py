import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont # For custom fonts
import time # Used for the countdown timer
import random

# ==============================================================
#  COLOUR & STYLE CONSTANTS
#  Centralising colours here makes it easy to restyle the app.
# ==============================================================
BG_DARK       = "#1A1A2E"   # Deep navy – main background
BG_CARD       = "#16213E"   # Slightly lighter – card/panel background
BG_PANEL      = "#1E2235"
ACCENT        = "#E94560"   # Vivid red-pink – highlights & buttons
ACCENT2       = "#7B61FF"       # violet
ACCENT_HOVER  = "#C73652"   # Darker shade for hover effect
CORRECT_CLR   = "#0F9B58"   # Green – correct answer feedback
WRONG_CLR     = "#E94560"   # Red-pink – wrong answer feedback
WRONG         = "#FF4C6A"
TEXT_LIGHT    = "#EAEAEA"   # Near-white – main text
TEXT_SEC      = "#8890B5"
TEXT_PRI      = "#EAEEFF"
CORRECT       = "#00C896"
TIMER_OK      = "#00E5FF"
TIMER_LOW     = "#FF4C6A"
TEXT_DIM      = "#8A8FAD"   # Muted blue-grey – secondary text
TIMER_WARN    = "#F5A623"   # Amber – timer warning colour

QUESTIONS = [
    {
        "question":"Which keyword do we use use to define a function in python?",
        "options":["func","def","define"],
        "answer": 1 # Index of the correct option
    },
    {
        "question":"What does len('Kampala') return?",
        "options":["6","8","7"],
        "answer": 2
    },
    {
        "question":"Which of these correctly converts a string '42' to an integer?",
        "options":["integer('42')","int('42')","number('42')"],
        "answer": 1
    },
    {
        "question":"What is the print(type(3.14)) output?",
        "options":["<class 'int'>","<class 'str'>","<class 'float'>"],
        "answer": 2
    },
    {
        "question":"Which operator  gives the reminder of division?",
        "options":["/","//","%"],
        "answer": 2
    },
    {
        "question":"What Tkinter method places a widget on the window?",
        "options":[".show()",".pack()",".display()"],
        "answer": 1
    },
    {
        "question":"What does root.mainloop() do in a Tkinter application?",
        "options":["Loops through all widgets","Runs a for a loop","opens the window and waits for events"],
        "answer": 2
    },
    {
        "question":"How do you read text from an Entry widget called name_entry?",
        "options":["name_entry.read()","name_entry.value()","name_entry.get()"],
        "answer": 2
    },
    {
        "question":"What does command=greet do in a Button widget (without brackets)?",
        "options":["calls greet immediately","links the button to the greet function","imports greet"],
        "answer": 1
    },
    {
        "question":"Which layout manager places widgets in rows and columns?",
        "options":[".pack()",".grid()",".place()"],
        "answer": 1
    },
    {
        "question":"What is the output of: x = 10;  print(x>5 and x<20)?",
        "options":["False","Error","True"],
        "answer": 2
    },
    {
        "question":"How do you clear all text from an Entry widget called entry?",
        "options":["entry.clear()","entry.delete(0,tk.END)","entry.reset()"],
        "answer": 1
    },
    {
        "question":"What does round(3.14159,2) return",
        "options":["3.14","3.1","3.15"],
        "answer": 0
    },
    {
        "question":"Which python keyword skips the rest of the function and returns nothing?",
        "options":["stop","exit","return"],
        "answer": 2
    },
    {
        "question":"What is the correct way to format a string with a variable called name?",
        "options":["'Hello' + name","Using an f string format","Both A and B work"],
        "answer": 2
    }
]

QUESTION_TIME = 20 #Seconds per question

class CyberteksApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cyberteks-IT Quizz App")
        self.geometry("780x540")
        self.resizable(False,False)
        self.configure(bg=BG_DARK)

        # ── shared state ──────────────────────────────
        self.score        = 0
        self.q_index      = 0
        self.questions    = []
        self.selected_ans = tk.StringVar()
        self.timer_var    = tk.StringVar(value="20")
        self._timer_id    = None

        # ── fonts ─────────────────────────────────────
        self.f_title  = tkfont.Font(family="Courier", size=22, weight="bold")
        self.f_sub    = tkfont.Font(family="Courier", size=11)
        self.f_qnum   = tkfont.Font(family="Courier", size=10, weight="bold")
        self.f_q      = tkfont.Font(family="Courier", size=13, weight="bold")
        self.f_opt    = tkfont.Font(family="Courier", size=11)
        self.f_btn    = tkfont.Font(family="Courier", size=12, weight="bold")
        self.f_score  = tkfont.Font(family="Courier", size=36, weight="bold")
        self.f_pct    = tkfont.Font(family="Courier", size=18)
        self.f_msg    = tkfont.Font(family="Courier", size=13, weight="bold")
        self.f_timer  = tkfont.Font(family="Courier", size=13, weight="bold")

        # ── build all frames ──────────────────────────
        self._frames = {}
        self._build_welcome()
        self._build_quiz()
        self._build_results()

        self.show_frame("welcome")

    # ════════════════════════════════════════════
    #  FRAME NAVIGATION
    # ════════════════════════════════════════════
    def show_frame(self, name: str):
        self._frames[name].tkraise()

    # ════════════════════════════════════════════
    #  WELCOME SCREEN
    # ════════════════════════════════════════════
    def _build_welcome(self):
        f = tk.Frame(self, bg=BG_DARK)
        f.place(relwidth=1, relheight=1)
        self._frames["welcome"] = f

        # decorative top bar
        bar = tk.Frame(f, bg=ACCENT, height=3)
        bar.pack(fill="x", side="top")

        # centre card
        card = tk.Frame(f, bg=BG_CARD, padx=50, pady=40,
                        highlightbackground=ACCENT2, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center")

        # glowing bracket decorations
        tk.Label(card, text="{ }", font=tkfont.Font(family="Courier", size=30),
                 fg=ACCENT2, bg=BG_CARD).pack()

        tk.Label(card,
                 text="CYBERTEKS-IT\nQUIZ APP",
                 font=self.f_title,
                 fg=ACCENT, bg=BG_CARD,
                 justify="center").pack(pady=(6, 4))

        tk.Label(card,
                 text="Test your Python & Tkinter Knowledge",
                 font=self.f_sub,
                 fg=TEXT_SEC, bg=BG_CARD).pack(pady=(0, 6))
        
        # divider
        tk.Frame(card, bg=ACCENT2, height=1, width=320).pack(pady=10)

        info = (
            "▸  15 Questions\n"
            "▸  20-second timer per question\n"
            "▸  Questions shuffled every run"
        )
        tk.Label(card, text=info, font=self.f_opt,
                 fg=TEXT_SEC, bg=BG_CARD, justify="left").pack(pady=8)

        tk.Button(card,
                  text="[ START QUIZ ]",
                  font=self.f_btn,
                  fg=BG_DARK, bg=ACCENT,
                  activebackground=ACCENT2,
                  activeforeground=TEXT_PRI,
                  relief="flat", cursor="hand2",
                  padx=24, pady=10,
                  command=self._start_quiz).pack(pady=(14, 0))

        # bottom bar
        tk.Frame(f, bg=ACCENT2, height=3).pack(fill="x", side="bottom")

    # ════════════════════════════════════════════
    #  QUIZ SCREEN
    # ════════════════════════════════════════════
    def _build_quiz(self):
        f = tk.Frame(self, bg=BG_DARK)
        f.place(relwidth=1, relheight=1)
        self._frames["quiz"] = f

        # ── top header bar ────────────────────────────
        header = tk.Frame(f, bg=BG_PANEL, pady=10)
        header.pack(fill="x")

        tk.Label(header, text="CYBERTEKS-IT QUIZ",
                 font=self.f_qnum, fg=ACCENT, bg=BG_PANEL).pack(side="left", padx=20)

        # timer badge on the right
        timer_frame = tk.Frame(header, bg=BG_PANEL)
        timer_frame.pack(side="right", padx=20)
        tk.Label(timer_frame, text="⏱", font=self.f_timer,
                 fg=TEXT_SEC, bg=BG_PANEL).pack(side="left")
        self.timer_lbl = tk.Label(timer_frame,
                                  textvariable=self.timer_var,
                                  font=self.f_timer,
                                  fg=TIMER_OK, bg=BG_PANEL, width=3)
        self.timer_lbl.pack(side="left", padx=(4, 0))

        # progress bar track
        self.progress_track = tk.Frame(f, bg=BG_PANEL, height=5)
        self.progress_track.pack(fill="x")
        self.progress_fill = tk.Frame(self.progress_track, bg=ACCENT, height=5)
        self.progress_fill.place(x=0, y=0, relheight=1)

        # ── question number + text ────────────────────
        body = tk.Frame(f, bg=BG_DARK, padx=40, pady=10)
        body.pack(fill="both", expand=True)

        self.q_num_lbl = tk.Label(body, text="Question 1 of 15",
                                  font=self.f_qnum, fg=ACCENT2, bg=BG_DARK)
        self.q_num_lbl.pack(anchor="w", pady=(10, 6))

        self.q_lbl = tk.Label(body, text="",
                              font=self.f_q,
                              fg=TEXT_PRI, bg=BG_DARK,
                              wraplength=680, justify="left")
        self.q_lbl.pack(anchor="w", pady=(0, 18))

        # ── radio-button options ──────────────────────
        self.radio_btns = []
        self.option_frames = []
        for _ in range(3):
            row = tk.Frame(body, bg=BG_CARD, padx=16, pady=10,
                           highlightbackground=BG_PANEL, highlightthickness=1)
            row.pack(fill="x", pady=5)

            rb = tk.Radiobutton(row,
                                text="",
                                variable=self.selected_ans,
                                value="",
                                font=self.f_opt,
                                fg=TEXT_PRI,
                                bg=BG_CARD,
                                selectcolor=BG_PANEL,
                                activebackground=BG_PANEL,
                                activeforeground=ACCENT,
                                relief="flat",
                                cursor="hand2",
                                command=lambda r=row: self._highlight_selected(r))
            rb.pack(anchor="w")
            self.radio_btns.append(rb)
            self.option_frames.append(row)

        # ── next button ───────────────────────────────
        btn_row = tk.Frame(body, bg=BG_DARK)
        btn_row.pack(fill="x", pady=(14, 0))

        self.next_btn = tk.Button(btn_row,
                                  text="NEXT  ›",
                                  font=self.f_btn,
                                  fg=BG_DARK, bg=ACCENT,
                                  activebackground=ACCENT2,
                                  activeforeground=TEXT_PRI,
                                  relief="flat", cursor="hand2",
                                  padx=24, pady=8,
                                  command=self._next_question)
        self.next_btn.pack(side="right")

        self.feedback_lbl = tk.Label(btn_row, text="",
                                     font=self.f_opt,
                                     fg=TEXT_SEC, bg=BG_DARK)
        self.feedback_lbl.pack(side="left")

    def _highlight_selected(self, selected_row):
        for row in self.option_frames:
            row.configure(highlightbackground=BG_PANEL if row is not selected_row else ACCENT)


    # ════════════════════════════════════════════
    #  RESULTS SCREEN
    # ════════════════════════════════════════════
    def _build_results(self):
        f = tk.Frame(self, bg=BG_DARK)
        f.place(relwidth=1, relheight=1)
        self._frames["results"] = f

        tk.Frame(f, bg=ACCENT, height=3).pack(fill="x", side="top")

        card = tk.Frame(f, bg=BG_CARD, padx=60, pady=40,
                        highlightbackground=ACCENT2, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="QUIZ COMPLETE",
                 font=self.f_qnum, fg=ACCENT2, bg=BG_CARD).pack()

        self.score_lbl = tk.Label(card, text="",
                                  font=self.f_score,
                                  fg=ACCENT, bg=BG_CARD)
        self.score_lbl.pack(pady=(10, 2))

        self.pct_lbl = tk.Label(card, text="",
                                font=self.f_pct,
                                fg=TEXT_SEC, bg=BG_CARD)
        self.pct_lbl.pack()

        tk.Frame(card, bg=ACCENT2, height=1, width=320).pack(pady=14)

        self.msg_lbl = tk.Label(card, text="",
                                font=self.f_msg,
                                fg=CORRECT, bg=BG_CARD,
                                justify="center")
        self.msg_lbl.pack(pady=(0, 14))

        btn_row = tk.Frame(card, bg=BG_CARD)
        btn_row.pack()

        tk.Button(btn_row,
                  text="[ RESTART ]",
                  font=self.f_btn,
                  fg=BG_DARK, bg=ACCENT,
                  activebackground=ACCENT2,
                  activeforeground=TEXT_PRI,
                  relief="flat", cursor="hand2",
                  padx=20, pady=9,
                  command=self._reset).pack(side="left", padx=8)

        tk.Button(btn_row,
                  text="[ QUIT ]",
                  font=self.f_btn,
                  fg=ACCENT, bg=BG_PANEL,
                  activebackground=BG_DARK,
                  activeforeground=ACCENT,
                  relief="flat", cursor="hand2",
                  padx=20, pady=9,
                  command=self.destroy).pack(side="left", padx=8)

        tk.Frame(f, bg=ACCENT2, height=3).pack(fill="x", side="bottom")

# ════════════════════════════════════════════
    #  QUIZ LOGIC
    # ════════════════════════════════════════════
    def _start_quiz(self):
        self._reset_state()
        self.questions = QUESTIONS.copy()
        random.shuffle(self.questions)
        self._load_question()
        self.show_frame("quiz")

    def _reset_state(self):
        self.score   = 0
        self.q_index = 0
        self.selected_ans.set("")
        if self._timer_id:
            self.after_cancel(self._timer_id)
            self._timer_id = None

    def _load_question(self):
        # reset option frames
        for row in self.option_frames:
            row.configure(highlightbackground=BG_PANEL)

        q = self.questions[self.q_index]
        total = len(self.questions)

        self.q_num_lbl.configure(text=f"Question {self.q_index + 1} of {total}")
        self.q_lbl.configure(text=q["question"])

        self.selected_ans.set("-1")   # -1 = nothing selected
        self.feedback_lbl.configure(text="")

        # Shuffle options but track where the correct answer lands
        indexed_opts = list(enumerate(q["options"]))   # [(0,"func"),(1,"def"),(2,"define")]
        random.shuffle(indexed_opts)

        # Store the new position of the correct answer
        self._correct_index = None
        for new_pos, (orig_index, text) in enumerate(indexed_opts):
            if orig_index == q["answer"]:
                self._correct_index = new_pos   # this is where correct ended up

        # Update radio buttons with shuffled text, value = new position as string
        for new_pos, (orig_index, text) in enumerate(indexed_opts):
            self.radio_btns[new_pos].configure(
                text=text,
                value=str(new_pos),   # value is the NEW position index
                fg=TEXT_PRI
            )

        # progress bar
        pct = (self.q_index / total)
        self.update_idletasks()
        track_w = self.progress_track.winfo_width() or 780
        self.progress_fill.configure(width=int(track_w * pct))

        self._start_timer()

    def _start_timer(self):
        if self._timer_id:
            self.after_cancel(self._timer_id)
        self._time_left = QUESTION_TIME
        self.timer_var.set(str(self._time_left))
        self.timer_lbl.configure(fg=TIMER_OK)
        self._tick()

    def _tick(self):
        if self._time_left <= 0:
            self.feedback_lbl.configure(text="⏱ Time's up!", fg=WRONG)
            self._timer_id = self.after(700, self._next_question)
            return
        color = TIMER_LOW if self._time_left <= 5 else TIMER_OK
        self.timer_lbl.configure(fg=color)
        self.timer_var.set(str(self._time_left))
        self._time_left -= 1
        self._timer_id = self.after(1000, self._tick)

    def _next_question(self):
        if self._timer_id:
            self.after_cancel(self._timer_id)
            self._timer_id = None

        chosen = self.selected_ans.get()   # a string like "0", "1", "2", or "-1"

        if chosen != "-1" and int(chosen) == self._correct_index:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(self.questions):
            self._load_question()
        else:
            self._show_results()

    def _show_results(self):
        total = len(self.questions)
        pct   = (self.score / total) * 100

        self.score_lbl.configure(text=f"{self.score}/{total}")
        self.pct_lbl.configure(text=f"{pct:.1f}%")

        if pct >= 80:
            msg   = "🏆  Excellent work!"
            color = CORRECT
        elif pct >= 50:
            msg   = "👍  Good job!"
            color = ACCENT
        else:
            msg   = "📚  Keep practicing!"
            color = TIMER_LOW

        self.msg_lbl.configure(text=msg, fg=color)
        self.show_frame("results")

    def _reset(self):
        self._start_quiz()


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = CyberteksApp()
    app.mainloop()
      