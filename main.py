print("I can solve the cubic with 3 real roots i. e. ax^3+bx^2+cx+d=0")
#create a function,beacuse we just need a b c d to solve the equiation ,so we just put a b c d in this function
name=str(input("What is your name? "))
#ask for the name
a=int(input("What is a? "))
b=int(input("What is b? "))
c=int(input("What is c? "))
d=int(input("What is d? "))
#ask for the value of a, b, c and d
def f(a,b,c,d):
    y = (((-b ** 3) / (27 * a ** 3) + ((b * c) / (6 * a ** 2)) - (d / (2 * a))) + ((((((-b ** 3) / (27 * a ** 3)) + ((b * c) / (6 * a ** 2)) - (d / (2 * a))) ** 2) + ((c / (3 * a)) - (b ** 2) / (9 * a ** 2)) ** 3) ** (1 / 2))) ** (1 / 3)
    return y #fomula1

def g(a,b,c,d):
    y = (((-b ** 3) / (27 * a ** 3) + ((b * c) / (6 * a ** 2)) - (d / (2 * a))) + ((((((-b ** 3) / (27 * a ** 3)) + ((b * c) / (6 * a ** 2)) - (d / (2 * a))) ** 2) + ((c / (3 * a)) - (b ** 2) / (9 * a ** 2)) ** 3) ** (1 / 2))) ** (1 / 3)
    return y #fomula2

def l(a,b,c,d):
    y = -b/(3*a)
    return y #fomula3

def m():
    y = f(a,b,c,d)+g(a,b,c,d)+l(a,b,c,d) #add every fomulas together
    return str(y.real) #we need to add .real after the anwser beacuse we need a interger anwser

line="Hello,"+name.capitalize()+" I will solve "+str(a)+"x^3-"+str(b)+"x^^2+"+str(c)+"x-"+str(d)+"=0"#This is to create a sentence for user
line=line.replace("--","-")#to refine the sentence
line=line.replace("1x^3","x^3")
print(line)#print the sentence
print("The root is ",m())

quit()



