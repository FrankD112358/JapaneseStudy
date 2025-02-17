import tkinter as tk
import wanakana
import webbrowser
from wanikani import wanikani
from word_list import mark_answer


is_correct = True


def next_word(root, words):
    refresh(root)

    if words:
        phrase = words[0][0]
        meaning, on_yomi_reading, kun_yomi_reading, url = wanikani(phrase)

        # TODO:
        on_yomi_meaning = None
        kun_yomi_meaning = None
        
        words.pop(0)

        root.label_phrase = tk.Label(root.window, text=phrase, bg='#333333', fg='#aaaaaa', font=('Arial', 24, 'normal'))
        root.label_phrase.pack(pady=(20, 20), ipadx=20, ipady=20)

        if on_yomi_meaning and kun_yomi_meaning:
            root.label_on_meaning = tk.Label(root.window, text="On'yomi Meaning", bg='#333333', fg='#aaaaaa')
            root.label_on_meaning.pack()

            root.entry_on_meaning = tk.Entry(root.window, width=50)
            root.entry_on_meaning.bind("<Return>", lambda e: on_enter_pressed(root))
            root.entry_on_meaning.pack(pady=(10, 10), ipadx=10, ipady=10)

            root.label_kun_meaning = tk.Label(root.window, text="Kun'yomi Meaning", bg='#333333', fg='#aaaaaa')
            root.label_kun_meaning.pack()

            root.entry_kun_meaning = tk.Entry(root.window, width=50)
            root.entry_kun_meaning.bind("<Return>", lambda e: on_enter_pressed(root))
            root.entry_kun_meaning.pack(pady=(10, 10), ipadx=10, ipady=10)
        else:
            root.label_meaning = tk.Label(root.window, text='Meaning', bg='#333333', fg='#aaaaaa')
            root.label_meaning.pack()

            root.entry_meaning = tk.Entry(root.window, width=50)
            root.entry_meaning.bind("<Return>", lambda e: on_enter_pressed(root))
            root.entry_meaning.pack(pady=(10, 10), ipadx=10, ipady=10)

        if on_yomi_reading and kun_yomi_reading:
            root.label_on_reading = tk.Label(root.window, text="On'yomi Reading", bg='#333333', fg='#aaaaaa')
            root.label_on_reading.pack()

            root.entry_on_reading = tk.Entry(root.window, width=50)
            root.entry_on_reading.bind('<KeyRelease>', lambda e: endtry_update(root.entry_on_reading))
            root.entry_on_reading.bind("<Return>", lambda e: on_enter_pressed(root))
            root.entry_on_reading.pack(pady=(10, 10), ipadx=10, ipady=10)

            root.label_kun_reading = tk.Label(root.window, text="Kun'yomi Reading", bg='#333333', fg='#aaaaaa')
            root.label_kun_reading.pack()

            root.entry_kun_reading = tk.Entry(root.window, width=50)
            root.entry_kun_reading.bind('<KeyRelease>', lambda e: endtry_update(root.entry_kun_reading))
            root.entry_kun_reading.bind("<Return>", lambda e: on_enter_pressed(root))
            root.entry_kun_reading.pack(pady=(10, 10), ipadx=10, ipady=10)
        else:
            root.label_reading = tk.Label(root.window, text='Reading', bg='#333333', fg='#aaaaaa')
            root.label_reading.pack()

            root.entry_reading = tk.Entry(root.window, width=50)
            root.entry_reading.bind('<KeyRelease>', lambda e: endtry_update(root.entry_reading))
            root.entry_reading.bind("<Return>", lambda e: on_enter_pressed(root))
            root.entry_reading.pack(pady=(10, 10), ipadx=10, ipady=10)

        root.label_words_count = tk.Label(root.window, text=f'言葉：{len(words)}', bg='#333333', fg='#aaaaaa')
        root.label_words_count.pack(padx=(10, 10), anchor=tk.W)        

        root.button_submit = tk.Button(root.window, text='Submit', command=lambda: submit(
                                    root, words, meaning, on_yomi_meaning, on_yomi_reading, kun_yomi_meaning, kun_yomi_reading, url, phrase), bg='#666666', fg='white')
        root.button_submit.pack(pady=(10, 10), ipadx=10, ipady=10)


def endtry_update(entry):
    japanese_result = wanakana.to_hiragana(entry.get(), custom_kana_mapping={'nn': 'ん', 'n': 'n'})
    entry.delete(0, tk.END)
    entry.insert(0, japanese_result) 


