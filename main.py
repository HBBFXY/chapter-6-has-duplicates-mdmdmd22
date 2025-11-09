def has_duplicates(lst):
    # 将列表转换为集合，集合会自动去除重复元素
    unique_set = set(lst)
    # 如果列表长度大于集合长度，说明有重复元素
    return len(lst) > len(unique_set)

# 测试用例
test_list1 = [1, 2, 3, 4, 5]
print(f"列表 {test_list1} 是否有重复元素：{has_duplicates(test_list1)}")

test_list2 = [1, 2, 2, 3, 4]
print(f"列表 {test_list2} 是否有重复元素：{has_duplicates(test_list2)}")

test_list3 = ["a", "b", "b", "c"]
print(f"列表 {test_list3} 是否有重复元素：{has_duplicates(test_list3)}")
