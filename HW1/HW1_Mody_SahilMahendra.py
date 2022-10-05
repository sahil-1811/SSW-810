#Sahil Mahendra Mody
# Assignment 1
#CWID: 20007262


#q1
iterations=int(input("Q1: Enter Number of iterations: "))
nums1=[]
nums2=[]
y=1
for i in range(1,iterations+1):
    if i%2==0:
        nums1.append(-1/y)
    else:
        nums2.append(1/y)
    y+=2
result=sum(nums1)+sum(nums2)
pi=4.0*result
print(pi)
    
print("-----------------------------------------------------------------------------------------------------------")
# #q2
Sum = 0.0
avg=0.0
nums1=[]
data = input("Q2: Enter a number until you press Enter: ")
while data != "":
    number = float(data)
    nums1.append(number)
    Sum += number
    data = input("Enter the next number: ")
print("The sum is", Sum)
print("The average is:",Sum/len(nums1))
print("-----------------------------------------------------------------------------------------------------------")
# #q3:
number_of_years=int(input('Q3: Enter number of years: '))
salary=int(input("Salary: "))
Percentage_increase=int(input("Enter percantage: "))
if Percentage_increase>100:
     print("Error Output")
else:
    print('Year \t Salary \t Rise in Percentage')
    print('--------------------------------------')
    print(1,'\t',format(salary, '.2f'),'\t',0)
    for i in range(2,number_of_years+1):
        salary+=salary*(Percentage_increase/100)
        print(i,'\t',format(salary, '.2f'),'\t',Percentage_increase)


print("-----------------------------------------------------------------------------------------------------------")
#q4
import random
money=int(input("Q4: Enter amount: "))

count=0
price=0
while money:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
   
    if dice1+dice2==7:
        money+=4
    else:
        money-=1
    price=max(price,money)
    count+=1
print("Maximum Price: ",price)
print("Number of rolls to break: ",count)
