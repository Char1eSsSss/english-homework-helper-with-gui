import tkinter as tk
from tkinter import messagebox

# TODO: use ttk to beautify tk gui (optional: just for better styling, requires 'ttkbootstrap' package)
'''import ttkbootstrap as ttk '''


class EnglishHomeworkHelperApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        padding = 5 # Padding value
        self.school_label = tk.Label(self, text="School:")
        self.school_label.grid(row=0, column=0, padx=padding, pady=padding)
        self.school_entry = tk.Entry(self, width=30)
        self.school_entry.grid(row=0, column=1, padx=padding, pady=padding)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=1, column=0, padx=padding, pady=padding)
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.grid(row=1, column=1, padx=padding, pady=padding)

        self.passwd_label = tk.Label(self, text="Password:")
        self.passwd_label.grid(row=2, column=0, padx=padding, pady=padding)
        self.passwd_entry = tk.Entry(self, show="*", width=30)
        self.passwd_entry.grid(row=2, column=1, padx=padding, pady=padding)

        self.api_url_label = tk.Label(self, text="API URL:")
        self.api_url_label.grid(row=3, column=0, padx=padding, pady=padding)
        self.api_url_entry = tk.Entry(self, width=30)
        self.api_url_entry.grid(row=3, column=1, padx=padding, pady=padding)

        self.api_key_label = tk.Label(self, text="API Key:")
        self.api_key_label.grid(row=4, column=0, padx=padding, pady=padding)
        self.api_key_entry = tk.Entry(self, show="*", width=30)
        self.api_key_entry.grid(row=4, column=1, padx=padding, pady=padding)

        self.modelname_label = tk.Label(self, text="Model:")
        self.modelname_label.grid(row=5, column=0, padx=padding, pady=padding)
        self.modelname_entry = tk.Entry(self, width=30)
        self.modelname_entry.grid(row=5, column=1, padx=padding, pady=padding)

        self.GUICheckVar = tk.BooleanVar(value=True)
        self.gui_option_checkbutton = tk.Checkbutton(self, text="GUI Browser", variable=self.GUICheckVar)
        self.gui_option_checkbutton.grid(row=6, column=0, padx=padding, pady=padding)

        self.start_button = tk.Button(self, text="Start Configuration", width=20, command=self.writeConfig)
        self.start_button.grid(row=6, column=1, padx=padding, pady=padding, sticky="e")
        
        #TODO: leave configured fields unchanged instead of overwriting with defaults
        self.hint_label = tk.Label(self, text="* Fields you didn't fill will become default values.\nWith all fields empty, no operation will be done.",
                                    fg="red", font=("Arial", 9, "bold"))
        self.hint_label.grid(row=7, column=0, columnspan=2, padx=padding, pady=padding)

    def writeConfig(self):
        if not self.school_entry.get() and not self.username_entry.get() and not self.passwd_entry.get() \
           and not self.api_url_entry.get() and not self.api_key_entry.get() and not self.modelname_entry.get():
            self.on_closing(messagebox_type="type1")
            
        else:
            with open("local/config.json", "w", encoding="utf-8") as f:
                f.write(
                '{\n'
                '    "browser": {\n'
                f'        "headless": {"false" if self.GUICheckVar.get() == True else "true"}\n'
                '    },\n'
                '    "credentials": {\n'
                '        "default": 0,\n'
                '        "all": [\n'
                '            {\n'
                f'                "school": "{self.school_entry.get() if self.school_entry.get() else "default_school"}",\n'
                f'                "username": "{self.username_entry.get() if self.username_entry.get() else "default_username"}",\n'
                f'                "password": "{self.passwd_entry.get() if self.passwd_entry.get() else "default_password"}"\n'
                '            }\n'
                '        ]\n'
                '    },\n'
                '    "ai_client": {\n'
                '        "default": 0,\n'
                '        "all": [\n'
                '            {\n'
                f'                "api_url": "{self.api_url_entry.get() if self.api_url_entry.get() else "default_api_url"}",\n'
                f'                "api_key": "{self.api_key_entry.get() if self.api_key_entry.get() else "default_api_key"}",\n'
                f'                "model": "{self.modelname_entry.get() if self.modelname_entry.get() else "default_model"}"\n'
                '            }\n'
                '        ]\n'
                '    },\n'
                '    "whisper": {\n'
                '        "model": "large",\n'
                '        "device": "auto",\n'
                '        "in_memory": true\n'
                '    },\n'
                '    "telegram_bot_token": "your_telegram_bot_token"\n'
                '}'
                )
            self.on_closing(messagebox_type="type2")
            
    def on_closing(self, messagebox_type):
        if messagebox_type == "type1":
            if messagebox.askyesno("Confirm", "It seems you didn't fill any fields. Are you sure to proceed?"):
                self.master.destroy()
        elif messagebox_type == "type2":
            messagebox.showinfo("Info", "Configuration saved successfully.")
            self.master.destroy()

'''cli/make_gui()'''
# root = tk.Tk()
# root.title("English Homework Helper Configurator")
# root.geometry("350x280")
# root.resizable(False, False)
# root.attributes("-topmost", True)

# app = EnglishHomeworkHelperApp(master=root)
# app.mainloop()