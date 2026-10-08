
#sum entering values
def sum1(n,sum=0):
    if n==0:
        return sum
    return sum1(n//10,sum+n%10)
num=int(input("enter the number :"))
print(sum1(num))
# count the values
def count1(n,count=0):
    if n==0:
        return count
    return (1+count1(n//10))
num=int(input("enter the values :"))
print(count1(num))
