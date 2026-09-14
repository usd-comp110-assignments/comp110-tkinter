"""
COMP 110 Lab: Tkinter Drawing

This module contains code to create mutliple rainbows.

Author: INSERT YOUR NAME AND EMAIL HERE
"""

import tkinter as tk

def draw_rainbow(target_canvas):
    """
    To Do: Fix this docstring
    """
    
    pass # To Do: Delete this line and fill in the code to draw the rainbow


def main():
    """
    Main function to create rainbows
    """

    root = tk.Tk()
    root.title("USD COMP110 Rainbows")

    canvas = tk.Canvas(root, width=450, height=150, bg="white")
    canvas.pack()

    # To Do: Add your call(s) to draw_rainbow below this line.

    root.mainloop()


if __name__ == "__main__":
    main()
