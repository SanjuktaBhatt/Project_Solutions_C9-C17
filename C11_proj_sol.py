import time
numbers=[0,1,5,19,65,211,"?"]
#Hint: 3^n-2^n=665
t1=time.time()
ans=int(input("Enter the missing number: "))
print(ans)
while ans!=665:
  ans=input("Enter the missing number again: ")
if ans==665:
  t2=time.time()
  puzzle_time=t2-t1
print(puzzle_time)    
