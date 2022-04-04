# for i in range(1,10):
#   if i%2==0:
#        continue
#   elif i%5==0:
#             break
#   else:
#             print(i)


# x=18
# for i in range(3,x):
#     if x %i==0:
#         print(x,"asal değildir")
#         break 
# else:
#     print(x,"asaldır")

# import time 
# t1=time.time()
# t1=t1+60+60
# t2=time.gmtime(t1)
# print(t2)


# import time 
# for i in range(10):
#     print(i)
#     time.sleep(0.1)

# import random 
# a=5
# b=10
# x=a+(int)((b-a)*random.random())
# print(x)

x=[1,2,3,4,5,5]
for indis,eleman in enumerate(x):
    print("x[{}] ={}".format(indis,eleman))