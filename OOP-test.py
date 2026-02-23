
# def test(a,b=[]):
#     test.flag = 'Now you see me!'
#     b.append(a)
#     return b

# test_1 = test
# print(test_1(1)) #如果把这行注释掉就会报错，因为test_1.flag是在test函数中定义的，如果不调用test函数，test_1.flag就不会被定义，所以会报错。
# print(test_1.flag)
# print(hasattr(test_1, 'flag')) #True

a = [1,2,3]
b = [9]
c = [4,5,6,7,8,9]
print(max(a,b,c,key = len))