# Normal way: use recurrsive function to keep calling until reach the min steps
# def climbStairs(n):
#     if n == 1:
#         return 1
#
#     if n == 2:
#         return 1 + climbStairs(1)
#
#     return climbStairs(n-1) + climbStairs(n-2)


# Faster way: Dynamic Programming
# Starting from step 4 (index 3 in 0-based indexing), the algorithm calculates the number of ways to climb to the current step by adding up previous 1-step and 2-step steps
'''
Example
Step Index	 prev2  	prev1  	current
    4	         2	      3	       5
    5	         3	      5	       8
    6	         5	      8	       13
'''

def climbStairs(n):
    if n <= 3:
        return n

    prev1 = 3
    prev2 = 2
    current = 0

    for i in range(3, n):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return current


# n = 2 # 2
# n = 3 # 3
# n = 4 # 5
# n = 5 # 8
n = 6 # 13
# n = 44 # 1134903170
print(climbStairs(n))
