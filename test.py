from datetime import datetime as dt 

now = dt.now()
then = dt(1988,5,18,12,56,42)
delta = now-then
deltadays = delta.days
deltadays = "{:,}".format(deltadays)
print("It's been",deltadays,"days since I was born.\nxD")
print(type(delta))

# whenever = dt.strptime("2017-12-31-20-59", "%Y-%m-%d-%H-%M")
# whenever.strftime("%Y-%m-%d")
# print(whenever)
# print(whenever.strftime("%Y-%m-%d"))

# a = [1,2,3]
# b = ["x", "y", "z"]
# for i,j in zip(a,b):
#     print("%s is %s" %(i,j))

# L = lambda x,y,z: (x+y)**z
# def something(what):
#     for a,b in zip(what,range(len(what))):
#         line = L(a,5,2)
#         print("Entry",b+1,"is",line)

# something([5,6,7,8])