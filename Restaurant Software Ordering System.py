from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000+0+0")
root.title("Restaurant Software Ordering System")


Tops=Frame(root, width=400,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=100,height=650,relief="raise")
f1.pack(side=LEFT)

#===============================TIME=================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Times new roman',50,'bold'),text="Restaurant Software Ordering System",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Fruits.get()==""):
        CoFries=0
    else:
        CoFruits=float(Fruits.get())


    
    if (Vegetables.get()==""):
        CoNoodles=0
    else:
        CoVegetables=float(Vegetables.get())



    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())



    if (Meat.get()==""):
        CoMeat=0
    else:
        CoMeat=float(Meat.get())

        
    if (Chapati.get()==""):
        CoChapati=0
    else:
        CoChapati=float(Chapati.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofFruits =CoFruits * 140
    CostofDrinks=CoD * 65
    CostofVegetables = CoVegetables* 90
    CostofSoup = CoSoup * 140
    CostMeat = CoMeat* 260
    CostChapati=CoChapati * 300

    CostofMeal= "Ksh", str('%.2f' % (CostofFruits+CostofDrinks+CostofVegetables+CostofSoup+CostMeat+CostChapati))

    PayTax=((CostofFruits+CostofDrinks+CostofVegetables+CostofSoup+CostMeat+CostChapati) * 0.2)

    TotalCost=(CostofFruits+CostofDrinks+CostofVegetables+CostofSoup+CostMeat+CostChapati)
 
    Ser_Charge= ((CostofFruits+CostofDrinks+CostofVegetables+CostofSoup+CostMeat+CostChapati)/99)

    Service = "Ksh", str ('%.2f' %  Ser_Charge)

    OverAllCost ="Ksh", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Ksh", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Cancel():
    rand.set("") 
    Fruits.set("")
    Vegetables.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Meat.set("")
    Chapati.set("")
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Fruits=StringVar()
Vegetables=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Meat=StringVar()
Chapati=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Customer Reference Number",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f1, font=('arial', 16, 'bold'),text="Fruits",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fruits,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)


lblVegetables= Label(f1, font=('arial', 16, 'bold'),text="Vegetables",bd=16,anchor="w")
lblVegetables.grid(row=2, column=0)
txtVegetables=Entry(f1, font=('arial',16,'bold'),textvariable=Vegetables,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtVegetables.grid(row=2,column=1)


lblSoup= Label(f1, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lblMeat= Label(f1, font=('arial', 16, 'bold'),text="Meat",bd=16,anchor="w")
lblMeat.grid(row=4, column=0)
txtMeat=Entry(f1, font=('arial',16,'bold'),textvariable=Meat,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtMeat.grid(row=4,column=1)

lblChapati= Label(f1, font=('arial', 16, 'bold'),text="Chapati",bd=16,anchor="w")
lblChapati.grid(row=5, column=0)
txtChapati=Entry(f1, font=('arial',16,'bold'),textvariable=Chapati,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtChapati.grid(row=5,column=1)
                              
#=================================RESTAURANT INFORMATION=======================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnCancel=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Cancel",bg="powder blue",command=Cancel).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


root.mainloop()


