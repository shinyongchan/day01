# class inheritance

class Pokemon:
    def __init__(self, name, owner, skills):  # 객체 생성 시 동작
        print(f'포켓몬 {name} 생성됨 ')
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')

    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}, 기술은 {self.skills}입니다.')
        for skill in self.skills :
            print(skill)
class Pikachu(Pokemon) : # inheritance
    pass
pi1 = Pikachu('피카츄', '덴트', '번개')
pi1.info()
p1 = Pokemon('피카츄', '한지우','50만 볼트/100만 볼트/번개')
p2 = Pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
