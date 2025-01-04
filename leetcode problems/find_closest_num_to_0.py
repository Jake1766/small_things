nums = [-4,-2,1,4,8]

def closest_to_zero(nums):
    distances = []
    closest = []
    for num in nums:
        if num < 0:
            distances.append(num * -1)
        else:
            distances.append(num)

    for distance in distances:

    print(distances)


print(closest_to_zero(nums))