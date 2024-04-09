# i=0
# while (i<10):
#   if(i%2):
#      i =i+3
#   i =i+1
#   print 

# print((1,2,3)+('a','b','c'))

# for i in ('a','b','c','d'):
#   print(i,end="")
# else:
#   print('end')

# print(16/2)


# n=4
# def f1():
#   n=n**4
#   print(n)
# f1()

# list1=[1,2,3,4,5]
# s=0
# i=1
# while(i in list1):
#   s=s+i
#   i=i+1
# print(s,end="")

# list1=[1,2,3,4,5]
# list2=[i%5 for i in list1]
# print (list2)


# set1={1,2,3,4,5}
# set1.clear()
# print (set1)


# class Cat:
#   def __init__(self,age):
#     self.age =age
#   def set_age(self,num):
#     self.age=num
#   def get_age(self):
#     return self.age
# cat1 =Cat(2)
# cat2 =Cat(4)
# cat1.set_age(cat2.get_age()) 
# cat2.set_age(5)
# cat3=Cat(cat1.get_age()+cat2.get_age())
# print(cat3.get_age())


# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
# age=50
# p1 =Person('Sam',24)
# print(p1.name,p1.age)

# a=4 
# print(a>>3)

# class Reeta:
#   name="Reeta"
#   blood_group="B Positive"
# class Priyanka(Reeta):
#   name='Priyanka'
# person = Priyanka()
# print(person.name,"-",person.blood_group)

# def fun1():
#   print(1)
# def fun2():
#   print(2)
# def fun3():
#   print(3)
# def func(ch):
#   switch ={
#     'x':fun1,
#     'y':fun2,
#     'z':fun3,
#   }
#   return switch.get(ch,'Wrong input')
# print(func('z'))


# set1={3.5,'g',6,3}
# set2={'h',4,3,'y'}
# print (set1.symmetric_difference(set2))

# for i in range(1,6,2):
#  if i==4:
#   break
#  print(i,end="")

# n=5
# while(n):
#  n = n-1
#  print(n,end='')


# name ='Python'
# def func():
#   name = " PythonGeeks"
# print(name)

# list1 =[14,19,6,13,0]
# def func(lst):
#   for i in lst:
#     if i %2:
#       print(i,end='')
# func(list1)
