# my_dict = {'a': "a", 'b': "c", 'c': 'b'}
#
# # 딕셔너리를 value 값으로 정렬
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
#
# # 정렬된 딕셔너리 출력
# for item in sorted_dict:
#     print(item[0], item[1])
my_dict = {'a': 3, 'c': 1, 'b': 2}

# 딕셔너리를 key 값으로 정렬
sorted_dict = sorted(my_dict.items())

# 정렬된 딕셔너리 출력
for item in sorted_dict:
    print(item[0], item[1])