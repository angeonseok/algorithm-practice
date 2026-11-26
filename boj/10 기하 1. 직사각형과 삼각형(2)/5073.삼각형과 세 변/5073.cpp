#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int a, b, c;

    while(cin >> a >> b >> c){
        if(a == 0 && b == 0 && c == 0)  break;

        int arr[3] = {a, b, c};
        sort(arr, arr + 3);

        if(arr[0] + arr[1] <= arr[2])   cout << "Invalid";
        else if(arr[0] == arr[1] && arr[1] == arr[2])   cout << "Equilateral";
        else if(arr[0] == arr[1] || arr[1] == arr[2] || arr[0] == arr[2])   cout << "Isosceles";
        else    cout << "Scalene";

        cout << '\n';
    }
}