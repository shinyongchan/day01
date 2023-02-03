## 함수 선언 부분 ##
def print_poly(px):
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        if (coef > 0 and i > 0):
            polyStr += "+"
            polyStr += f'{coef}x^{term}'
            term -= 1
        elif (coef < 0 or i == 0):
            polyStr += f'{coef}x^{term}'
            term -= 1
        else:
            term -= 1






    return polyStr


def calc_poly(xValue, px):
    retValue = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        retValue += coef * xValue ** term
        term -= 1

    return retValue


## 전역 변수 선언 부분 ##
px = [7, -4, 6, 2]  # =

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_poly(px)
    print(pStr)

    xValue = int(input("X 값 : "))

    print(calc_poly(xValue, px))


