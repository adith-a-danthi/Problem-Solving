
# HackerRank - Jumping on the Clouds
# Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. 
# She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. She must avoid the thunderheads. 
# Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.
# For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided

# Sample Input: 
# 7
# 0 0 1 0 0 1 0

# Sample Output: 
# 4

# Explanation:
# Emma must avoid clouds at index 2 and 5. She can win the game with a minimum of 4 jumps.
 
n = int(input())
arr = list(map(int, input().rstrip().split()))

jumps = 0
i = 0

while i < n-1:
    if i+2 < n and arr[i+2] == 0:
        i+=2
    else:
        i+=1
    jumps+=1

print("Jumps: ", jumps)