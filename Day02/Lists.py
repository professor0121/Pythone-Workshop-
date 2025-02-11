#python list 

l=[1,2,3,4,5,6,7,8]
print(l)

#Accessibility of the Lists 

print("lists element not  manual accing these using a loop")

for i in l:
 print(i,end="\t")


print("\nlists element not  manual accing these using a loop by index")

for i in range(0,len(l)):
 print(i,"-------->",l[i])