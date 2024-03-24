#answer=bool(input("enter"))
#print(type (answer),answer)
    

#name="chahat"
#print("his name is ",name)
#print(f"his name is (name)")

#a=10
#b=20
#10 is a and b is 20
#print(a,"is a and b",b)
#10 is a and b is 20

#print("a is ",a,"and b is ",b)
#print(a,"is a and ",b,"is b")

#a=10
#b=20
#c=30
#print(a,b,sep="mera ho jayega")#\t give the 4 digits space 


#a=10
#b=5
#we print to the current line and then shift to the new line
#print(a,b,"\n")


#single line comment #
#multiple line comment '''

"""
Arithmetic operators
Addition +
Subtraction -
Multiplication *
float Division /
Floor Division // (returns the integer part of the division)
Modulus % (returns the remainder of the division)
Exponentiation **      basically power
"""

"""Assignment Operators
Used to assign values to variables.

Assign =
Add and Assign +=
Subtract and Assign -=
Multiply and Assign *=
Divide and Assign /=
Modulus and Assign %=
Exponentiate and Assign **=
Floor Divide and Assign //=
"""

"""Bitwise Operators
Used for manipulation of individual bits in integers.

Bitwise AND &
Bitwise OR |
Bitwise XOR ^(charet symbols)
000
011
101
110

Bitwise NOT ~
Left Shift <<
Right Shift >>
"""

"""
(-234)
o/p=235
-(-234)
o/p=233
"""


"""a=10
print(a<<2)
print(a>>2)"""
#every left shift is multiplied by 2
#every right shift is divide by 2

# (IDLE)integrated development learning environment 

"""
COMPARISION OPERATOR IS BASICALLY TO PRINT TRUE AND FALSE 
LOGICAL OPERATORS (WHEN U HAVE TO COMBILE MULTIPLE TASKS)
and -WHEN ALL NEEDED (small character we have to use )
or-ANY ONE WOULD BE 
"""

#calculate the square of a number 
#THE PROGRAMMER SHOULD THINK LIKE THIS
#(1) O/P (2) Process (3) I/P(WORK IN OPPOSITE WAY)
#method 1
"""number = 5
square = number ** 2

print(f"The square of {number} is {square}")

#method 2
number = 5
square = pow(number, 2)

print(f"The square of {number} is {square}")

#method 3

number = 5
square = number * number

print(f"The square of {number} is {square}")
"""
#CUBE OF A NUMBER
#print(cube)
#no ** 3
#input 10
"""n=float(input ("enter a number"))
cube=n**3
print(f"cube of { n } is {cube}")"""

#convert INR to USD
#85->1$
"""
O/P->USD
INR/85
O/P->INR
"""

"""INR=float(input("enter amount in INR:"))
USD=INR/85
print(f"Amount {INR} INR is {USD}$")
"""

"""import math 
math.sqrt(49)
math.pow(2,2)"""

"""#quadratic equations
import math
# Import math module for sqrt function
import math

# Define coefficients
a = 1
b = 5
c = 6

import math
a=float (input("a"))
b=float (input("b"))
c=float (input("c"))
term=math.sqrt(b**2-4*a*c)
root1=(-b+term)/(2*a)
root2=(-b-term)/(2*a)"""

"""# Calculate the discriminant
discriminant = b**2 - 4 * a * c

if discriminant >= 0:
  
  root1 = (-b + math.sqrt(discriminant)) / (2 * a)
  root2 = (-b - math.sqrt(discriminant)) / (2 * a)
  
 
  print(f"Root 1: {root1}")
  print(f"Root 2: {root2}")
else:
  
  imaginary_part = math.sqrt(-discriminant) / (2 * a)
  
 
  print(f"Root 1: {-b / (2 * a)} + {imaginary_part}i")
  print(f"Root 2: {-b / (2 * a)} - {imaginary_part}i")
"""


"""
code:
sequence 
branch (if,if else,if elif else)
loop(for,while)

"""


"""n=int(input("enter a number"))
if n>=0:
    print(n,"is +ve")
if n<=0:
    print(n,"is -ve")"""
"""
n=int(input("enter a number"))
if n>=0:
    print(n,"is +ve")
else:
    print(n,"is -ve")"""



