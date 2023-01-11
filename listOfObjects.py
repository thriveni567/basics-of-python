class student:
     def __init__(self,name,rollno):
            self.name=name
            self.rollno=rollno

list=[]
list.append(student("rahul",4))
list.append(student("sathvik",5))
list.append(student("yaswin",8))
print(type(list))
print("length of the list is",len(list))
for obj in list:
    print(obj.name, obj.rollno,sep=',')

