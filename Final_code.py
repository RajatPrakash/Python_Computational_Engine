from tkinter.scrolledtext import ScrolledText

import wolframalpha
import wikipedia
import tkinter as tk

window = tk.Tk()
window.geometry('300x400')
window.title('Personal Computational Assistance')
window.resizable(False, False)
entry = tk.Entry(window, bg='white', borderwidth=5, font=('Arial BOLD', 20))
entry.pack()


def get_data():
    user_input = entry.get()
    try:
        app_id = 'Q3K2GK-2E3XXXXXXX'
        client = wolframalpha.Client(app_id)
        answer = client.query(user_input)
        result = next(answer.results).text
        label.configure(text=result)
    except:
        result = wikipedia.summary(user_input)
        label.configure(text=result)


search = tk.Button(window, text='Search', borderwidth=5, font=('Arial BOLD', 15), command=get_data)
search.pack()

bottom_frame = tk.Frame(window)
bottom_frame.place(relx=0.1, rely=0.35, relwidth=0.85, relheight=0.6)
label = tk.Label(bottom_frame,text='testing', bg='grey')
#lbl = ScrolledText(window, bg='white', relief='GROOVE', height=600, width=400, font='TkFixedFont',).grid(row = 50, column = 1, sticky=N+S+E+W)
label.place(relwidth=1, relheight=1)

window.mainloop()
