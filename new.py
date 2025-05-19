# start=int(input("enter a 1st num:"))
# end=int(input("enter a 2nd num:"))
# sum=0
# for num in range(start,end+1):
#     if num%2==0:
#         sum = sum+num
# print(sum)

# num=12345
# rev_num=0
# while num!=0:
#     last_digit=num%10
#     last_digit*10+

# user_inp= eval(input('enter a collection of nums:'))
# for table in user_inp:
#     for fac in range(11,21):
#         print(table*fac)

user_inp=int(input("legnth of fib"))
fib=[0,1]
for _ in range(user_inp-2):
    fib.append(fib[-1]+fib[-2])
print(fib)



