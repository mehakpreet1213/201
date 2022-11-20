from tkinter import *
window=Tk()

# add widgets here


window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window,text="enter your height",fg="black",bg="lightcyan",font=("calibri",12))
height_label.place(x=20,y=140)

height_Entry=Entry(window,text="",bd=2,width=22)
height_Entry.place(x=150,y=140)

weight_Label=Label(window,text="enter your weight",fg="black",bg="lightcyan",font=("calibri",12))
weight_Label.place(x=20,y=190)

weight_Entry=Entry(window,text="",bd=2,width=22)
weight_Entry.place(x=150,y=190)


def calulatebmi():
    weight=int(weight_Entry.get())
    height=int(height_Entry.get())/100
    bmi=weight/(height*height)
    bmi=round(bmi,1)
    message=""
    if bmi< 18.5:
        message="you are underweight"

    elif bmi>18.5 and bmi <=24.9:
        message="it is normal range"

    elif bmi >25 and bmi<=29.5:
        message="you are overweight"

    elif bmi >30:
        message="you are obese"

    else:
        message="something went wrong"
    output_message=Label(result_frame,text=name+" your bmi is "+str(bmi)+"  and "+message,bg="lightcyan",font=("calibri",12))
    output_message.place(x=20,y=40)
    output_message.pack()

    calculate_button=Button(window,text="calculatebmi",fg="black",bg="lightcyan",command=calculate_bmi)
    calculate_button.place(x=20,y=200)





result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()