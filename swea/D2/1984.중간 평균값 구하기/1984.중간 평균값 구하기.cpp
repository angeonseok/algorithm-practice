#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int T;

int main(){
    cin >> T;

    for(int t = 1; t <= T; t++){
        int arr[10], a;

        for(int i = 0; i < 10; i++)
            cin >> arr[i];
        
        sort(arr, arr+10);

        int total = 0;
        for(int i = 1; i < 9; i++)
            total += arr[i];

        cout << '#' << t << ' ' << round((double)total / 8) << endl;
    }
}