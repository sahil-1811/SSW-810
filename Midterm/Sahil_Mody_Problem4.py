#Name :Sahil Mahendra Mody
#Cwid:20007262



import random

def p4():
    name=input("enter Students name: ")
    dict={}
    while name!="":
        if name=="":
            break
        else:
            dict[name]=random.randint(1,100)
        name=input("Enter student name: ")
    print(dict)
    first,second=0,0
    first = max(dict.values())
    
    second = 0
    for i in dict:
        if(dict[i]>second and dict[i]<first):
                second = dict[i]  
    name1=list(dict.keys())[list(dict.values()).index(second)]
    return (f"{name1} ranks second with {second} marks")
print(p4())

