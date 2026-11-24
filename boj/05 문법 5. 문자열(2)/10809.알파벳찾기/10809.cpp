#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    string s;
    cin >> s;

    vector<int> arr(26, -1);
    for(int i = 0; i < s.size(); i++){
        int a = s[i] - 'a';

        if(arr[a] == -1)    arr[a] = i;
    }

    for(int j = 0; j < 26; j++) cout << arr[j] << ' ';
}