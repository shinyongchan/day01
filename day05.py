# lambda function
import random

def process(no_list, f) :
    for no in no_list :
        print(f(no))



numbers = [ random.randint(1,100) for i in range(5)]
print(numbers)
process(numbers,lambda x : x*x)



# function as parameter
# import random
#
# def process(no_list, f) :
#     for no in no_list :
#         print(f(no))
#
# def squares(n):
#     '''
#     제곱 함수
#     :param n: integer
#     :return: integer
#     '''
#
#     return n*n
#
# numbers = [ random.randint(1,100) for i in range(5)]
# print(numbers)
# process(numbers,squares)



