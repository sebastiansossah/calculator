from tkinter import *

root = Tk()
miFrame = Frame(root)
miFrame.config(relief="groove")
miFrame.pack()

#-------------------------Global variables
operacion = ""
results = 0
count = 0

numeroEnPantalla=StringVar()
#numeroEnPantalla.set(0)
resetOperator= False


# -------------------------This is the screen

pantalla = Entry(miFrame, textvariable=numeroEnPantalla)

pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

# -------------------------Functions
def escribirNumero(num):
    global resetOperator

    global operacion #Declare the global function operacion
    
    if resetOperator != False: #use a conditional, if the varible is diferent of empty 
        numeroEnPantalla.set(num) # We start again with the nums that we introduce 
        resetOperator=False #Modify again the varible to be a empty variable, so the code get into else again

    else: 
        numeroEnPantalla.set(numeroEnPantalla.get() + num)
   

#with this function we create the button that delete all the numbers that we input 
#inside the entry
def delete():
    global operacion
    global results
    global resetOperator
    global count
    global count_rest
    global count_div

    pantalla.delete("0","end")
    operacion = ""
    results = 0
    resetOperator=False
    count = 0
    count_rest =0
    count_div = 0

#--------------------------Function sum
def sum(num):
    global operacion
    global results
    global resetOperator

    results+=float(num) #the same that results = results + int(num)
    numeroEnPantalla.set(results)
    operacion="+"
    resetOperator = True
#--------------------------Function rest
count_rest=0
num1= 0
def rest(num):
    global operacion
    global results
    global resetOperator
    global count_rest 
    global num1
    
    print(count_rest)

    if count_rest == 0:
        num1= int(num)
        results = num1
        
    
    else: 
        if count_rest == 1:
            
            results = num1 - int(num)
        
        else:
            results= int(results) - int(num)
    
        numeroEnPantalla.set(results)
        results=numeroEnPantalla.get()
    
    count_rest= count_rest +1
    operacion="-"
    resetOperator=True

#--------------------------Function multipler
def mult(num):
    global operacion
    global results
    global resetOperator
    global count

    if count == 0:
        results = int(num) * 1
        numeroEnPantalla.set(results)
        operacion="x"
        resetOperator=True
        count+=1
    
    else: 
        results = int(num) * results
        numeroEnPantalla.set(results)
        resetOperator=True
        operacion="x"
    
        
#--------------------------Function divison
count_div = 0
num1 = 0
def div(num):
    
    global num1
    global operacion
    global results
    global resetOperator
    global count_div 

    print(count_div)
    print(num1)

    if count_div == 0:
        num1= float(num)
        results = num1
        count_div+=1

    else:
        if count_div == 1:
           results = num1 / float(num)
           numeroEnPantalla.set(results)
           
    
        else: 
            results= float(results)/ float(num)
            numeroEnPantalla.set(results)

        
        numeroEnPantalla.set(results)
        results=numeroEnPantalla.get()
    
    count_div+=1
    operacion="%"
    resetOperator=True

    
    
#-------------------------Function result
def result():
        global results
        global operacion
        global count_rest
        global count_div

        if operacion=="+":
            numeroEnPantalla.set(results+int((numeroEnPantalla.get())))
            results= 0
        
        elif operacion=="-":
            numeroEnPantalla.set(int(results)-int(numeroEnPantalla.get()))
            results= 0
            count_rest= 0

        elif operacion=="x":
            numeroEnPantalla.set(results*int(numeroEnPantalla.get()))
            results= 0

        elif operacion=="%":
            numeroEnPantalla.set(float(results)/float(numeroEnPantalla.get()))
            results= 0
            count_div = 0


# -------------------------This is the first row of buttons
boton7 = Button(miFrame, text="7", width=3, command= lambda:escribirNumero("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command= lambda:escribirNumero("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command= lambda:escribirNumero("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="%", width=3, command= lambda:div(numeroEnPantalla.get()))
botonDiv.grid(row=2, column=4)

# -------------------------This is the second row of buttons
boton4 = Button(miFrame, text="4", width=3, command= lambda:escribirNumero("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command= lambda:escribirNumero("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command= lambda:escribirNumero("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="x", width=3, command= lambda:mult(numeroEnPantalla.get()))
botonMult.grid(row=3, column=4)

# -------------------------This is the third row of buttons
boton1 = Button(miFrame, text="1", width=3, command= lambda:escribirNumero("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command= lambda:escribirNumero("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command= lambda:escribirNumero("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3, command= lambda:rest(numeroEnPantalla.get()))
botonRest.grid(row=4, column=4)

# -------------------------This is the quarter row of buttons
botonComa = Button(miFrame, text=",", width=3, command= lambda:escribirNumero(","))
botonComa.grid(row=5, column=1)
boton0 = Button(miFrame, text="0", width=3, command= lambda:escribirNumero("0"))
boton0.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command= lambda: result())
botonIgual.grid(row=5, column=3)
botonSuma = Button(miFrame, text="+", width=3, command= lambda:sum(numeroEnPantalla.get()) )
botonSuma.grid(row=5, column=4)

# -------------------------This is the quarter row of buttons
botonClear = Button(miFrame, text="Delete", command=delete)
botonClear.grid(row=6, column=2)
root.mainloop()