"""
n=int(input("enter a number"))
if n>0:
    print(n,"is +ve")
elif n<0:
    print(n,"is -ve")

else:
    print(n,"is  zero")

    """

"""number1 = 10
number2 = 20

minimum = min(number1, number2)

print(f"The minimum of {number1} and {number2} is {minimum}")
"""

"""
number1 = 10
number2 = 5
number3 = 12

minimum = (number1 if number1 <= number2 else number2) if (number1 if number1 <= number2 else number2) <= number3 else number3

print(f"The minimum of {number1}, {number2}, and {number3} is {minimum}")

"""
""
#check if y is leap year
"""year = int(input("enter a number"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")"""

### print three number used in ascending order
"""homework"""       

##1 to 10 
"""start=1
while start<=10:
    print(start)
start+=1


"""
#10 to 1
"""start = 10
while start >= 1:
    print(start)
    start -= 1"""

#1 to n for n>=0
#n to 1 for n>0
#accept start and end from user and
#example start 2 end 5,2,3,4,5
#start 2 end -2,2,1,0,-1,-2




#in bidding process take max and stop
#when less than last is given 
#1,2,5,18,2 stop max:18
#2,7,100,1000,1,stop MAX:1000
#logic max=0,1,2,5,10,18,18---2 stop and report
"""
sum =0 
while True:
     n=int (input ("enter a number "))
     if n<0:
         break
     sum+=n
     print ("sum is :",sum)

"""
#keep accepting numbers till 0 given
#when 0 is given print min,max and avg of all numbers
#6,1,7,2,9,12,5,3,0
#max:12
#min:1
#avg=(6+1....+3)/total no of element
"""max=0   #ref
min=999 #ref
count=0
sum=0
while True:
    no=int(input("Enter:"))
    if no==0:
        break
    if no>max:
        max=no
    if no<min:
        min=no
    count+=1
    sum+=no
print("Max is:",max,"Min is",min,"Avg:",(sum)/count)"""

#in bidding process take max and stop
#when less than last is given
#1,2,5,10,18,2 stop Max:18
#2,7,100,1000,1 stop Max:1000
#logic: max=0,1,2,5,10,18---2 stop and report
"""max=0
while True:
    no=int(input("Enter:"))
    if no>max:
        max=no
    else:
        break
print("Max is:",max)"""


#convert days in year and months (365,30 MONTH)
#input days-------Y+M 720days
#days =720
#print("year",days//365)

"""
DAYS -> 928// 365
928 % 365
MONTH=DAYS//30
DAYS=DAYS%30
"""

#given time in secs convert it to hours in minute 
"""
seconds=8200
hours=seconds//3600
print("hours",hours)
minute=seconds//60
print("minute",minute)
"""
#given 2 times in hours :mins:secs separately show addition of both
#t1 2:37:52  t23:41:51 =6:19:43

"""h1,m1,s1=2,37,52
h2,m2,s2=23,41,51
s3=s1+s2
m3=m1+m2
h3=h1+h2
m3=m3+s3//60
s3=s3%60
h3=h3+m3//60
m3=m3%60
print(f"time: {h1} {m1} {s1}")
print(f"time: {h2} {m2} {s2}")
print(f"time: {h3} {m3} {s3}")

"""
"""
a=10
b=20
print("a=",a,"b=",b)
a,b=b,a
print("a=",a,"b=",b)"""

#swap two variable with arithmatic operations
#swap two variables with bitwise operations(X-OR)
"""a=10
b=8
print("a=",a,"b=",b)
a=a^b
b=a^b
a=a^b
print("a=",a,"b=",b)"""
"""
age=18
if(age>=18):
    print("they can vote")
else:
    print("not vote")"""

#reads marks of 5 subjects and print passing class m
#marks are out of 100 and total is 500
#percentage >=60 :first class
#percentage >=50 :second class
#50>percentage=40 :pass class
#40>percentage :failed
#note student fails if in any subject he/she scores below 40

"""n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
n4=int(input("enter a number"))
n5=int(input("enter a number"))
if(n1 or n2 or n3 or n4 or n5 <40):
    print("fail in some subjects ")
total=n1+n2+n3+n4+n5
percentage=(100*total)//500
if (percentage>=60):
    print("first class")
elif(percentage>=50):
    print("Second class")
elif(percentage>=40):
    print("pass")
else: 
    print("fail")
    
    """
