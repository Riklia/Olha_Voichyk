def filter_list(lst):
    return [el for el in lst if type(el) == int]


if __name__ == "__main__":
    if filter_list([1,2,'a','b']) == [1,2]:
        print("filter_list([1,2,'a','b']) == [1,2]")
    if filter_list([1,'a','b',0,15]) == [1,0,15]:
        print("filter_list([1,'a','b',0,15]) == [1,0,15]")
    if filter_list([1,2,'aasf','1','123',123]) == [1,2,123]:
        print("filter_list([1,2,'aasf','1','123',123]) == [1,2,123]")