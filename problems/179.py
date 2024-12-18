class LargerNumKey(str):
    def __lt__(x, y):
        # Compare x+y with y+x in reverse order to get descending order
        return x+y > y+x

def largestNumber(nums):
    # Convert the list of numbers to list of strings
    nums = [str(num) for num in nums]
    
    # Sort the list of strings using our custom sorting function
    print(nums)
    nums.sort(key=LargerNumKey)
    print(nums)
    # Join the sorted list of strings to form the final result
    largest_num = ''.join(nums)
    
    # If the largest number is 0, return "0"
    # Otherwise, return the largest number
    return "0" if largest_num[0] == "0" else largest_num
    
print(largestNumber([3,30,34,5,9]))
