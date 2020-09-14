/*
HackerRank: Breaking the record
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array .
Given Maria's scores for a season, find and print the number of times she breaks her records for most and least points scored during the season.

Input Format:
The first line contains an integer , the number of games.
The second line contains  space-separated integers describing the respective values of .

Output Format:
Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.

Sample Input:
9
10 5 20 20 4 5 2 25 1

Sample Output:
2 4
*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> brokenRecords(vector<int> scores) {
    int max = scores[0], min = scores[0];
    vector<int> count(2,0);
    vector<int>::iterator ptr;

    for (ptr = scores.begin(); ptr < scores.end(); ptr++)
    {
        if (*ptr < min) {
            min = *ptr;
            count[1]++;
        } else if (*ptr > max) {
            max = *ptr;
            count[0]++;
        }
    }
    return count;
}

int main() {
    int n, max, min, input;
    vector<int> scores;

    cin>>n;
    for (int i = 0; i < n; i++) {
        cin>>input;
        scores.push_back(input);
    }
    
    vector<int> result = brokenRecords(scores);
    cout<<result[0]<<" "<<result[1];
}