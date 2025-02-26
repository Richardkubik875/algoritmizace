def myMapFunc(s):
    return s.upper
my_str = "Čauky"
updated_list = map(myMapFunc, my_str)
print(updated_list)
for i in updated_list:
    print(i)