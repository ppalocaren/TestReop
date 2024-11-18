
#check if the first number in the list and the last number in the list are the same
def listname(numberlist):
    print("the list of numbers is ", numberlist)
    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False

number_x = [10, 20, 30, 40, 10]
print("The result is ", listname(number_x))

number_y = [75, 65, 35, 75, 30]
print("The result is ", listname(number_y))