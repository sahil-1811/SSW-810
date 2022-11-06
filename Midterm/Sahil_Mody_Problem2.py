#Name :Sahil Mahendra Mody
#Cwid:20007262



def fibonacci(num):
    res=[]
    a=0
    b=1

    count=0

    if num < 0:
        return False
    elif num == 0:
        return True
    elif num == 1:
        return True 
    else:
        while count<=num:
            c=a+b
            res.append(c)
            a=b
            b=c
            count+=1


            print(res)
            if num in res:
                return True
        return False   


num=int(input("Enter a number to check whether it is in fibonacci series:"))
print(fibonacci(num))
 