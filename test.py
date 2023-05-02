nums = [150,24,79,50,88,345,3]
target = 200

lowerindex = 0
higherindex = len(nums) - 1
nums = sorted(nums)


while higherindex -1 < len(nums) - 1 and lowerindex <= len(nums) - 1:

    tempsum = nums[lowerindex] + nums[higherindex]
    print(lowerindex, higherindex, tempsum)

    if tempsum == target:
        print(lowerindex, higherindex, tempsum)

    if target >= 0:
        if tempsum > target:
            tempsum = nums[lowerindex] + nums[higherindex - 1]
            print(lowerindex, higherindex - 1, tempsum)
            if tempsum == target:
                print(lowerindex, higherindex - 1, tempsum)
            higherindex -= 1

        if tempsum < target:
            tempsum = nums[lowerindex + 1] + nums[higherindex]
            print(lowerindex + 1, higherindex, tempsum)
            if tempsum == target:
                print(lowerindex, higherindex)
            lowerindex = lowerindex + 1

    else:
        if tempsum < target:
            tempsum = nums[lowerindex] + nums[higherindex - 1]
            print(lowerindex, higherindex - 1, tempsum)
            if tempsum == target:
                print(lowerindex, higherindex - 1, tempsum)
            higherindex -= 1

        if tempsum > target:
            tempsum = nums[lowerindex + 1] + nums[higherindex]
            print(lowerindex + 1, higherindex, tempsum)
            if tempsum == target:
                print(lowerindex, higherindex)
            lowerindex = lowerindex + 1
