list=[1,2,3,4,5,6,7,8]
currentSumEven=0
currentSumOdd=0
length=len(list)
i=0
while i<length:
 if i%2==0:
  currentSumEven+=list[i]
 else:
  currentSumOdd+=list[i]
 i+=1		
print("Sum of all odd number index element and even reletively",currentSumEven,currentSumOdd)