"""flag=0
total=0
for i in range(1,6):
    m = int(input("Enter Mark for subject " + str(i) + ":"))
    total+=m
    if m<40:
        flag+=1
percentage=(100*total)//500
percentage=(100*total)/500
if flag>0:
    print(f"failed in {flag} with {percentage} ")
else:
    if percentage>=60:
        print(f"Passed with:{percentage} First class")
    elif percentage>=50:
        print(f"Passed with:{percentage} Second class")
    elif percentage>=40:
        print(f"Passed with:{percentage} Pass class")
"""

#Enter three angles & check if it is a triangle
"""a1,a2,a3=float(input("Angle 1")),float(input("Angle 2")),float(input("Angle 3"))
if a1>0 and a2>0 and a3>0:
    if a1+a2+a3==180:
        print("Triangle it is")
    else:
        print("It is not")
else:
    print("It is not")"""

"""
    153%10=3 153//10=15
    15%10=5  15//10=1
    """

#divide numbers in its parts
"""no=int(input("Enter no:"))
while no>0:
    digit=no%10
    no//=10
    print(f"we have {no} digit removed {digit}")
"""
#find sum of all digits
"""sum=0
no=int(input("Enter no:"))
while no>0:
    digit=no%10
    no//=10
    sum+=digit
    print(f"We have {no} digit removed {digit}")
print("Sum is:",sum)


"""
#reverse a number
"""rno=0
no=int(input("Enter no:"))
while no>0:
    digit=no%10
    no//=10
    rno=rno*10+digit
    print(f"We have {no} digit removed {digit} reverse no is {rno}")"""
#from 100 to 999 count and print number of palindrome numbers
"""101
.
.
.
999
Total :"""

#read no
#make copy
#reverse
#compare with copy/original and comment
"""
count=0
for no in range(100,1000):
    tno=no#make copy
    rno=0
    while tno>0:#reverse
        digit=tno%10
        tno//=10
        rno=rno*10+digit
    if rno==no:#compare with copy/original and comment
        print(no)
        count+=1
print("Total numbers printed are:",count)"""

#armstrong  number:



#armstrong number:
"""sum=0
no=int(input("Enter no:"))
tno=no
while no>0:
    digit=no%10
    no//=10
    sum+=digit**3
    print(f"We have {no} digit removed {digit} so far sum is {sum}")
if sum==tno:
    print("Yes")
else:
    print("Not")"""

#armstrong number between 100 to 999
#check prime or not
"""for no in range(1,50):
    flag=True
    for i in range(2,no):#7  2,3,4,5,6
     if no%i==0:
        flag=False
        break
if flag:
    print(no,"is prime")
else:
    print(no,"is not prime")

"""

#1+2+3+4.....+n     n is number
#1*2*3.......n
#1/2+3/4+5/6    n term
#1/2-3/4+5/6-7/8   nth term
#0 1 1 2 3 5....nth term

#1+2+3+4.....+n     n is number
"""sum=0
n=int(input("Enter n:"))
for i in range(1,n+1):
    print(i,end="+")
    sum+=i
print("Sum is :",sum)
"""
#factorial of number

"""product=1
n=int(input("Enter n:"))
for i in range(1,n+1):
    print(i,end="X")
    product*=i
print(":",product)"""
#calculate x to the power of  y without any function
#or operator
"""product=1
x=int(input("Enter X:"))
y=int(input("Enter power y:"))
for i in range(y):
    print(x,end=" X ")
    product*=x
print(f"\n{x} to power of {y} is {product}")
"""
"""#1/2+3/4+5/6    n term n=1 1/2 n=2 1/2 3/4 n=3 1/2 3/4 5/6
n=int(input("Enter n:"))
sum=0.0
for i in range(1,(2*n)+1,2):
    print(i,"/",(i+1),end=" + ")
    sum+=i/(i+1)
print("\nSum is:",sum)
"""
"""#1/2-3/4+5/6-7/8
n=int(input("Enter n:"))
m=1
sum=0.0
for i in range(1,(2*n)+1,2):
    print(m*i,"/",(i+1),end=" + ")
    sum+=m*(i/(i+1))
    m=m*-1
print("\nSum is:",sum)
"""
#fibo
#every next element is addition of last 2
# 0,1    ,1,2,3,5,8...... nth term
"""f0=0
f1=1
n=int(input("Enter n:"))
for i in range(0,n):
    if i<=1:
        print(i,end=",")
    else:
        fn=f0+f1
        print(fn,end=",")
        f0,f1=f1,fn
"""
# accept a number from user and check is it from fibo series
#ex:input:8 yes it is
#ex2:input:9 no it is not
#calculate series till fn crosses given number if match stop
#else say no
"""

f0=0
f1=1
no=int(input("Enter number to check:"))
for i in range(0,no):
    if i<=1:
        print(i,end=",")
    else:
        fn=f0+f1
        print(fn,end=",")
        if fn==no:
            print("Found in series")
            break
        if fn>no:
            print("Not Found in series")
            break
        f0,f1=f1,fn
"""

