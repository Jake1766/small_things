# https://leetcode.com/problems/count-operations-to-obtain-zero/description/

# code would benefit from heavy optimisation

# num1 and num2 are provided
# subtract smaller num from larger num
# repeat until 0 is reached
# return number of cycles taken to reach 0

#possible solution involves division

# fail case 137/161 passed:
# num1 = 0, num2 = 1

# fail case 148/167 passed
# num1 = 99999 num2 = 1


num1 = 2
num2 = 3


# output should be 0

def count_0(num1, num2):
    zero = False
    count = 0

    # check if either value is zero,
    # returns 0 if true as zero has been reached
    if num1 == 0 or num2 == 0:
        return count

    while not zero:
        if num1 <= num2:
            if num2 % num1 == 0:
                return (num2 / num1) + count
            num2 = num2 - num1
            print("num2 is: ", num2)

        else:
            if num1 % num2 == 0:
                return (num1 / num2) + count
            num1 = num1 - num2
            print("num1 is: ", num2)

        if num1 == 0 or num2 == 0:
            zero = True
        count += 1

        print("count = ", count)
    return count


def count2_0(num1, num2):

    if num1 > num2:
        numerator = num1
        denominator = num2
    else:
        numerator = num2
        denominator = num1
    quotient = numerator/denominator
    print(quotient)


print("function 1 output: ", int(count_0(num1, num2)))
