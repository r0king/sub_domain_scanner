import tkinter as tk


class NewguiApp:

    def __init__(self, master=None):
        # build ui
        self.text = tk.StringVar()
        frame_1 = tk.Frame(master)
        frame_2 = tk.Frame(frame_1)
        scrollbar_2 = tk.Scrollbar(frame_2)
        scrollbar_2.config(orient='vertical')
        scrollbar_2.place(anchor='nw', relheight='1.0', x='0', y='0')
        button_6 = tk.Button(frame_2)
        button_6.config(default='normal', text='Zen map')
        button_6.place(anchor='nw', relx='0.03', rely='0.94', x='0', y='0')
        button_7 = tk.Button(frame_2)
        button_7.config(text='burp')
        button_7.place(anchor='nw', relx='0.17', rely='0.94', x='0', y='0')
        button_8 = tk.Button(frame_2)
        button_8.config(text='terninal')
        button_8.place(anchor='nw', relx='0.31', rely='0.94', x='0', y='0')
        text_3 = tk.Text(frame_2)
        text_3.config(background='#78d9d9', font='{KacstScreen} 12 {}', height='10', insertbackground='#d959d9')
        text_3.config(insertunfocussed='none', width='50')
        self.text = '''details'''
        text_3.insert('0.0', self.text)
        text_3.place(anchor='nw', relheight='0.56', relwidth='0.95', relx='0.03', rely='0.03', x='0', y='0')
        frame_2.config(height='200', width='200')
        frame_2.place(anchor='nw', relheight='1.0', relwidth='0.7', relx='0.3', rely='0.0', x='0', y='0')
        frame_3 = tk.Frame(frame_1)

        self.entry_3 = tk.Entry(frame_3,width=50)
        self.entry_3.config(font='{Ubuntu} 12 {}')
        text = '''domain'''
        self.entry_3.delete('0', 'end')
        self.entry_3.insert('0', text)
        self.entry_3.pack(fill='both', side='top')


        buttongo=tk.Button(frame_3,width=50,command=self.clickgone)
        buttongo.pack()

        frame_3.config(height='200', width='200')
        frame_3.place(anchor='nw', relheight='1.0', relwidth='0.30', relx='0.0', rely='0.0', x='0', y='0')
        frame_1.config(height='500', relief='flat', width='900')
        frame_1.pack(side='top')

        # Main widget
        self.mainwindow = frame_1

    def clickgone(self, ):
        print(self.entry_3.get())
        return

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = NewguiApp(root)
    root.geometry('900x500')
    app.run()
