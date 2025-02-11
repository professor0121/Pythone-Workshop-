list=[1,2,3,4,5,6,7,8]
 
length=len(list)
 
print("before sort=>",list)
for j in range(length-1):
 for i in range(length-1):
  if list[i]<list[i+1]:
   list[i],list[i+1]=list[i+1],list[i]
   print("pass of=>",j+1,list)

print("sorted array in desending order\n\n ",list)