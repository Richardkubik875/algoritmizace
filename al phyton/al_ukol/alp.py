def myMapFunc(n):
    return n*10
my_list = {2,3,4,5,6,7,8,9}
updated_list = map(myMapFunc, my_list)
print(updated_list)
print(list(updated_list))