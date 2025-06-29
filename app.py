import tkinter as tk

from ui.index import Index


def main():
    root = tk.Tk()
    root.wm_title("Ringerous")
    index = Index(root)
    index.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
