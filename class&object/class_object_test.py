
class Weapon:
    def prick(self, obj):  # 这是该装备的主动技能,扎死对方
        obj.life_value -= 500  # 假设攻击力是500

class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name, atk, life_value):
        self.name = name  # 每一个角色都有自己的昵称;
        self.atk = atk  # 每一个角色都有自己的攻击力;
        self.life_value = life_value  # 每一个角色都有自己的生命值;
        self.weapon = Weapon()  # 给角色绑定一个武器;

    def walk(self):
        print(self.name + ' is walking...')


    def attack(self, dog):
        # 人可以攻击狗，这里的狗也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_value -= self.atk


class Dog:  # 定义一个狗类
    role = 'dog'  # 狗的角色属性都是狗

    def __init__(self, name, breed, atk, life_value):
        self.name = name  # 每一只狗都有自己的昵称;
        self.breed = breed  # 每一只狗都有自己的品种;
        self.atk = atk  # 每一只狗都有自己的攻击力;
        self.life_value = life_value  # 每一只狗都有自己的生命值;

    def bite(self, people):
        print('dog bites the person')
        # 狗可以咬人，这里的狗也是一个对象。
        # 狗咬人，那么人的生命值就会根据狗的攻击力而下降　　　　
        people.life_value -= self.atk


print(Person.role)  # 查看人的role属性
print(Person.walk)  # 引用人的走路方法，注意，这里不是在调用

egg = Person('egon', 10, 1000)  # 类名()就等于在执行Person.__init__()
# 执行完__init__()就会返回一个对象。这个对象类似一个字典，存着属于这个人本身的一些属性和方法。
# 你可以偷偷的理解：egg = {'name':'egon','walk':walk}

ha2 = Dog('二愣子', '哈士奇', 10, 1000)  # 创造了一只实实在在的狗ha2
print('二哈初始血量：' + str(ha2.life_value))        # 看看ha2的生命值
egg.attack(ha2)               # egg打了ha2一下
print('二哈血量:' + str(ha2.life_value))         # ha2掉了10点血