/*
HackerRank: Between Two Sets

You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

    1. The elements of the first array are all factors of the integer being considered
    2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

Sample Input:
2 3
2 4
16 32 96

Sample Output:
3

Explanation:
2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.

*/

#include <iostream>
#include <vector>

using namespace std;

int gcd(int a, int b) { 
    if (b == 0) 
        return a; 
    return gcd(b, a % b); 
}

int arrayLcm(vector<int> arr) { 
    int ans = arr[0]; 
    int n = arr.size();
    for (int i = 1; i < n; i++) 
        ans = (((arr[i] * ans)) / 
                (gcd(arr[i], ans))); 
  
    return ans; 
}

int arrayGcd(vector<int> arr) { 
    int result = arr[0];
    int n = arr.size();
    for (int i = 1; i < n; i++) 
        result = gcd(arr[i], result); 
  
    return result; 
} 

int getCount(vector<int> a, vector<int> b) {
    int count = 0;
    int lcm = arrayLcm(a);
    int gcd = arrayGcd(b);
    int k = lcm;
    for (int i = lcm; i <= gcd; i += lcm) {
        if (gcd%i==0) {
            count++;
        }
    }
    return count;
}

int main() {
    int m, n, input;
    vector<int> a,b;

    cout<<"Enter the size of the two arrays: ";
    cin>>m>>n;
    cout<<"Enter elements of the first array: ";
    for (int i = 0; i < m; i++) {
        cin>>input;
        a.push_back(input);
    }
    cout<<"Enter the elements of the second array: ";
    for (int i = 0; i < n; i++) {
        cin>>input;
        b.push_back(input);
    }
    cout<<"Count = "<<getCount(a,b);
}