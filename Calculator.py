import math as m
Userinputforoperation = input("Would You Like Add, Subtract Multipy or Divide? Enter a,s,m,d or sqrt exactly ")
X = float(input("Please enter your first number "))
if Userinputforoperation == "a":
    Y = float(input("Please enter your second number "))
    Final_Answer = round(X + Y,2) 
elif Userinputforoperation == "s":
    Y = float(input("Please enter your second number "))
    Final_Answer = round(X - Y,2)
elif Userinputforoperation == "m":
    Y = float(input("Please enter your second number "))
    Final_Answer = round(X * Y,2)
elif Userinputforoperation == "d":
    Y = float(input("Please enter your second number "))
    if Y != 0:
        Final_Answer = round(X/Y,2)
    else:
        Final_Answer = "Zero can not be executed"
elif Userinputforoperation == "sqrt":
    Final_Answer = round(m.sqrt(X),2)
else:
    print("Error Not Executable")    

print(Final_Answer)
