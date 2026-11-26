#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;

    int arr[3] = {a, b, c};
    sort(arr, arr + 3);

    if(arr[2] >= arr[0] + arr[1])   cout << (arr[0] + arr[1]) * 2 - 1;
    else cout << arr[0] + arr[1] + arr[2];
}