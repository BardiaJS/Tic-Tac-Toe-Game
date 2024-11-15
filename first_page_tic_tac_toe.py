import customtkinter
import single_player_tic_tac_toe
import multi_player_tic_tac_toe

def single_button_clicked():
    single_player_tic_tac_toe.main


def multi_button_clicked():
    with open('multi_player_tic_tac_toe.py') as f:
        exec(f.read())


# graphic declaring
app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("700*700")

single_button = customtkinter.CTkButton(app ,text="Single Player" , command=single_button_clicked)
single_button.grid(row=1, column=1, padx=20, pady=20)

multi_button = customtkinter.CTkButton(app ,text="Multi player" , command=multi_button_clicked)
multi_button.grid(row=1, column=2, padx=20, pady=20)

app.mainloop()