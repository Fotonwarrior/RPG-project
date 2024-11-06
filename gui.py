import tkinter as tk 
#import tycoongame_objects as tg

appname = "Capitalist Tycoon"

class gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(appname)
        res = str(self.root.winfo_screenwidth())+ "x" + str(self.root.winfo_screenheight())
        self.root.geometry(res)
        self.company = None
        #self.input = entryfield(self.root, ['a', 'b', 'c'], self.process_inputs)
        #self.root.mainloop()

    def process_inputs(self, inputs):
        self.temp_inputs = inputs
        print(self.temp_inputs)

class entryfield:
    def __init__(self, master, entries, callback):
        self.frame = tk.Frame(master)
        self.inputs = []
        self.callback = callback
        for entry in entries:
            innerframe = tk.Frame(self.frame)
            tk.Label(innerframe, text=f'Please enter {entry}').pack(side='left')
            input = tk.Entry(innerframe)
            self.inputs.append(input)
            input.pack(side='left')
            innerframe.pack()
        tk.Button(self.frame, text='submit', command=self.finalize).pack()
        self.frame.pack()

    def finalize(self):
        inputs = [entry.get() for entry in self.inputs]
        self.callback(inputs)
        self.frame.destroy()
        
#def instantiate()    

#gui()