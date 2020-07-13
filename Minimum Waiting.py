'''
One day there are N customers standing in a line so that they can buy a mobile. For each customer who is waiting in line, 
the owner knows that he needs time arr[i] to server that customer. He doesn't want to dissapoint the customers in line.
A customer is dissapointed only if he waits more than the time needed to serve him.
The time a customer needs to wait is the total time when all the customers standing in front of him in line are tended to.
Find the order such that the number of dissapointed customers are minimum.

Input Format:
First line contains the value N. i.e., Number of customers
Second Line contains N space seperated integers representing the time required to serve that customer.

Output Format:
Single integer value depecting the number of satisfied customers (customers who aren't dissapointed) in the queue.

Example:
Sample Input
5
31 2 9 20 6

Sample Output
4

Explanation:
2, 6, 9, 20, 31
The customers can be arranged in the above order to reduce dissapointment
'''

n = int(input())
arr = list(map(int, input().rstrip().split()))

arr.sort()

count, max, sum = 0,0,0

for i in range(n):
    for j in range(i):
        if arr[i] > sum:
            count += 1
            sum += arr[j]
    if count > max:
        max = count
    count, sum = 0,0

print(max)