#create menu driven code for tea,coffee,water
"""while True:
    choice=int(input("\n1.Tea\n2.Coffe\n3.Water\n0.Exit\n:"))#menu
    if choice==1:
        print("Tea selected")
    elif choice==2:
        print("Coffee selected")
    elif choice==3:
        print("Water selected")
    elif choice==0:
        print("Thanks for using code")
        break
    else:
        print("Wrong choice")"""

#create menu driven code for tea(10),coffee(20),water(15)
#on exit calculate total amount earned also show itemized sale
#example:
# 10 Tea sold 100
# 5 Coffees sold 100
# 2 Water sold 30
# Total:2
"""
tc=cc=wc=0
while True:
    choice=int(input("\n1.Tea\n2.Coffe\n3.Water\n0.Exit\n:"))#menu
    if choice==1:
        print("Tea selected")
        tc+=1
    elif choice==2:
        print("Coffee selected")
        cc+=1
    elif choice==3:
        print("Water selected")
        wc+=1
    elif choice==0:
        print("Thanks for using code")
        break
    else:
        print("Wrong choice")
total=tc*10+cc*20+wc*15
print("sells")
print("-----------------------------------------------------")
print(f"{tc} Tea sold earned {tc*10} ")
print(f"{cc} Tea sold earned {cc*20} ")
print(f"{wc} Tea sold earned {wc*15} ")
"""
#create menu driven code for tea(10),coffee(20),water(15)
#on exit calculate total amount earned also show itemized sale
#example:
# 10 Tea sold 100
# 5 Coffees sold 100
# 2 Water sold 30
# Total:230
#price to seller for tea is 5,coffess is 12 and water is 13
#calculate net profit from sells
"""tc=cc=wc=0
while True:
    choice=int(input("\n1.Tea\n2.Coffe\n3.Water\n0.Exit\n:"))#menu
    if choice==1:
        print("Tea selected")
        tc+=1
    elif choice==2:
        print("Coffee selected")
        cc+=1
    elif choice==3:
        print("Water selected")
        wc+=1
    elif choice==0:
        print("Thanks for using code")
        break
    else:
        print("Wrong choice")
total=tc*10+cc*20+wc*15
print("sells")
print("-----------------------------------------------------")
print(f"{tc} Tea sold earned {tc*10} ")
print(f"{cc} Tea sold earned {cc*20} ")
print(f"{wc} Tea sold earned {wc*15} ")
print(f"Total is{total} ")
net_total=tc*5+cc*12+wc*13
print("Profit is:",total-net_total)
"""

#a shop sells tea(10),coffee(20),water(15)
#take order aksing each item and generate bill per customer along with bill number
#2300 to start c1-2301 c2-2302
#after order will go to next customer till customer says -1
#calculate total amount earned also show itemized sale


"""tc=cc=wc=0#GLOBAL COUNTER
billno=2300
while True:
    nt=int(input("Tea ?"))
    tc+=nt
    nc=int(input("Coffee ?"))
    cc+=nc
    nw=int(input("Water ?"))
    wc+=nw
    billno+=1
    print("Your bill no is:",billno)
    print("-------------------------------------------------------------------")
    if nt>0:
        print(f"Tea {nt} total {nt*10}")
    if nc>0:
        print(f"Coffee {nc} total {nc*20}")
    if nw>0:
        print(f"Water {nw} total {nw*15}")
    print("Amount to be paied:",(nt*10)+(nc*20)+(nw*15))
    print("-------------------------------------------------------------------")
    choice=input("\nWant stop -1 else any key to order more")
    if choice=="-1":
        break


total=tc*10+cc*20+wc*15
print("sells")
print("-----------------------------------------------------")
print(f"{tc} Tea sold earned {tc*10} ")
print(f"{cc} Coffe sold earned {cc*20} ")
print(f"{wc} Water sold earned {wc*15} ")
print(f"Total is{total} ")
net_total=tc*5+cc*12+wc*13
print("Profit is:",total-net_total)
"""


