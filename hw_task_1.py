""" 1 """


def len_string(string):
    if isinstance(string, (str, list, dict, tuple, bytes, range, set, frozenset)):
        return print("Length of string: ", len(string))
    else:
        return print("Invalid type of string")


s = ""
len_string(s)

''' 2 '''


def len_list(list1, list2):
    if len(list1) > len(list2):
        return print("Lenght of first list ", len(list1))
    if len(list2) > len(list1):
        return print("Lenghth of second list ", len(list2))
    else:
        return print("The lengths of the lists are equal")


list_1 = [1, 2, 3, (1, 2)]
list_2 = [1, 4, 5]
len_list(list_1, list_2)

''' 3 '''


def sum_list(list1):
    # list4 = (1, 2)
    list4 = [1, 2, 3, 4]
    if isinstance(list4, list):
        return print("Sum of two lists ", list1 + list4)
    else:
        list1.append(list4)
        return print("New list ", list1)


list_3 = [1, (1, 2, 3), "er"]
sum_list(list_3)

''' 4 '''


def sign_of_number(num):
    if num < -100 or num > 100:
        print('-')
    else:
        print('+')


number = -20
sign_of_number(number)

''' 5 '''


def equal_list(str1, str2):
    if str1 in str2:
        print("YES")
    else:
        print("NO")


str_1 = 'test'
str_2 = 'test1'
equal_list(str_1, str_2)

''' 6 '''


def positive_numbers(list1):
    count = 0
    for i in list1:
        count += i > 0
    print("Number of positive numbers ", count)


list_4 = [1, -4, 6, -8, -10]
positive_numbers(list_4)

''' 7 '''


def number_of_days(years, month):
    print("Days: ", (years * 12 + month) * 29)
    # print(years * month * 29)


number_of_days(1, 1)

''' 8 '''


def split_str(str):
    count = ''
    try:
        for world in str.split():
            count += world[0]
        return print("Abbreviation", count)
    except Exception as ex:
        print("Error type of data")


str_3 = "Attendance at The exhibition was over Half a million"
split_str(str_3)

''' 9 '''


def factorial(number):
    n = number
    if number == 0:
        return print("Factorial: ", 1)
    while n > 1:
        number *= n - 1
        n -= 1
    return print("Factorial: ", number)


factorial(10)

''' 10 '''

lst = [2, 4, 5, 8, 9, 13]

n = len(lst)-1
while n >= 0:
    lst[n] *= n
    n -= 1
print(lst)
