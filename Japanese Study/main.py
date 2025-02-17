import tkinter as tk
from word_list import get_random_words
from screen import next_word

class JapanesePhraseWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg='#333333')
        self.window.geometry('800x600')
        self.window.resizable(True, True)
        
        self.dropdown = tk.StringVar(self.window)
        self.dropdown.set('All')
        self.dropdown_menu = tk.OptionMenu(self.window, self.dropdown, 'All', 'Hiragana Attached', 'Jukugo', 'Single', 'Verb')
        self.dropdown_menu.pack(pady=(10, 10), ipadx=10, ipady=10)
        
        self.contains_label = tk.Label(self.window, text='Contains', bg='#333333', fg='#aaaaaa')
        self.contains_label.pack()
        self.contains_input = tk.Entry(self.window)
        self.contains_input.pack(pady=(10, 10), ipadx=10, ipady=10)

        self.button_submit = tk.Button(self.window, text='Start', command=self.start, bg='#666666', fg='white')
        self.button_submit.pack(pady=(10, 10), ipadx=10, ipady=10)


    def start(self):
        words = get_random_words(self.contains_input.get(), self.dropdown.get())
        next_word(self, words)

if __name__ == '__main__':
    window = JapanesePhraseWindow()
    window.window.mainloop()

# 認