## 함수 선언 부분 ##
def print_poly(px, tx):
                             # 최고차항 숫자 = 배열길이-1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수
        term = tx[i]
        if (coef > 0 and i > 0):
            polyStr += f'+{coef}x^{term}'

        elif (coef < 0 or i == 0) :
            polyStr += f'{coef}x^{term}'









    return polyStr


def calc_poly(xValue, px, tx):
    retValue = 0
    # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        term = tx[i]
        retValue += coef * xValue ** term

    return retValue


## 전역 변수 선언 부분 ##
px = [7, -4, 5]  # =
tx = [300, 20, 0]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_poly(px,tx)
    print(pStr)

    xValue = int(input("X 값 : "))

    print(calc_poly(xValue, px, tx))


