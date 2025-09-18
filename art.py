"""
COMP 110, Lab Drawing

This module contains code to recreate dog and bunny artwork

Author: INSERT YOUR NAME AND EMAIL HERE
"""

import tkinter as tk

# add needed functions here

def main():
    """
    Main function to create dog and bunny artwork
    """

    root = tk.Tk()
    root.title("USD COMP110 dog and bunny artwork")

    canvas = tk.Canvas(root, width=500, height=500, bg="black")
    canvas.pack()

    #place function call(s) here

    root.mainloop()

if __name__ == "__main__":
    main()