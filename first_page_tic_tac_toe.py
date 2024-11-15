import customtkinter




# graphic declaring
app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("700*700")

single_button = customtkinter.CTkButton(app ,text="Single Player" )
single_button.grid(row=1, column=1, padx=20, pady=20)

multi_button = customtkinter.CTkButton(app ,text="Multi player" )
multi_button.grid(row=1, column=2, padx=20, pady=20)

app.mainloop()