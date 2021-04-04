# list1 = [1, 2, 3,4,5]
# # for i in list1:
# #     print(list1[1:3:2])

# a =3
# b=2
# # x=2
# result = lambda x:x+1
# print(result(4))
# print(lambda b, x=b:test(x, b))

# str_a ="abcdefghijk"
# # print(str_a[1:7:2])
# result = 0
# for i in range(1,101):
#     if i %2 == 0:
#         result =result + i
# print(result)

# a = 1
# while a<10:a = a+1
# print(a)

# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)

# import random
#
# computer_num = random.randint(1, 100)

# while True:
# #     input_num = int(input("请输入一个数字："))
# #     if input_num < computer_num:
# #         print("输入的值小了")
# #     elif input_num > computer_num:
# #         print("输入的值大了")
# #     else:
# #         print("你猜对了")
# #         break

# def fun2(a, b, c, d):
#     print("a的值为", a)
#     print("b的值为", b)
#     print("c的值为", c)
#     print("d的值为", d)
#
# fun2(1, 2, 3, 4)
#
# fun3 = lambda x: x + 2
# print(fun3(2))

# list =[]
# for i in range(4):
#     list.append(i**2)
# print(list)

# list =[i**2 for i in range(1,6)]
# # print(list)

# list = []
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i}*{j} =", i * j)

# a ={i for i in "abcdefghijklm" }
# print(type(a))

# b = {i: i + 2 for i in range(1, 3)}
# # print(type(b))
# name = "zhangsan"
# age = 6
# # print('My name is %s,I am %d years old' % (name, age))
# # print('my name is {},I am {}years old'.format(name,age))
#
# f = open('data.txt')


# print(f.readlines())
# print(f.readline())
# # f.close()

# with open('data.txt')  as f:
#     print(f.readlines())

# import json
# try:
#     num1 = 1
#     num2 = 1
#     print(num1 / num2)
# # except ZeroDivisionError:
# #     print("不能除0")
# except:
#     print("异常了")
# finally:
#     print("hhhhhaaaaa")


class Hero(object):
    xl = 0
    gj = 0
    name = ""

    # def __init__(self):
    #     if __name__ == '__main__':
    #         name = self.__class__.__name__
    #         Hero.name = name
    #         print(name)

    def getClassName(self):
        if __name__ == '__main__':
            Hero.name = self.__class__.__name__
            print(Hero.name)
            return Hero.name

    def fight(self, enemy_xl, enemy_gj):
        self.name = Hero.getClassName
        print(self.name)
        my_fxl = self.xl - enemy_gj
        enemy_fxl = enemy_xl - self.gj
        if my_fxl > enemy_fxl:

            print(self.__class__.__name__, "我赢了")
        elif my_fxl < enemy_fxl:
            print( "敌人赢了")
        else:
            print("打平了")


class Hero1(Hero):
    xl = 1100
    gj = 1000


class Hero2(Hero):
    xl = 2000
    gj = 1100


# H = Hero()
# H.getClassName()


H1 = Hero1()
H2 = Hero2()
H1.fight(Hero2.xl, H2.gj)
