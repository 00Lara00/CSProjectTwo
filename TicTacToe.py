from tkinter import *
from tkinter import messagebox

base = Tk()
base.title("TicTacToe")

"""
Allows for choosing of spots
"""

clicked = True
count = 0
messagebox.showinfo('TicTacToe','X Starts' )
x_win = 0
o_win = 0

"""
disables buttons; makes sure they are selected at start of game
"""

def disable_buttons():
    spot_one.config(state=DISABLED)
    spot_two.config(state=DISABLED)
    spot_three.config(state=DISABLED)
    spot_four.config(state=DISABLED)
    spot_five.config(state=DISABLED)
    spot_six.config(state=DISABLED)
    spot_seven.config(state=DISABLED)
    spot_eight.config(state=DISABLED)
    spot_nine.config(state=DISABLED)

"""
Checks for game winner
"""

def win_calculation():
    global winner
    winner = False
    """
    Checking for X win
    """

    if spot_one['text'] == 'X' and spot_two['text'] == 'X' and spot_three['text'] == 'X':
        global x_win
        spot_one.config(bg='green')
        spot_two.config(bg='green')
        spot_three.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()

    elif spot_four['text'] == 'X' and spot_five['text'] == 'X' and spot_six['text'] == 'X':
        spot_four.config(bg='green')
        spot_five.config(bg='green')
        spot_six.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()

    elif spot_seven['text'] == 'X' and spot_eight['text'] == 'X' and spot_nine['text'] == 'X':
        spot_seven.config(bg='green')
        spot_eight.config(bg='green')
        spot_nine.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()

    elif spot_one['text'] == 'X' and spot_four['text'] == 'X' and spot_seven['text'] == 'X':
        spot_one.config(bg='green')
        spot_four.config(bg='green')
        spot_seven.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()

    elif spot_two['text'] == 'X' and spot_five['text'] == 'X' and spot_eight['text'] == 'X':
        spot_two.config(bg='green')
        spot_five.config(bg='green')
        spot_eight.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()

    elif spot_three['text'] == 'X' and spot_six['text'] == 'X' and spot_nine['text'] == 'X':
        spot_three.config(bg='green')
        spot_six.config(bg='green')
        spot_nine.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()

    elif spot_one['text'] == 'X' and spot_five['text'] == 'X' and spot_nine['text'] == 'X':
        spot_one.config(bg='green')
        spot_five.config(bg='green')
        spot_nine.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()

    elif spot_three['text'] == 'X' and spot_five['text'] == 'X' and spot_seven['text'] == 'X':
        spot_three.config(bg='green')
        spot_five.config(bg='green')
        spot_seven.config(bg='green')
        winner = True
        x_win += 1
        messagebox.showinfo('TicTacToe', 'Player X wins!')
        disable_buttons()
"""
Checks for O winner
"""

    if spot_one['text'] == 'O' and spot_two['text'] == 'O' and spot_three['text'] == 'O':
        global o_win
        spot_one.config(bg='green')
        spot_two.config(bg='green')
        spot_three.config(bg='green')
        winner = True
        o_win += 1
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()

    elif spot_four['text'] == 'O' and spot_five['text'] == 'O' and spot_six['text'] == 'O':
        spot_four.config(bg='green')
        spot_five.config(bg='green')
        spot_six.config(bg='green')
        winner = True
        o_win += 1
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()

    elif spot_seven['text'] == 'O' and spot_eight['text'] == 'O' and spot_nine['text'] == 'O':
        spot_seven.config(bg='green')
        spot_eight.config(bg='green')
        spot_nine.config(bg='green')
        winner = True
        o_win += 1
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()

    elif spot_one['text'] == 'O' and spot_four['text'] == 'O' and spot_seven['text'] == 'O':
        spot_one.config(bg='green')
        spot_four.config(bg='green')
        spot_seven.config(bg='green')
        o_win += 1
        winner = True
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()

    elif spot_two['text'] == 'O' and spot_five['text'] == 'O' and spot_eight['text'] == 'O':
        spot_two.config(bg='green')
        spot_five.config(bg='green')
        spot_eight.config(bg='green')
        winner = True
        o_win += 1
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()

    elif spot_three['text'] == 'O' and spot_six['text'] == 'O' and spot_nine['text'] == 'O':
        spot_three.config(bg='green')
        spot_six.config(bg='green')
        spot_nine.config(bg='green')
        winner = True
        o_win += 1
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()

    elif spot_one['text'] == 'O' and spot_five['text'] == 'O' and spot_nine['text'] == 'O':
        spot_one.config(bg='green')
        spot_five.config(bg='green')
        spot_nine.config(bg='green')
        winner = True
        o_win += 1
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()

    elif spot_three['text'] == 'O' and spot_five['text'] == 'O' and spot_seven['text'] == 'O':
        spot_three.config(bg='green')
        spot_five.config(bg='green')
        spot_seven.config(bg='green')
        winner = True
        o_win += 1
        messagebox.showinfo('TicTacToe', 'Player O wins!')
        disable_buttons()
"""
Checks for tie
"""
    if count == 9 and winner == False:
        messagebox.showinfo('TicTacToe', 'Game has ended in a tie')
        disable_buttons()

"""
Assigns X or O to button clicked
"""

def button_click(button):
    global clicked, count
    if button['text'] == ' ' and clicked == True:
        button['text'] = 'X'
        clicked = False
        count += 1
        win_calculation()
    elif button['text'] == ' ' and clicked == False:
        button['text'] = 'O'
        clicked = True
        count += 1
        win_calculation()
    else:
        messagebox.showerror("TicTacToe", 'Spot has been selected, choose a different spot')

"""
Resets the game 
"""

def reset():
    global spot_one, spot_two, spot_three, spot_four, spot_five, spot_six, spot_seven, spot_eight, spot_nine
    global clicked, count
    clicked = True
    count = 0
    spot_one = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace', command=lambda: button_click(spot_one))
    spot_one.grid(row=0, column=0)
    spot_two = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace', command=lambda: button_click(spot_two))
    spot_two.grid(row=0, column=1)
    spot_three = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace',
                        command=lambda: button_click(spot_three))
    spot_three.grid(row=0, column=2)

    spot_four = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace',
                       command=lambda: button_click(spot_four))
    spot_four.grid(row=1, column=0)
    spot_five = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace',
                       command=lambda: button_click(spot_five))
    spot_five.grid(row=1, column=1)
    spot_six = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace', command=lambda: button_click(spot_six))
    spot_six.grid(row=1, column=2)

    spot_seven = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace',
                        command=lambda: button_click(spot_seven))
    spot_seven.grid(row=2, column=0)
    spot_eight = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace',
                        command=lambda: button_click(spot_eight))
    spot_eight.grid(row=2, column=1)
    spot_nine = Button(base, text=' ', height=3, width=6, bg='SystemButtonFace',
                       command=lambda: button_click(spot_nine))
    spot_nine.grid(row=2, column=2)

"""
Sets up the menu of the game
"""

menu = Menu(base)
base.config(menu=menu)

options = Menu(menu)
menu.add_cascade(label='Options', menu=options)
options.add_command(label='Game Reset', command=reset)
reset()
base.mainloop()
