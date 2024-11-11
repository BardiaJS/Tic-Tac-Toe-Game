import customtkinter

# graphic declaring
app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("700*700")

button1 = customtkinter.CTkButton(app ,text="Single Player")
button1.grid(row=1, column=1, padx=20, pady=20)

button2 = customtkinter.CTkButton(app ,text="Multi player")
button2.grid(row=1, column=2, padx=20, pady=20)

app.mainloop()