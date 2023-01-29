import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


class Notebook(tk.Frame):

    def __init__ (self, master):
        super().__init__(master)
        self.filename = None

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #Calls function and sets the size and centers master.
        self.size, self.center_width, self.center_height = self.win_size(screen_width, screen_height)
        master.geometry(f"{self.size}+{self.center_width}+{self.center_height}")

        #Frames:
        mainFrame = tk.Frame(master, width=450, height=550, bg='red')
        mainFrame.grid(row=1, column=0)
        
        #meant to be the size of the nav bar. 
        self.navFrame = tk.Frame(mainFrame, width = 450, height= 26, highlightthickness=1)
        self.navFrame.grid(row=0)

        #Holds I/O
        self.textFrame = tk.Frame(mainFrame, width=450, height=524, highlightthickness=1)
        self.textFrame.grid(row=1)

        #Widgets:

        #Initialize I/O.
        self.enter = tk.Text(self.textFrame, font=('sans', 13), borderwidth=0)

        #Open files, and grabs text in file and writes it in the Text widget.
        self.open_file = tk.Button(self.navFrame, text='Open', command= self.open_file) 

        #Saves the current text state, and overwrites what is on the file
        self.save = tk.Button(self.navFrame, text='Save', command= self.save_file)
        
        self.save_as = tk.Button(self.navFrame, text='Save As', command=self.save_as_file)
        
        #Calls run function and runs script if python file
        self.run_button = tk.Button(self.navFrame, text='Run', command=self.run)
       
        #Buttons for light and dark mode
        self.light_mode = tk.Button(self.navFrame, text='Light Mode', command=self.light)
        self.dark_mode = tk.Button(self.navFrame, text='Dark Mode', command=self.dark)


        self.ui_builder()

    #Place all UI on GUI. Purpose is to clean up __init__, and run mainloop
    def ui_builder(self):
        self.enter.place(x=0, y=0) 
        self.open_file.place(x=0, y=0)
        self.save.place(x=40, y=0)
        self.save_as.place(x=75, y=0)
        self.run_button.place(x=125, y=0)
        self.light_mode.place(x=308, y=0)
        self.dark_mode.place(x=380, y=0)

        self.startUp() #Checks what color the user previously used
        self.mainloop() #Updates and runs window


    #Opens file and displays file content in self.enter
    def open_file(self):
        
        self.filename = fd.askopenfilename()

        self.enter.delete('1.0', tk.END) #Clears any data on text widget (Doesn't delete file data)

        with open(self.filename, 'r') as file:
            lines = file.readlines()

            for i in range(0, len(lines)) : #Used to write info from file into self.enter for user to edit
                self.enter.insert(float(i)+1.0, lines[int(i)])


    def save_file(self):
        #If the filename does exist, then all the info willl be pulled from self.enter and then will overwrite everything on said file
        if self.filename:
            file_data = self.enter.get("1.0", tk.END)
            
            if self.filename:
                with open(self.filename, 'w') as file:
                    file.write(file_data)

        else:
            #If the file doesn't exist, then a new one is created. Default name is Notebook.txt
            fTypes = [('All Files', '*.*'), ('Text Document', '*.txt*'), ('Python Files', '*.py*')]

            #This pulls up the file explorer and allows the user to save the file, move it to a new folder, and change file type.
            self.filename = fd.asksaveasfile(initialfile='Notebook.txt', filetypes=fTypes, defaultextension = '.txt')

            file_data = self.enter.get("1.0", tk.END)

            with open(self.filename, 'w') as file:
                    file.write(file_data)


    #Create a seperate file with current info in self.enter
    def save_as_file(self):
        fTypes = [('All Files', '*.*'), ('Text Documents', '*.txt*'), ('Python Files', '*.py*')]

        self.filename = fd.asksaveasfile(initialfile='Notebook.txt', defaultextension='.txt', filetypes=fTypes) 

        file_data = self.enter.get("1.0", tk.END)

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
    


    def startUp(self):
        with open('usrChoice.txt', 'r') as file:
            uTheme = file.readlines()
                
        if 'light' in uTheme:
            self.light()
        else:
            self.dark()
        

    #Color configurations for dark mode
    def dark(self):
        self.navFrame.configure(bg='#202340', highlightbackground='#0f1126')
        self.textFrame.configure(bg='#202340', highlightbackground='#202340')

        self.enter.configure(highlightbackground='#202340', bg='#363959', fg='#ededf0')

        self.save.configure(bg='#363959', fg='white', highlightcolor='#202340')
        self.save_as.configure(bg='#363959', fg='white', highlightcolor='#202340')
        self.open_file.configure(bg='#363959', fg='white', highlightcolor='#202340')
        self.run_button.configure(bg='#363959', fg='white', highlightcolor='#202340')
        self.dark_mode.configure(bg='#363959', fg='white', highlightcolor='#202340')
        self.light_mode.configure(bg='#363959', fg='white', highlightcolor='#202340')    

        with open('usrChoice.txt', 'w') as file:
            file.write('dark')


    #Color configurations for light mode
    #This is also the default option
    def light(self):
        self.navFrame.configure(bg='#f9f9fa', highlightbackground='#0f1126')
        self.textFrame.configure(bg='#f9f9fa', highlightbackground='#202340')

        self.enter.configure(highlightbackground='#ededf0', bg='#d7d7db', fg='#0c0c0d')

        self.save.configure(bg='#f9f9fa', fg='#0c0c0d', highlightcolor='#ededf0')
        self.save_as.configure(bg='#f9f9fa', fg='#0c0c0d', highlightcolor='#ededf0')
        self.open_file.configure(bg='#f9f9fa', fg='#0c0c0d', highlightcolor='#ededf0')
        self.run_button.configure(bg='#f9f9fa', fg='#0c0c0d', highlightcolor='#ededf0')
        self.dark_mode.configure(bg='#f9f9fa', fg='#0c0c0d', highlightcolor='#ededf0')
        self.light_mode.configure(bg='#f9f9fa', fg='#0c0c0d', highlightcolor='#ededf0')    

        with open('usrChoice.txt', 'w') as file:
            file.write('light')


if __name__ == "__main__":
    #Initializes the GUI 

    root = tk.Tk()
    root.resizable(0,0)
    notebook = Notebook(root)