# DAY 5:
""" 
encapsulation
data + operation:eg pani puri

abstraction 
data (hidden)+ operation (open): eg pani puri

polymorphisms
override (inheritance) / overload(support to multiple types)


inheritance(take properties from pre-existing )
type of inheritance 
there is no keyword in inheritance just use this symbols ==>()
single 
multilevel
hierarchical 
multiple (4/10 question may be asked )
hybrid(multiple + multi-level )

class X(s1,s2,s3):
    s1.edu()   
"""

"""
"""

#QUESTION ==> (human-name,gender),(education-degree) and job (salary)
#use init() to 
#set all data in 
#each class 

#Human,Education,Job
"""class Human:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def display(self):
        print("\nHuman:Name:",self.name,"Gender:",self.gender)
class Education(Human):
    def __init__(self,name,gender,degree):
        super().__init__(name,gender)
        self.degree=degree
    def display(self):
        super().display()
        print("\nEducation: Degree:",self.degree)
class Job(Education):
    def __init__(self,name,gender,degree,salary):
        super().__init__(name,gender,degree)
        self.salary=salary
    def display(self):
        super().display()
        print("\nJob: salary:",self.salary)


j=Job("amar","male","phd",1000)
j.display()


"""
#create class Alive
#having method communicate:
#human,dog,bug are sub classes of Alive 
#but dog communicate:barking 
#but bug comunicate : some sound 
#1 which type of inheritance 
#implement this 

"""class Alive:
    def communicate(self):
        pass
class Human(Alive):
    def communicate(self):
        print("Language spoken")
class Dog(Alive):
    def communicate(self):
        print("Bhow Bhow")
d=Dog()
h=Human()
d.communicate()
h.communicate()
"""
#banking systems
"""
Menu 1.Create account
                auto generate account number iff balance is 3000+ also takes name ,gender
                shows account created and account number 
     2.deposit 
                read account number ,search for account if found then read amount can not be  -ve 

     3.Withdrawl 
               read account  number ,search for account if found then read amount allow transection iff after transaction balance is > 3000
     4. Check balance 
                read account  number ,search for account if found then give balance 
     5.Exit 

"""
class Bank_Account:
    generated_account_no=20240300#class variable
    #class variable has single copy(static of java)
    def __init__(self):
        self.name=input("Enter name:")
        self.gender=input("Enter gender:")
        while True:
            self.amount=float(input("Enter Amount min is 3000:"))
            if self.amount>=3000:
                break
        print("account created:")
        self.account_no=(Bank_Account.generated_account_no+1)
        #made an instance copy for object from class variable
        Bank_Account.generated_account_no+=1
        print("Your account number is:",self.account_no)

    def deposit(self):
        amt=float(input("Enter amount:"))
        if amt<0:
            print("can not give -ve")
        else:
            self.amount+=amt
            print("New balance for",self.account_no,"is",self.amount)
    def withdraw(self):
        amt=float(input("Enter amount:"))
        if self.amount-amt<=3000:
            print("no funds")
        else:
            self.amount-=amt
            print("New balance for",self.account_no,"is",self.amount)
    def check_balance(self):
        print("Balance for",self.account_no,"is",self.amount)


Accounts={}
while True:
    choice=int(input("\n1.Create Account\n2.Deposit\n3.Withdraw\n4.Check Balance\n0.Exit"))
    if choice==1:
        a=Bank_Account()
        Accounts[a.account_no]=a
    elif choice==2:
        a=int(input("Enter Account number:"))
        if a in Accounts:
            print("Account found")
            current_account=Accounts[a]
            current_account.deposit()
        else:
            print("Not found")
    elif choice==0:
        print("Exiting system")
        break        
