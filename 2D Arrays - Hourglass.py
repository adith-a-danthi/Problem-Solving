'''
Hackerrank - 2D array DS
You are given a 2D array with dimensions 6*6. An hourglass in an array is defined as a portion shaped like this:
a b c
  d
e f g

For example, if we create an hourglass using the number 1 within an array full of zeros, it may look like this:
  1 1 1 0 0 0
  0 1 0 0 0 0
  1 1 1 0 0 0
  0 0 0 0 0 0
  0 0 0 0 0 0
  0 0 0 0 0 0
Actually, there are many hourglasses in the array above. The three topmost hourglasses are the following:
  1 1 1     1 1 0     1 0 0
    1         0         0
  1 1 1     1 1 0     1 0 0
The sum of an hourglass is the sum of all the numbers within it. The sum for the hourglasses above are 7, 4, and 2, respectively.
In this problem, you have to print the largest sum among all the hourglasses in the array.

Input Format:
There will be exactly 6 lines of input, each containing 6 integers separated by spaces. Each integer will be between -9 and 9, inclusively.

Output Format:
Print the answer to this problem on a single line.

Sample Input:
  1 1 1 0 0 0
  0 1 0 0 0 0
  1 1 1 0 0 0
  0 0 2 4 4 0
  0 0 0 2 0 0
  0 0 1 2 4 0

Sample Output:
19

Explanation:
The hourglass possessing the largest sum is:
2 4 4
  2
1 2 4

Sum = 2 + 4 + 4 + 2 + 1 + 2 + 4 = 19
'''

if __name__ == '__main__':
    arr = []
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    n = -9*7
    for i in range(4):
        for j in range(4):
            result = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            n = max(n, result)
    print(n)