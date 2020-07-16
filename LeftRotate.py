# Hackerrank - Arrays: Left Rotation
# Given an array 'a' of 'n' integers and a number, 'd', perform d left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers.

# Sample Input:
# 5 4
# 1 2 3 4 5

# Sample Output:
# 5 1 2 3 4

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    n = d%len(a)
    result = a[n:] + a[:n]

    print(' '.join(map(str, result)))
    

