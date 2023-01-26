import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

#Heres a guide for help: https://realpython.com/python-gui-tkinter/

#TODO: MAKE A LIGHT AND DARK MODE:
# colors: https://design.firefox.com/photon/visuals/color.html

 #TODO: make a function called UI builder to get stuff out of __init__
        #Initialize stuff in init and functionality should be in the UI func

class Notebook(tk.Frame):

    def __init__ (self, master):
        super().__init__(master)

        self.filename = None
        self.open_called = False

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #Calls function and sets the size and centers master.
        self.size, self.center_width, self.center_height = self.win_size(screen_width, screen_height)
        master.geometry(f"{self.size}+{self.center_width}+{self.center_height}")

        #Frames:

        #Size of gui
        mainFrame = tk.Frame(master, width=450, height=550, bg='red')
        mainFrame.grid(row=1, column=0)
        
        #meant to be the size of the nav bar. 
        navFrame = tk.Frame(mainFrame, width = 450, height= 26, highlightthickness=1)
        navFrame.grid(row=0)

        #Holds I/O
        textFrame = tk.Frame(mainFrame, width=450, height=524, highlightthickness=1)
        textFrame.grid(row=1)

        #Widgets:

        #Initialize I/O.
        self.enter = tk.Text(textFrame, font=('sans', 13), borderwidth=0)
        self.enter.place(x=0, y=0)

        #Open files, and grabs text in file and writes it in the Text widget.
        self.open = tk.Button(navFrame, text='Open', command= self.open_file) 
        self.open.place(x=0, y=0)

        #Saves the current text state, and overwrites what is on the file
        self.save_as = tk.Button(navFrame, text='Save As', command= self.save_file)
        self.save_as.place(x=40, y=0)

        #Calls run function and runs script if python file
        self.run_button = tk.Button(navFrame, text='Run', command=self.run)
        self.run_button.place(x=91, y=0)


        self.light_mode = tk.Button(navFrame, text='Light Mode', command=None)
        #TODO: ADD LIGHT MODE

        self.dark_mode = tk.Button(navFrame, text='Dark Mode', command=None)
        #TODO: ADD DARK MODE


        #Styling and Customization:
        
        navFrame.configure(bg='#202340', highlightbackground='#0f1126')
        textFrame.configure(bg='#202340', highlightbackground='#202340')

        self.enter.configure(highlightbackground='#202340', bg='#363959', fg='#ededf0')

        self.save_as.configure(bg='#363959', fg='white', highlightcolor='#202340')
        self.open.configure(bg='#363959', fg='white', highlightcolor='#202340')
        self.run_button.configure(bg='#363959', fg='white', highlightcolor='#202340')

        self.master.configure()


        #TODO: Customize those framees, as well as the widgets

        #TODO: create a function that can switch between light and dark mode.



        self.mainloop() #Updates and runs window


    #Opens file and displays file content in self.enter
    def open_file(self):

        self.filename = fd.askopenfilename()

        self.enter.delete('1.0', tk.END) #Clears any data on text widget (Doesn't delete file data)

        with open(self.filename, 'r') as file:
            lines = file.readlines()

            for i in range(0, len(lines)) :
                self.enter.insert(float(i)+1.0, lines[int(i)])

            self.open_called = True


    #Saves info to file by overwriting info present -- requires open_file being run.
    def save_file(self):
        file_data = self.enter.get("1.0", tk.END)
        
        if self.filename:
            with open(self.filename, 'w') as file:
                file.write(file_data)


    #Runs python files
    def run(self):
        if self.filename.endswith('.py'):
            exec(open(self.filename).read()) 

            #if VScode is open, runs in VScode.
            #To open cmd, run file outside of cmd

        else:
            from tkinter import messagebox

            #Message box will pop up if file type isn't .py
            messagebox.showerror('Notebook', 'Error: file type not supported')        


    #Sets the size of root and centers master on startup
    def win_size(self, screen_width, screen_height):
        ROOT_WIDTH, ROOT_HEIGHT = 450, 550 #Desired size of the window

        #Math to center the window
        center_width = int(screen_width/2 - ROOT_WIDTH/2)
        center_height = int(screen_height/2 - ROOT_HEIGHT/2)

        size = f"{str(ROOT_WIDTH)}x{str(ROOT_HEIGHT)}" #Sets the root width and height

        return size, center_width, center_height


if __name__ == "__main__":

    root = tk.Tk()
    notebook = Notebook(root)

    notebook.mainloop()
