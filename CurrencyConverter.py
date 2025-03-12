from currency_converter import CurrencyConverter
import tkinter as tk
a = CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")

def clicked():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = a.convert(amount , cur1 , cur2)
    l5 = tk.Label(window,text=data , font="Times 25 bold").place(x = 200 , y = 290)

L1 = tk.Label(window,text="Currency Converter" , font="Times 25 bold").place(x = 100 , y = 30)
L2 = tk.Label(window,text="Enter Amount Here : " , font="Times 18 bold").place(x = 50 , y = 80)
e1 = tk.Entry(window)

L3 = tk.Label(window,text="Enter Currency : " , font="Times 18 bold").place(x = 50 , y = 130)
e2 = tk.Entry(window)

L4 = tk.Label(window,text="Enter Req Currency : " , font="Times 18 bold").place(x = 50 , y = 180)
e3 = tk.Entry(window)
b1 = tk.Button(window,text="click"  , command=clicked).place(x =230 , y = 240)

e1.place(x = 300 , y = 85)
e2.place(x = 300 , y = 140)
e3.place(x = 300 , y = 190)
window.mainloop()




#a = CurrencyConverter()
#print(a.convert(12 , "USD" , "INR"))

