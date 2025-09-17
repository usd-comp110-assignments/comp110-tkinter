"""
COMP 110, Lab Drawing

This module contains code to create mutliple bullseye for an archery range

Author: INSERT YOUR NAME AND EMAIL HERE
"""

import tkinter as tk

def bullseye(canvas,x,y):
    """
    fix this docstring
    """
    #put your code here and delete the pass
    pass

def main():
    """
    Main function to create bullseyes
    """

    root = tk.Tk()
    root.title("USD COMP110 Bullseye")

    canvas = tk.Canvas(root, width=450, height=150, bg="white")
    canvas.pack()

    #place function call(s) here


    root.mainloop()

if __name__ == "__main__":
    main()