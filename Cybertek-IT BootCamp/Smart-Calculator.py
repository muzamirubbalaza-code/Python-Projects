import tkinter as tk
import requests



def press(symbol):
    current = expression_var.get()
    expression_var.set(current + symbol)  # append symbol to expression
 
def calculate():
    try:
        expr   = expression_var.get()
        result = eval(expr)               # eval() runs the maths expression
        result = round(result, 8)         # avoid floating point artifacts
        expression_var.set(str(result))
        result_var.set('= ' + str(result))
    except ZeroDivisionError:
        expression_var.set('Cannot divide by zero')
        result_var.set('')
    except Exception:
        expression_var.set('Invalid expression')
        result_var.set('')
 
def clear_all():
    expression_var.set('')
    result_var.set('')
 
def backspace():
    current = expression_var.get()
    expression_var.set(current[:-1])      # remove last character
 
# ── Joke fetcher ──────────────────────────
def get_joke():
    joke_label.config(text='Fetching joke...')
    try:
        url  = 'https://official-joke-api.appspot.com/random_joke'
        resp = requests.get(url, timeout=5)
 
        if resp.status_code == 200:
            data  = resp.json()            # parse JSON → Python dict
            setup = data['setup']
            punch = data['punchline']
            joke_label.config(text=setup + '\n' + punch)
        else:
            joke_label.config(text='Could not load joke (HTTP ' + str(resp.status_code) + ')')
    except requests.exceptions.ConnectionError:
        joke_label.config(text='No internet connection.')
    except Exception as e:
        joke_label.config(text='Error: ' + str(e))
 
# ══ Build the window ══════════════════════
root = tk.Tk()
root.title('Cyberteks-IT  Smart Calculator')
root.geometry('360x540')
root.configure(bg='#0D2252')
root.resizable(False, False)
 
# ── StringVar — auto-updates linked widgets ──
expression_var = tk.StringVar()
result_var     = tk.StringVar()
 
# ── Title ──
tk.Label(root, text='CYBERTEKS-IT  CALCULATOR',
         bg='#0D2252', fg='white',
         font=('Arial', 12, 'bold')).pack(pady=(14,6))
 
# ── Expression display (dark panel) ──
display_frame = tk.Frame(root, bg='#0A1628', padx=14, pady=10)
display_frame.pack(fill='x', padx=16, pady=4)
 
# textvariable= links this Label to expression_var
tk.Label(display_frame, textvariable=expression_var,
         bg='#0A1628', fg='#93C5FD',
         font=('Courier New', 14),
         anchor='e', wraplength=290).pack(fill='x')
 
tk.Label(display_frame, textvariable=result_var,
         bg='#0A1628', fg='#FCD34D',
         font=('Courier New', 18, 'bold'),
         anchor='e').pack(fill='x')
 
# ── Button grid — created with a loop ──
button_labels = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '(', '+'],
    [')',  'C', '←', '='],
]
 
btn_frame = tk.Frame(root, bg='#0D2252')
btn_frame.pack(padx=16, pady=8)
 
for row_index, row in enumerate(button_labels):
    for col_index, label in enumerate(row):
 
        # Choose color based on button type
        if label == '=':
            bg_color, fg_color = '#CC2222', 'white'
        elif label in '/*-+':
            bg_color, fg_color = '#162E6B', '#93C5FD'
        elif label == 'C':
            bg_color, fg_color = '#4B5563', 'white'
        else:
            bg_color, fg_color = '#1E3A5F', 'white'
 
        # Map label to the right function
        if label == '=':
            cmd = calculate
        elif label == 'C':
            cmd = clear_all
        elif label == '←':
            cmd = backspace
        else:
            # lambda captures label at creation time
            cmd = lambda s=label: press(s)
 
        tk.Button(btn_frame,
                  text=label,
                  command=cmd,
                  width=5, height=2,
                  bg=bg_color, fg=fg_color,
                  font=('Arial', 12, 'bold'),
                  relief='flat'           # removes 3D border
        ).grid(row=row_index, column=col_index, padx=3, pady=3)
 
# ── Joke section ──
tk.Label(root, text='😂 Random Joke',
         bg='#0D2252', fg='white',
         font=('Arial', 11, 'bold')).pack(pady=(10,4))

joke_label = tk.Label(root,
                      text='Click the button to get a joke',
                      bg='#0A1628', fg='#E5E7EB',
                      font=('Arial', 10),
                      wraplength=300,
                      justify='center',
                      padx=10, pady=10)
joke_label.pack(padx=16, pady=4, fill='x')

tk.Button(root,
          text='Get Joke',
          command=get_joke,
          bg='#22C55E', fg='white',
          font=('Arial', 10, 'bold'),
          relief='flat').pack(pady=6)

root.mainloop()