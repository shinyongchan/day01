

def add_data(pokemon):
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon

def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가


    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가

def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)

    pokemons[idx] = None  # 데이터 삭제
    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제
    # for i in range(idx + 1, len_pokemons):
    #     pokemons[i - 1] = pokemons[i]
    #     pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[len_pokemons - 1])

pokemons = []
menu =-1

if __name__ == "__main__":
    while (menu != 4):

        menu = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if (menu == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (menu == 2):
            idx = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(idx, data)
            print(pokemons)
        elif (menu == 3):
            idx = int(input("삭제할 위치--> "))
            delete_data(idx)
            print(pokemons)
        elif (menu == 4):
            print(pokemons)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue





