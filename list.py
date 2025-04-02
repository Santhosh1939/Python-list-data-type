# #1
# my_list=[10,20,30,40,50,11]
# my_list.reverse()
# print(my_list)

# #2

# # list1=[1,2,3,4,5]
# # list2=[4,5,6,7,8]
# # for i in list2:
# #     list1.append(i)
# # print(list1)

# #or

# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]

# common =[]
# for i in list1:
#     if i in list2:
#         common.append(i)
# print(common)

# #3

# original_list=[1,2,2,3,4,4,5]
# Unique=list(set(original_list))
# print(Unique)

# #4
# duplicate_list=[1,2,2,3,4,4,5]
# remove_dups= []

# for i in duplicate_list:
#     if i not in remove_dups:
#      remove_dups.append(i)
# print(remove_dups)   


# #5

# list1=[1,2,3,4]
# list2=["Vivian","Tesla","Honda"]
# list1.extend(list2)
# print(list1)


# #6

# list1=[1,2,3]
# repeat_list=[]
# for i in range(3):
#    repeat_list +=list1
# print(repeat_list)

# #7

# my_list1=[1,2,3,4,5,6,7,8,10]
# new_list=my_list1[1::2]
# print(new_list)

# #8

# natural=[13,14,15]
# insert_num=[10,11,12]
# natural.insert(0,insert_num)
# print(natural)

# #or

# natural=[13,14,15]
# insert_num=[10,11,12]
# insert_num = natural[:0]
# print(natural)

# #9

# print([i**2 for i in range(1,11)])

# #10
# print([i for i in range(2,21,2)])

# #11

# words=["apple","banana","cherry","date"]
# len_list = []

# for i in words:
#     len_list.append(len(i))
# print(len_list)


