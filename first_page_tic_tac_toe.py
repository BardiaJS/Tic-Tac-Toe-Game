import customtkinter
import os


def single_player_callback():
    app.destroy()
    os.system('python single_player_tic_tac_toe.py')
    

def multi_player_callback():
    app.destroy()
    os.system('python multi_player_tic_tac_toe.py')
    

# graphic declaring
app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("700*700")

single_button = customtkinter.CTkButton(app ,text="Single Player" , command=single_player_callback)
single_button.grid(row=1, column=1, padx=20, pady=20)

multi_button = customtkinter.CTkButton(app ,text="Multi player" , command=multi_player_callback)
multi_button.grid(row=1, column=2, padx=20, pady=20)

app.mainloop()