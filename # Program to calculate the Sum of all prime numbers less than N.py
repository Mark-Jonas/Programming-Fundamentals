#Sum of all prime numbers upto X
# Mark-Jonas Koranteng (10955584) DCIT 104
# I did this assignment on my own
num=input("input number value")
num=int(num)
sum=0
for i in range(2,num+1):
    for k in range(2,i):
        if(i%k==0):
            break
    else:
        print(i, "is prime")
        sum=sum+i
print("the sum of prime numbers is", sum)