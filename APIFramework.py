import tkinter as tk
from tkinter import simpledialog
import shutil
import os


class GUIFramework:
    def __init__(self, root):
        self.root = root
        self.root.title("API Framework")
        self.root.geometry("500x500")

        create_model_label = tk.Label(root, text="Create")
        create_model_label.pack(padx=30, pady=30)

        # Create Model
        create_model_button = tk.Button(
            root,
            text="Create Model",
            command=self.create_model_popup,
            height=2,
            width=5,
        )
        create_model_button.pack(padx=10, pady=10)

        create_view_button = tk.Button(
            root, text="Create View", command=self.create_view_popup, height=2, width=5
        )
        create_view_button.pack(padx=10, pady=10)

    def create_model_popup(self):
        model_name = simpledialog.askstring("Create Model", "Enter Model Name:")
        if not model_name:
            return

        model_path = f"APP/model/{model_name}.py"
        if os.path.exists(model_path):
            tk.messagebox.showwarning(  # type: ignore
                "File Exists", f"File '{model_name}.py' already exists."
            )
            return

        shutil.copy("APP/template/model.py", model_path)
        tk.messagebox.showinfo("Success", f"Model '{model_name}' created.")  # type: ignore

    def create_view_popup(self):
        view_name = simpledialog.askstring("Create View", "Enter View Name:")
        if not view_name:
            return

        view_path = f"web/view/{view_name}.html"
        if os.path.exists(view_path):
            tk.messagebox.showwarning(  # type: ignore
                "File Exists", f"File '{view_name}.html' already exists."
            )
            return

        shutil.copy("APP/template/view.html", view_path)
        tk.messagebox.showinfo("Success", f"View '{view_name}' created.")  # type: ignore


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIFramework(root)
    root.mainloop()
