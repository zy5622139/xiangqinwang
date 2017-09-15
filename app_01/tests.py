from django.test import TestCase

# Create your tests here.
data=['alex',49,[1900,3,18]]
print(data[2][2])


# def func(strrr):
#     dict_list = {'num':0,'str':0,'space':0,'others':0}
#     for i in strrr:
#         if i.isalpha():
#             dict_list['str']+=1
#         elif i.isalnum():
#             dict_list['num']+=1
#         elif i.isspace():
#             dict_list['space']+=1
#         else:
#             dict_list['others']+=1
#     return dict_list
# print(func('asd23asd  123asd;#$%'))