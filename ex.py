#ex 3.4

number = list(map(int, input("세 정수를 입력하시오 : ").split(' ')))

if number [0] > number [1] :
    if number [0] > number [2] and number[1] > number [2]:
        print(number[0], number[1], number[2],)
    else :
        print(number[0], number[2], number[1], )
elif number [1] > number[2] :
    if number [2] > number[0] :
        print(number[1], number[2], number[0], )
    else :
        print(number[1], number[0], number[2], )
else :
    if number [0] > number [1] :
        print(number[2], number[0], number[1], )
    else :
        print(number[2], number[1], number[0], )