# class Matrix:
#     def __init__(self, el1, el2):
#         self.el1 = el1
#         self.el2 = el2
#
#     def __add__(self):
#         matr = [[0, 0, 0, 0],
#                 [0, 0, 0, 0],
#                 [0, 0, 0, 0]]
#
#         for i in range(len(self.el1)):
#
#             for j in range(len(self.el2[i])):
#                 matr[i][j] = self.el1[i][j] + self.el2[i][j]
#
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))
#
# my_matrix = Matrix([[5, 18, 11,0],
#                     [6, 17, 23,0],
#                     [41, 23, 23, 0]],
#                    [[1, 3, 23, 0],
#                     [43, 3, 24, 0],
#                     [23, 5, 3, 0]])
# print(my_matrix.__add__())
#2
# class Silk:
#     def __init__(self, size, height):
#         self.size = size
#         self.height = height
#
#     def get_v(self):
#         return self.size / 6.5 + 0.5
#
#     def get_h(self):
#         return self.height * 2 + 0.3
#
#     @property
#     def getall(self):
#         return str(f'Погонных метров\n'
#                    f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
#
#
# class Pullover(Silk):
#     def __init__(self, size, height):
#         super().__init__(size, height)
#         self.v = round(self.size / 6.5 + 0.5)
#
#     def __str__(self):
#         return f'кол-во материала на свитер {self.v}'
#
# class Pants(Silk):
#     def __init__(self, size, height):
#         super().__init__(size, height)
#         self.h = round(self.height * 2 + 0.3)
#
#     def __str__(self):
#         return f'кол-во материала на брюки {self.h}'
#
# pull = Pullover(23, 32)
# pants = Pants(31, 34)
# print(pull)
# print(pants)
# print(pull.getall)
# print(pants.getall)
# print(pants.get_v())
# print(pants.get_h())
#3
# class Count:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#
#     def __str__(self):
#         return f'Результат операции {self.quantity * "*"}'
#
#     def __mul__(self, other):
#         return Count(int(self.quantity * other.quantity))
#
#     def __truediv__(self, other):
#         return Count(round(self.quantity // other.quantity))
#
#
#     def make_order(self, count_line):
#         line = ''
#         for i in range(int(self.quantity / count_line)):
#             line += f'{"*" * count_line} \\n'
#         line += f'{"*" * (self.quantity % count_line)}'
#         return line
# count1 = Count(40)
# count2 = Count(2)
# print(count1)
# print(count2.make_order(6))
# print(count1.make_order(13))
# print(count1 / count2)
print(count1*count2)