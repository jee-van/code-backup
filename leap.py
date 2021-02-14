# The function is expected to return an integer.
# The function accepts an integer as parameter.

from math import ceil

def logic(my_input):

    sum = 0

    while True:

        nums = list(map(int, str(my_input)))
        if len(nums)%2 == 0:
            for n in range(ceil(len(nums)/2)):
                sum += (nums[n]*nums[len(nums)-n-1])
        else:
            for n in range(ceil(len(nums)/2)):
                if n == len(nums)//2:
                    sum += nums[n]
                else:
                    sum += (nums[n]*nums[len(nums)-n-1])
        
        if len(str(sum))>1:
            
            my_input = sum
            sum = 0
        else:
            break
        
        
    return sum
    


# Do not edit below

# Get the input
my_input = int(input())

# Print output returned from the logic function
print(logic(my_input))
