
def maximumSubarraySum(nums, k):
        hash_t = {}
        inner_sum = 0
        res = 0
        l = 0

        for r in range(len(nums)):
            
            if nums[r] in hash_t and hash_t[nums[r]] >=l:
                #anything before the first intance of nums[r] is invalid
                l = hash_t[nums[r]]+1
                inner_sum = sum(nums[l:r])

            inner_sum += nums[r]
            hash_t[nums[r]] = r
            
            if r-l+1 == k:
                res = max(res, inner_sum)
                inner_sum -= nums[l]
                del hash_t[nums[l]]
                l+=1
        
        return res

            
            
print(maximumSubarraySum([18,9,9,12,12,18], 5))



ans = 0
current_sum = 0
begin = 0
end = 0
num_to_index = {}

while end < len(nums):
    curr_num = nums[end]
    last_occurrence = num_to_index.get(curr_num, -1)
    # if current window already has number or if window is too big, adjust window
    while begin <= last_occurrence or end - begin + 1 > k:
        current_sum -= nums[begin]
        begin += 1
    num_to_index[curr_num] = end
    current_sum += nums[end]
    if end - begin + 1 == k:
        ans = max(ans, current_sum)
    end += 1
return ans