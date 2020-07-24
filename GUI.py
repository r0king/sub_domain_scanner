import cl_subd_scan as scanner
import multiprocessing as mp
import tkinter as tk
from ttkthemes import ThemedStyle
from tkinter import ttk

import json

import sys


class NewguiApp(ttk.Frame):

    def __init__(self, master=None):
        self.the_scanner = mp.Process(target=scanner.main)
        self.goorrun = tk.StringVar()
        frame_1 = ttk.Frame(master, relief='flat')
        frame_2 = ttk.Frame(frame_1)
        frame_1.place(anchor='nw', relx='0.0', rely='0.0', x='0', y='0', relheight='1.0', relwidth='1.0')

        scrollbar_2 = ttk.Scrollbar(frame_2)
        scrollbar_2.config(orient='vertical')
        scrollbar_2.place(anchor='nw', relheight='1.0', x='0', y='0')

        button_6 = ttk.Button(frame_2)
        button_6.config(text='Zenmap')
        button_6.place(anchor='nw', x="20", rely='0.95')

        button_7 = ttk.Button(frame_2)
        button_7.config(text='burp')
        button_7.place(anchor='nw', x="120", rely='0.95')
        button_8 = ttk.Button(frame_2)
        button_8.config(text='terminal')
        button_8.place(anchor='nw', x="220", rely='0.95')

        self.Text_detail = tk.Text(frame_2)
        self.Text_detail.config(background='#78d9d9', font='{KacstScreen} 12 {}')
        self.Text_detail.config(width='50')
        self.Text_detail.place(anchor='nw', relheight='0.85', relwidth='1', relx='0.03', rely='0.03', x='0', y='0')
        self.Text_detail.insert(tk.END, "select domain")

        frame_2.place(anchor='nw', relheight='1.0', relwidth='0.6', relx='0.3', rely='0.0', x='0', y='0')
        frame_3 = ttk.Frame(frame_1)

        self.entry_3 = ttk.Entry(frame_3, width=50)
        self.entry_3.config(font='{Ubuntu} 12 {}')
        domaintext = 'domain'
        self.entry_3.delete('0', 'end')
        self.entry_3.insert('0', domaintext)
        self.entry_3.pack(fill='both', side='top')

        self.sub_filename = ttk.Entry(frame_3, width=50)
        self.sub_filename.config(font='{Ubuntu} 12 {}')
        subdomainfile = 'subd file'
        self.sub_filename.delete('0', 'end')
        self.sub_filename.insert('0', subdomainfile)
        self.sub_filename.pack(fill='both', side='top')

        if self.the_scanner.is_alive():
            goorrun = "Running"
            self.the_scanner.join()
        else:
            goorrun = "Go"
        button_go = ttk.Button(frame_3, width=50, command=self.domain_scanner_go, text=goorrun)
        button_go.pack()

        print("Scanning: ", self.the_scanner.is_alive())
        frame_3.place(anchor='nw', relheight='1.0', relwidth='0.30', relx='0.0', rely='0.0', x='0', y='0')

        # Main widget
        self.mainwindow = frame_1

    def printthecontent(self):

        self.Text_detail.delete(1.0, "end")
        if self.the_scanner.is_alive():
            self.Text_detail.insert(tk.END, "\nScanning..")
        else:
            self.Text_detail.insert(tk.END, "\nScan completed..\n")

        with open("details.json", 'r') as json_details_loc:
            details_content_dict = json.load(json_details_loc)
            with open(str(details_content_dict['Detail of sessoin'][-1]["json_loc"]), 'r') as json_details:
                details_content_dict = json.load(json_details)
            for num, line in details_content_dict.items():
                self.Text_detail.insert(tk.END, "{}, {} \n".format(str(num + 1), line))

    def domain_scanner_go(self, ):
        self.Text_detail.insert(tk.END, "Scanning: ", self.the_scanner.is_alive())

        if self.the_scanner.is_alive():
            self.Text_detail.insert(tk.END, "\nScanner ALready running")
            return
        arg1, arg2 = self.entry_3.get(), self.sub_filename.get()
        scanner.main(str(arg1), int(arg2))
        self.Text_detail.delete(1.0, "end")
        self.Text_detail.insert(tk.END, self.entry_3.get() + "\n")
        self.printthecontent()
        return

    def run(self):
        self.mainwindow.mainloop()


def main():
    root = tk.Tk()
    app = NewguiApp(root)
    root.geometry("1500x900")
    style = ThemedStyle(root)
    style.set_theme("breeze")
    app.run()


if __name__ == '__main__':
    main()
