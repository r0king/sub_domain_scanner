import cl_subd_scan as scanner
import multiprocessing as mp
import tkinter as tk
import sys
from tkinter import messagebox

class NewguiApp(tk.Frame):


    def __init__(self, master=None):

        global the_scanner
        the_scanner=mp.Process()
        self.text_details = tk.StringVar()
        self.goorrun=tk.StringVar()
        frame_1 = tk.Frame(master)
        frame_2 = tk.Frame(frame_1)
        scrollbar_2 = tk.Scrollbar(frame_2)
        scrollbar_2.config(orient='vertical')
        scrollbar_2.place(anchor='nw', relheight='1.0', x='0', y='0')
        
        button_6 = tk.Button(frame_2)
        button_6.config(text='Zenmap')
        button_6.place(anchor='nw', relx='0.08', rely='0.92', x='0', y='0')
        
        button_7 = tk.Button(frame_2)
        button_7.config(text='burp')
        button_7.place(anchor='nw', relx='0.27', rely='0.92', x='0', y='0')
        button_8 = tk.Button(frame_2)
        button_8.config(text='terninal')
        button_8.place(anchor='nw', relx='0.41', rely='0.92', x='0', y='0')
       
        details_scroll=tk.Scrollbar()
        text_details = 'details'
        self.Text_detail = tk.Text(frame_2)
        self.Text_detail.config(background='#78d9d9', font='{KacstScreen} 12 {}', height='10')
        self.Text_detail.config( width='50')
        self.Text_detail.place(anchor='nw', relheight='0.85', relwidth='1', relx='0.03', rely='0.03', x='0', y='0')
        self.Text_detail.insert(tk.END,"select domain")

        frame_2.config(height='200', width='200')
        frame_2.place(anchor='nw', relheight='1.0', relwidth='0.6', relx='0.3', rely='0.0', x='0', y='0')
        frame_3 = tk.Frame(frame_1)

        self.entry_3 = tk.Entry(frame_3, width=50)
        self.entry_3.config(font='{Ubuntu} 12 {}')
        domaintext = 'domain'
        self.entry_3.delete('0', 'end')
        self.entry_3.insert('0', domaintext)
        self.entry_3.pack(fill='both', side='top')

    

        self.sub_filename = tk.Entry(frame_3, width=50)
        self.sub_filename.config(font='{Ubuntu} 12 {}')
        subdomainfile = 'subd file'
        self.sub_filename.delete('0', 'end')
        self.sub_filename.insert('0', subdomainfile)
        self.sub_filename.pack(fill='both', side='top')


        if the_scanner.is_alive():
            goorrun="Running"
        else:
            goorrun="Go"
        button_go = tk.Button(frame_3, width=50, command=lambda:self.domain_scanner_go(),text=goorrun)
        button_go.pack()
        
        frame_3.config(height='200', width='200')
        frame_3.place(anchor='nw', relheight='1.0', relwidth='0.30', relx='0.0', rely='0.0', x='0', y='0')
        frame_1.config(height='500', relief='flat', width='900')
        frame_1.pack(side='top')

        # Main widget
        self.mainwindow = frame_1

    def printthecontent(self,details):
        details.insert(tk.END,"\nokworking")

    def domain_scanner_go(self, ):
        print("Scanning: ",the_scanner.is_alive())
        if the_scanner.is_alive():

            self.Text_detail.insert(tk.END,"\nScanner ALready running")
           
            return

        self.the_scanner=mp.Process(target=scanner.main(self.entry_3.get(),self.sub_filename.get()))
        the_scanner.start()

        print("Scanning: ",the_scanner.is_alive())

        self.Text_detail.delete(1.0,"end")
        self.Text_detail.insert(tk.END,self.entry_3.get()+"\n")
        self.Text_detail.insert(tk.END,"scan complete\n")
        self.printthecontent(self.Text_detail)
        return

    def run(self):
        self.mainwindow.mainloop()

def main():
    root = tk.Tk()
    app = NewguiApp(root)
    root.geometry('900x500')
    app.run()


if __name__ == '__main__':
    main()
