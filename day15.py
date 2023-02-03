friends = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

def add_data(friens, friend):

    for i in range(len(friends)):
        if friends[i][1] <= friend[1]:
            friends.insert(i, friend)
            break
        elif i == len(friends)-1:
            friends.append(friend)
            break


name = str(input("이름 :"))
cnt = int(input("횟수 : "))
friend = (name, cnt)

add_data(friends,friend)
print(friends)
