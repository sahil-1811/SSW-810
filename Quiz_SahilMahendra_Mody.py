
def reverse(data):
    updated_data1=[]
    for i in range(len(data),0,-1):
        print(i)
        updated_data1.append(i)
    return (f"Normal data:{data} and reversed data:{updated_data1}")



n=int(input("Enter the range of list: "))
data=[]
for i in range(n):
     t=int(input("ENter numbers"))
     data.append(t)
print(reverse(data))
print("-"*100)

def prime(n):
    c=0
    print("Prime Numbers Are: ")
    for i in range(2,n):
        flag=True
        for j in range(2,i//2+1):
            if i%j==0:
                flag=False
        
        if flag==True:
            print(i)
    

prime(100)
print("-"*100)

def duplicates(data):
    dict={}
    for i in data:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    arr=[]
    for j in dict:
        if dict[j]>1:
            arr.append(j)
    return (f"Normal array is {data} and Array with duplicate values is {arr}")


data=[1,2,3,4,3,4,4]
print(duplicates(data))
print("-"*100)