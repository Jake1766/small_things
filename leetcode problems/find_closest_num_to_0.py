nums = [-4, -2, 1,-1, 4, 8]
nums2 = [-10000, -10000]
def closest_to_zero(nums):
    distances = []
    #create positive array
    for num in nums:
        if num < 0:
            num = num * -1
            distances.append(num)
        else:
            distances.append(num)

    #find closest value
    closest = distances[0]
    for distance in distances:
        if distance < closest:
            closest = distance

    #if + value exists return it
    if closest in nums:
        return closest
    else:
        return closest * -1

#using a single pass
def closest_to_zero2(nums):
    first_run = true
    closest = nums[0]
    for num in nums:







print(closest_to_zero(nums2))