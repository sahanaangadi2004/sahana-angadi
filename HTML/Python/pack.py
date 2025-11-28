
t=10,20,30
a,b,c=t
print(a)
print(b)
print(c)


a=10
b=20
c=30
t=a,b,c
print(t)

str='a quick brown fox'
print(str[2:7:])
print(str[-3:])
print(str[9:12:])
print(str[2:7:2])


#set
s={34,52,78,18,30,52,34,52}
print(len(s))
print(s)
s=set()
print(type(s))

#dictionary
Student={
    'Name':'anu',
    'Age':21,
    'Course':'MCA',
    'phone':9876543210,
    'email':'anu@gmail.com',
    'age':22
}
print(Student)
print(Student['Name'])
print(Student['age'])       
Student['name']= 'Anu Kumar'
Student['city']='Bangalore'
print(Student)


