# Named parameter
# def addition(num, num1):
#     return num+num1

# add = addition(num1=2, num=5)
# print(add)

# optional/default parameter
# def addition(num, num1=0):
#     return num+num1

# add = addition(2)
# print(add)

# multi parameter in list form
# def addition(*numbers):
#     sum = 0
    # for i in numbers:
    #     sum += i
    # return sum
    
    # i=0
    # while i < len(numbers):
    #     sum += numbers[i]
#         i += 1
#     return sum
    
# print( addition(4,3,12,32) )

# multi-parameter in dictionary form
def addition(**numbers):
    sum=0
    for key, value in numbers.items():
        sum += value
    return sum

print(addition(first=89, second=30, third=20))