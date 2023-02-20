myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 1]


def count(the_list, x):
    var_count = 0
    for i in the_list:
        if i == x:
            var_count += 1
    return var_count


print(count(myList, 1))


def isin(the_list, x) -> bool:
    if x in the_list:
        return True


print(isin(myList, 5))


def index(the_list, x):
    for i in range(len(the_list)):
        if the_list[i] == x:
            return i


print(index(myList, 10))


def reverse(the_list):
    return the_list[-1::-1]


print(reverse(myList))


def sort(the_list):
    for i in range(len(the_list)):
        for j in range(i + 1, len(the_list)):
            if the_list[i] > the_list[j]:
                the_list[i], the_list[j] = the_list[j], the_list[i]
    return the_list
print(sort(myList))