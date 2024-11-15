from random import randrange
import customtkinter
import random






input_buttons = [[2 ,3 ,4 ] ,
                [5 , 6 ,7] ,
                [8 , 9 , 10]]

check_buttons = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9] 
def tic_tac_toe():
                returned_number = check_conditions(input_buttons)
                if(returned_number == -1):
                        while(check_buttons):
                                random_number = random.randint( 1 , 9)
                                if(random_number in check_buttons):
                                        if((random_number == 1)):
                                                check_buttons.remove(1)
                                                button1.configure(text="O") 
                                                input_buttons[0][0] = 0
                                                break
                                        elif((random_number == 2)):
                                                check_buttons.remove(2)
                                                button2.configure(text="O") 
                                                input_buttons[0][1] = 0
                                                break
                                        elif((random_number == 3)):
                                                check_buttons.remove(3)
                                                button3.configure(text="O") 
                                                input_buttons[0][2] = 0
                                                break
                                        elif((random_number == 4)):
                                                check_buttons.remove(4)
                                                button4.configure(text="O") 
                                                input_buttons[1][0] = 0
                                                break
                                        elif((random_number == 5)):
                                                check_buttons.remove(5)
                                                button5.configure(text="O") 
                                                input_buttons[1][1] = 0
                                                break
                                        elif((random_number == 6)):
                                                check_buttons.remove(6)
                                                button6.configure(text="O") 
                                                input_buttons[1][2] = 0
                                                break
                                        elif((random_number == 7)):
                                                check_buttons.remove(7)
                                                button7.configure(text="O") 
                                                input_buttons[2][0] = 0
                                                break
                                        elif((random_number == 8)):
                                                check_buttons.remove(8)
                                                button8.configure(text="O") 
                                                input_buttons[2][1] = 0
                                                break
                                        elif((random_number == 9)):
                                                check_buttons.remove(9)
                                                button9.configure(text="O") 
                                                input_buttons[2][2] = 0
                                                break
                                           
                
                        returned_number = check_conditions(input_buttons)
                        if(returned_number == 0):
                                label.configure(text="You lose!")
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
        check_buttons.remove(1)
        tic_tac_toe()
def button2_callback():
        button2.configure(text="*")
        input_buttons[0][1] = 1
        check_buttons.remove(2)
        tic_tac_toe()
def button3_callback():
        button3.configure(text="*")
        input_buttons[0][2] = 1
        check_buttons.remove(3)
        tic_tac_toe()
def button4_callback():
        button4.configure(text="*")
        input_buttons[1][0] = 1
        check_buttons.remove(4)
        tic_tac_toe()
def button5_callback():
        button5.configure(text="*")
        input_buttons[1][1] = 1
        check_buttons.remove(5)
        tic_tac_toe()
def button6_callback():
        button6.configure(text="*")
        input_buttons[1][2] = 1
        check_buttons.remove(6)
        tic_tac_toe()
def button7_callback():
        button7.configure(text="*")
        input_buttons[2][0] = 1
        check_buttons.remove(7)
        tic_tac_toe()
def button8_callback():
        button8.configure(text="*")
        input_buttons[2][1] = 1
        check_buttons.remove(8)
        tic_tac_toe()
def button9_callback():
        button9.configure(text="*")
        input_buttons[2][2] = 1
        check_buttons.remove(9)
        tic_tac_toe()
        
        
def button_reset_callback():
        global check_buttons
        global input_buttons        
        
        check_buttons.clear()
        check_buttons.append(1)
        check_buttons.append(2)
        check_buttons.append(3)
        check_buttons.append(4)
        check_buttons.append(5)
        check_buttons.append(6)
        check_buttons.append(7)
        check_buttons.append(8)
        check_buttons.append(9) 
       
        
        input_buttons.clear()
        input_buttons=[[] , [] , []]
        input_buttons[0].append(2)
        input_buttons[0].append(3)
        input_buttons[0].append(4)
        
        input_buttons[1].append(5)
        input_buttons[1].append(6)
        input_buttons[1].append(7)
        
        input_buttons[2].append(8)
        input_buttons[2].append(9)
        input_buttons[2].append(10)
        
        button1.configure(text=" ")
        button2.configure(text=" ")
        button3.configure(text=" ")
        button4.configure(text=" ")
        button5.configure(text=" ")
        button6.configure(text=" ")
        button7.configure(text=" ")
        button8.configure(text=" ")
        button9.configure(text=" ")     
        label.configure(text=" ")

        
    


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

button_reset = customtkinter.CTkButton(app ,text="Reset", command=button_reset_callback)
button_reset.grid(row=4, column=1, padx=20, pady=20)

label = customtkinter.CTkLabel(app, text=" ", fg_color="transparent")
label.grid(row=5, column=2, padx=20, pady=20)


app.mainloop()