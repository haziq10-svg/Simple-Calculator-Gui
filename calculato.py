from tkinter import  *

root = Tk()
root.geometry('600x600')
root.title("Simple Calculator")

root.configure(bg = 'light blue')

label_font = ("Times New Roman" , 15)

bg = 'light blue'


text = Label(root ,text = "Welcome To Simple Calulator" ,font= ("Times New Roman" , 18) , bg = bg)
text.pack(pady = 5)

text1 = Label(root , text = "Enter 1st Number" , font = label_font , bg = bg)
text1.pack(pady = 5)

number1 = Entry(root , width = 20 )
number1.get()
number1.pack(pady=5)

text2 = Label(root ,text = "Enter 2nd Number" ,bg = bg , font = label_font)
text2.pack(pady = 5)

number2 =Entry(root , width = 20 )
number2.pack(pady = 5)
number2.get()

text3 = Label(root , text = "Enter Operation", bg = bg , font = label_font)
text3.pack(pady=5)

operation = Entry(root , width = 20)
operation.pack(pady = 5)
operation.get()


def function():
    a =float(number1.get()) #to make it easier
    b =float (number2.get())
    x = operation.get()

    if x == "+" :
        y = round((a + b),2)
        ok.config(text =f"{y}")

    elif x == "-":
        y = round((a - b),2)
        ok.config(text =f"{y}")

    elif x == "*":
        y = round((a * b),2)
        ok.config(text =f"{y}")

    elif x == "/":
        y = round((a / b),2)
        ok.config(text =f"{y}")
        


        
button = Button(root ,text = "Calculate" , command= function)
button.pack(pady = 5)

ok = Label(root , text = '')
ok.pack(pady = 5)
    

text4 = Label(root , text = "+ for addition" , bg = bg , font = label_font)
text4.pack(pady =5)

text5 = Label(root , text = "- for substraction" , bg = bg , font = label_font)
text5.pack(pady = 5)

text6 = Label(root , text = "* for multiplication" , bg = bg , font = label_font)
text6.pack(pady = 5)

text7 = Label(root , text = "/ for division" , bg = bg , font = label_font)
text7.pack(pady = 5)

root.mainloop()

