# https://leetcode.com/problems/count-operations-to-obtain-zero/description/

# num1 and num2 are provided
# subtract smaller num from larger num
# repeat until 0 is reached
# return number of cycles taken to reach 0

num1 = 99999
num2 = 1

# output should be 0

def count_0(num1, num2):
    zero = False
    count = 0
    if num1 == 0 and num2 == 0:
        return 0

    while not zero:
        if num1 <= num2:
            num2 = num2 - num1
        else:
            num1 = num1 - num2

        print("num1: ", num1, "\nnum2: ", num2)
        count += 1

        if num1 == 0 or num2 == 0:
            zero = True
    print("count = ", count)
    return count

count_0(num1, num2)