def submit(root, words, meaning, on_yomi_meaning, on_yomi_reading, kun_yomi_meaning, kun_yomi_reading, url, phrase):
    global is_correct

    correct_meaning = True
    correct_on_meaning = True
    correct_kun_meaning = True
    correct_on_reading = True
    correct_kun_reading = True
    in_meaning = ''
    in_on_yomi_meaning = 'none'
    in_kun_yomi_meaning = ''
    in_on_yomi_reading = ''
    in_kun_yomi_reading = ''

    if meaning:
        try:
            in_meaning = root.entry_meaning.get().lower().strip()
            correct_meaning = check(in_meaning, meaning, root.entry_meaning)
            print(f'in_meaning: {in_meaning}, meaning: {meaning}')
        except:
            in_meaning = ''
    if on_yomi_meaning:
        try:
            in_on_yomi_meaning = root.entry_on_meaning.get().lower().strip()
            correct_on_meaning = check(in_on_yomi_meaning, on_yomi_meaning, root.entry_on_meaning)
            print(f'in_on_yomi_meaning: {in_on_yomi_meaning}, on_yomi_meaning: {on_yomi_meaning}')
        except:
            in_on_yomi_meaning = ''
    if kun_yomi_meaning:
        try:
            in_kun_yomi_meaning = root.entry_kun_meaning.get().lower().strip()
            correct_kun_meaning = check(in_kun_yomi_meaning, kun_yomi_meaning, root.entry_kun_meaning)
            print(f'in_kun_yomi_meaning: {in_kun_yomi_meaning}, kun_yomi_meaning: {kun_yomi_meaning}')
        except:
            in_kun_yomi_meaning = ''
    if on_yomi_reading and kun_yomi_reading:
        try:
            in_on_yomi_reading = root.entry_on_reading.get().lower().strip()
            correct_on_reading = check(in_on_yomi_reading, on_yomi_reading, root.entry_on_reading)
            print(f'in_on_yomi_reading: {in_on_yomi_reading}, on_yomi_reading: {on_yomi_reading}')
        except:
            in_on_yomi_reading = ''
    else:
        try:
            in_on_yomi_reading = root.entry_reading.get().lower().strip()
            correct_on_reading = check(in_on_yomi_reading, on_yomi_reading, root.entry_reading)
            print(f'in_on_yomi_reading: {in_on_yomi_reading}, on_yomi_reading: {on_yomi_reading}')
        except:
            in_on_yomi_reading = ''    
    if kun_yomi_reading:
        try:
            in_kun_yomi_reading = root.entry_kun_reading.get().lower().strip()
            correct_kun_reading = check(in_kun_yomi_reading, kun_yomi_reading, root.entry_kun_reading)
            print(f'in_kun_yomi_reading: {in_kun_yomi_reading}, kun_yomi_reading: {kun_yomi_reading}')
        except:
            in_kun_yomi_reading = ''

    if correct_meaning and correct_on_meaning and correct_kun_meaning and correct_on_reading and correct_kun_reading:
        root.button_submit.destroy()

        root.button_continue = tk.Button(root.window, text='Continue', command=lambda: next_word(root, words), bg='#666666', fg='white')
        root.button_continue.pack(pady=(10, 10), ipadx=10, ipady=10)

        root.label_reading = tk.Label(root.window, text='Correct', bg='#333333', fg='#aaaaaa')
        root.label_reading.pack()

        root.button_wanikani = tk.Button(root.window, text='Wanikani Page', command=lambda: webbrowser.open(url), bg='#666666', fg='white')
        root.button_wanikani.pack(pady=(10, 10), ipadx=10, ipady=10)

        mark_answer(phrase, is_correct)
    else:
        is_correct = False


def on_enter_pressed(root):
    try:
        root.button_continue.invoke()
    except:
        root.button_submit.invoke()


def check(input, actual, item):
    print('input, actual', input, actual)

    if input.lower() in actual:
        item.config(bg='#CCFFCC')
        return True
    else:
        item.config(bg='#FFD7BE')

    return False


def refresh(root):
    # Destroy all labels
    for label in root.window.winfo_children():
        if isinstance(label, tk.Label):
            label.destroy()

    # Destroy all buttons
    for button in root.window.winfo_children():
        if isinstance(button, tk.Button):
            button.destroy()

    # Destroy all entries
    for button in root.window.winfo_children():
        if isinstance(button, tk.Entry):
            button.destroy()

    # Destroy all dropdowns
    for dropdown in root.window.winfo_children():
        if isinstance(dropdown, tk.OptionMenu):
            dropdown.destroy()
