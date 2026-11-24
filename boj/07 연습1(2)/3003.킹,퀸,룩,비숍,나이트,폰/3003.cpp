#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> n = {1, 1, 2, 2, 2, 8};
    vector<int> arr(6, 0);

    for(int i = 0; i < 6; i++)  cin >> arr[i];

    for(int j = 0; j < 6; j++)  cout << n[j] - arr[j] << ' ';
}