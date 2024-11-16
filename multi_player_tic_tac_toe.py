from random import randrange
import customtkinter




input_buttons = [[2 ,3 ,4 ] ,
                [5 , 6 ,7] ,
                [8 , 9 , 10]]
which_user = 1
check_buttons = [False , False , False , False , False , False , False , False , False] 
def tic_tac_toe():
                returned_number = check_conditions(input_buttons)
                if(returned_number == -1):
                        is_checked_checkbuttons = 0
                        for i in check_buttons:
                                if( i == True):
                                        is_checked_checkbuttons += 1
                        if(is_checked_checkbuttons == 9):
                                label.configure(text="Draw!")
                                        
                else:
                        if(returned_number == 0):
                                label.configure(text="User B wins!")
                        elif(returned_number == 1):
                                label.configure(text="User A wins!")
                        elif(returned_number == -1):
                                label.configure(text="Draw!")
        

            
           
        
        
        
def check_conditions(input_buttons):
        
        if(input_buttons[0][0] == input_buttons[0][1] == input_buttons[0][2]):
            if(input_buttons[0][0] == 0 ):
                    return 0
            else:
                    return 1
            
            
            
        elif(input_buttons[1][0] == input_buttons[1][1] == input_buttons[1][2]):
                if(input_buttons[1][0] == 0 ):
                        return 0
                else:
                        return 1
                
           
        elif(input_buttons[2][0] == input_buttons[2][1] == input_buttons[2][2]):
    
                if(input_buttons[2][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][0] == input_buttons[1][0] == input_buttons[2][0]):
 
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][1] == input_buttons[1][1] == input_buttons[2][1]):

                if(input_buttons[0][1] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][2] == input_buttons[1][2] == input_buttons[2][2]):
  
                if(input_buttons[0][2] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][0] == input_buttons[1][1] == input_buttons[2][2]):
 
                if(input_buttons[0][0] == 0 ):
                        return 0
                else:
                        return 1
                
        elif(input_buttons[0][2] == input_buttons[1][1] == input_buttons[2][0]):

                if(input_buttons[0][2] == 0 ):
                        return 0
                else:
                        return 1
                
        else:
                return -1
                


























# button functions

def button1_callback():
        global which_user
        if(which_user == 1):
                
                if(check_buttons[0] == False):
                        button1.configure(text="*")
                        input_buttons[0][0] = 1 
                        check_buttons[0] = True
                else:
                        label.configure(text="You can't choose that button!")
                which_user = 0
        else:
                if(check_buttons[0] == False):
                        button1.configure(text="O")
                        input_buttons[0][0] = 0 
                        check_buttons[0] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
               
        tic_tac_toe()
def button2_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[1] == False):
                        button2.configure(text="*")
                        input_buttons[0][1] = 1 
                        check_buttons[1] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[1] == False):
                        button2.configure(text="O")
                        input_buttons[0][1] = 0
                        check_buttons[1] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
def button3_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[2] == False):
                        button3.configure(text="*")
                        input_buttons[0][2] = 1 
                        check_buttons[2] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[2] == False):
                        button3.configure(text="O")
                        input_buttons[0][2] = 0
                        check_buttons[2] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
def button4_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[3] == False):
                        button4.configure(text="*")
                        input_buttons[1][0] = 1 
                        check_buttons[3] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[3] == False):
                        button4.configure(text="O")
                        input_buttons[1][0] = 0
                        check_buttons[3] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
def button5_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[4] == False):
                        button5.configure(text="*")
                        input_buttons[1][1] = 1 
                        check_buttons[4] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[4] == False):
                        button5.configure(text="O")
                        input_buttons[1][1] = 0
                        check_buttons[4] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
def button6_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[5] == False):
                        button6.configure(text="*")
                        input_buttons[1][2] = 1 
                        check_buttons[5] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[5] == False):
                        button6.configure(text="O")
                        input_buttons[1][2] = 0
                        check_buttons[5] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
def button7_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[6] == False):
                        button7.configure(text="*")
                        input_buttons[2][0] = 1 
                        check_buttons[6] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[6] == False):
                        button7.configure(text="O")
                        input_buttons[2][0] = 0
                        check_buttons[6] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
def button8_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[7] == False):
                        button8.configure(text="*")
                        input_buttons[2][1] = 1 
                        check_buttons[7] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[7] == False):
                        button8.configure(text="O")
                        input_buttons[2][1] = 0
                        check_buttons[7] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
def button9_callback():
        global which_user
        if(which_user == 1):
                if(check_buttons[8] == False):
                        button9.configure(text="*")
                        input_buttons[2][2] = 1 
                        check_buttons[8] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 0
        else:
                if(check_buttons[8] == False):
                        button9.configure(text="O")
                        input_buttons[2][2] = 0
                        check_buttons[8] = True
                else:
                        label.configure(text="You can't choose that button!")

                which_user = 1
        tic_tac_toe()
        
        

def button_reset_callback():
        global input_buttons
        global which_user
        global check_buttons   
        
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

        
        
        
        
        
        
        
        
          
        
        input_buttons.clear()
        input_buttons =[[] , 
                        [] ,
                        []]
        input_buttons[0].append(2)
        input_buttons[0].append(3)
        input_buttons[0].append(4)
        input_buttons[1].append(5)
        input_buttons[1].append(6)
        input_buttons[1].append(7)
        input_buttons[2].append(8)
        input_buttons[2].append(9)
        input_buttons[2].append(10)
        
        which_user = 1
        
        check_buttons.clear()
        
        for i in range(0 , 9):
                check_buttons.append(False)
                i +=1

# graphical interface declaring
app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("800*800")
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
label.grid(row=4, column=2, padx=20, pady=20)


app.mainloop()