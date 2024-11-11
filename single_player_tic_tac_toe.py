from random import randrange
import customtkinter


input_buttons = [[2 ,3 ,4 ] ,
                [5 , 6 ,7] ,
                [8 , 9 , 10]]

check_buttons = [False , False , False , False , False , False , False , False , False] 
def tic_tac_toe():
                returned_number = check_conditions(input_buttons)
                if(returned_number == -1):
                        while(True):
                                random_number_row = randrange(3)
                                random_number_column = randrange(3)
                                random_created_number = input_buttons[random_number_row][random_number_column]
                                if((random_created_number != 1) and (random_created_number != 0)):
                                        if((random_created_number == input_buttons[0][0]) and (check_buttons[0] != True)):
                                                button1.configure(text="O") 
                                                check_buttons[0] = True
                                        elif((random_created_number == input_buttons[0][1]) and (check_buttons[1] != True)):
                                                button2.configure(text="O") 
                                                check_buttons[1] = True
                                        elif((random_created_number == input_buttons[0][2]) and (check_buttons[2] != True)):
                                                button3.configure(text="O") 
                                                check_buttons[2] = True
                                        elif((random_created_number == input_buttons[1][0]) and (check_buttons[3] != True)):
                                                button4.configure(text="O") 
                                                check_buttons[3] = True
                                        elif((random_created_number == input_buttons[1][1]) and (check_buttons[4] != True)):
                                                button5.configure(text="O") 
                                                check_buttons[4] = True
                                        elif((random_created_number == input_buttons[1][2]) and (check_buttons[5] != True)):
                                                button6.configure(text="O") 
                                                check_buttons[5] = True
                                        elif((random_created_number == input_buttons[2][0]) and (check_buttons[6] != True)):
                                                button7.configure(text="O")
                                                check_buttons[6] = True 
                                        elif((random_created_number == input_buttons[2][1]) and (check_buttons[7] != True)):
                                                button8.configure(text="O") 
                                                check_buttons[7] = True
                                        elif((random_created_number == input_buttons[2][2]) and (check_buttons[8] != True)):
                                                button9.configure(text="O") 
                                                check_buttons[8] = True
                                        break   
                
                        returned_number = check_conditions(input_buttons)
                else:
                        if(returned_number == 0):
                                label.configure(text="You lose!")
                        elif(returned_number == 1):
                                label.configure(text="You Win!")
                        else:
                                label.configure(text="Draw!")
        

            
            
        
        
        
def check_conditions(input_buttons):
        
        if(input_buttons[0][0] == input_buttons[0][1] == input_buttons[0][2]):
            print ("The games is over!")
            if(input_buttons[0][0] == 0 ):
                    return 0
            else:
                    return 1
            
            
            
        elif(input_buttons[1][0] == input_buttons[1][1] == input_buttons[1][2]):
                print ("The games is over!")
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
           
        elif(input_buttons[2][0] == input_buttons[2][1] == input_buttons[2][2]):
                print ("The games is over!")
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][0] == input_buttons[1][0] == input_buttons[2][0]):
                print ("The games is over!")
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][1] == input_buttons[1][1] == input_buttons[2][1]):
                print ("The games is over!")
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][2] == input_buttons[1][2] == input_buttons[2][2]):
                print ("The games is over!")
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][0] == input_buttons[1][1] == input_buttons[2][2]):
                print ("The games is over!")
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][2] == input_buttons[1][1] == input_buttons[2][0]):
                print ("The games is over!")
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        else:
                return -1
                


























# button functions

def button1_callback():
        button1.configure(text="*") 
        input_buttons[0][0] = 1
        check_buttons[0] = True
        tic_tac_toe()
def button2_callback():
        button2.configure(text="*")
        input_buttons[0][1] = 1
        check_buttons[1] = True
        tic_tac_toe()
def button3_callback():
        button3.configure(text="*")
        input_buttons[0][2] = 1
        check_buttons[2] = True
        tic_tac_toe()
def button4_callback():
        button4.configure(text="*")
        input_buttons[1][0] = 1
        check_buttons[3] = True
        tic_tac_toe()
def button5_callback():
        button5.configure(text="*")
        input_buttons[1][1] = 1
        check_buttons[4] = True
        tic_tac_toe()
def button6_callback():
        button6.configure(text="*")
        input_buttons[1][2] = 1
        check_buttons[5] = True
        tic_tac_toe()
def button7_callback():
        button7.configure(text="*")
        input_buttons[2][0] = 1
        check_buttons[6] = True
        tic_tac_toe()
def button8_callback():
        button8.configure(text="*")
        input_buttons[2][1] = 1
        check_buttons[7] = True
        tic_tac_toe()
def button9_callback():
        button9.configure(text="*")
        input_buttons[2][2] = 1
        check_buttons[8] = True
        tic_tac_toe()
    


# graphical interface declaring
app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("700*700")
button1 = customtkinter.CTkButton(app ,text=" ", command=button1_callback)
button1.grid(row=1, column=1, padx=20, pady=20)

button2 = customtkinter.CTkButton(app ,text=" ", command=button2_callback)
button2.grid(row=1, column=2, padx=20, pady=20)

button3 = customtkinter.CTkButton(app ,text=" ", command=button3_callback)
button3.grid(row=1, column=3, padx=20, pady=20)

button4 = customtkinter.CTkButton(app ,text=" ", command=button4_callback)
button4.grid(row=2, column=1, padx=20, pady=20)

button5 = customtkinter.CTkButton(app ,text=" ", command=button5_callback)
button5.grid(row=2, column=2, padx=20, pady=20)

button6 = customtkinter.CTkButton(app ,text=" ", command=button6_callback)
button6.grid(row=2, column=3, padx=20, pady=20)

button7 = customtkinter.CTkButton(app ,text=" ", command=button7_callback)
button7.grid(row=3, column=1, padx=20, pady=20)

button8 = customtkinter.CTkButton(app ,text=" ", command=button8_callback)
button8.grid(row=3, column=2, padx=20, pady=20)

button9 = customtkinter.CTkButton(app ,text=" ", command=button9_callback)
button9.grid(row=3, column=3, padx=20, pady=20)

label = customtkinter.CTkLabel(app, text=" ", fg_color="transparent")
label.grid(row=4, column=2, padx=20, pady=20)


app.mainloop()