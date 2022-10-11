# a = "hello"
# b = 12
# c = str(b)# str
# print(a+" "+c)
# chay duoc

# a = " hello"
# b = "12"
# c = "35"
# # "12" -> 12
# d = int(b) + int(c)
# #int: integer
# #str: string
# print(d)
# chay duoc

# a = "12"
# b = " 35"
# c = int(a)+ int(b)
# print(c)
#  chay duoc

# a = [1,3,6,-1,6,"hhaha",3+6]
# print(a[6])
# chay duoc

# a = [1,3,6,-1,6,"hhaha",3+6]
# size = len(a)
# last_index = size -1
# print(a[last_index])
# chay duoc

# a = 1
# b = 3
# c = 12
# d = 9
# e = 5
# f = 6
# arr = [1,3,12,9,5,6]
# print(arr)
# chay duoc

# # gan them phan tu vao mang
# arr = [1,3,12,9,5,6]
# arr.append(7)
# arr.append(1000)
# arr.append(-5000)
# print(arr)
# chay duoc

# arr = [1,3,12,9,5,6,7,1000,-5000]
# arr.remove(1000)
# print(arr)
# chay duoc
# # in ra chu so trong chuoi ky tu tren
# a = "xin chao"
# print(a[2])
# chay duoc
# # # in ra chu so trong chuoi ky tu tren
# a = " xinchao"
# b = a[0:5]
# print(b)
# chay duoc
# a = "xinchaoxinchaoxinchao"
# b = a[0:None]
# print(b)
# None = null = rong

# a = " xinchaohello"
#
#
# key = "11"
#
# index = a.find(key)
# index_2 = index + len(key)
# result = a[0:index_2]
# print(result)
# nếu trời mưa thì tôi sẽ nghỉ học
# if <dieu kien>:
#     thuc thi cau lenh
# >,<,>= : lon hon hoac bang, == : bang, !=: khac
# <= : nho hon
# if 1<2:
#     print("mot lon hon hai")
# if 2>1:
#     print("hai lon hon mot" )
# if 1>2:
#     print("mot lon hon hai")
#     print("sdsdasdad")
#     print("dadad")
# if 2>1:
#     print("hai lon hon mot")
#     print("hilo")
# if 2>1:
#     print("mot lon hon hai")
# else:
#     print("hai lon hon mot")
# a = 5
# b =10
#
# if a>b:
#     print("a > b")
# else:
#     print("a < b")

# a = 15
# b = 15
# if not ( a is b):
#     print("a khac b")
# else:
#     print("a bang b")
#  a = 10
#  b = 15
# if not (a is b):

# if 10>2 and 10-2 == 8:
#     print(" hom nay la mot ngay dep troi")
# else:
#     print("đạt hôi chân and hôi nách")

# 10 % 3 = 1
#
# 10 / 3 = 3  3 *3 = 9

# a =
# if a % 2 == 0:
#     print(a"là số chẵn")
# else:
#     print(a,"là số lẻ")
#
# đang sai chưa xong

# a = input("nhặp vào gí trị của a:")
# if a % 2 == 0:
#     print(a,"so chẵn")
# else:
#     print(a,"là sô lẻ")


# a = int(input("nhập vao số để kiểm tra: "))#str
# if a % 2 == 0:
#     print(a,"là số chẵn")
# else:
#     print(a,"là số lẻ")
#     chạy được

#xét học lực theo điểm

# diem = 9
# nếu điểm == 9 là loạt giỏi
# điểm  = 8 khá
# điểm = 7 tb
# điểm = 6 yếu
# điểm còn lại :óc chó
# if < điều kiện1>:
#     thực thi
# elif <điều kiện2>:
#     thực thi
# elif <điều kiện3>:
# else
# if  diem == 9:
#     print(" gioi")
# elif diem == 8:
#     print("khá")
# elif diem == 7:
#     print("trung bình")
# elif diem == 6:
#     print("yếu")
# else:
#     print("kém cỏi")
# chạy được

# diem = 10
# if diem == 9  :
#     print("giỏi")
# if

# diem = 10
# if diem >= 9:
#     print("giỏi")
# elif diem >=7:
#     print("khá")
# else:
#     print("yếu")
#  diem = 10
# if  diem == 9 or diem == 10:
#     print(" quá oki")
# elif diem == 8:
#     print("khá là oki")
# else:
#     print("không ổn lắm")

diem = 10
if diem >= 9:
    print("quá oki")
elif diem >=7:
    print("cũng bình thường ")
elif diem >2:
    print("không ổn lắm")
else:
    print("không được rồi")
    print("ai có thể")
