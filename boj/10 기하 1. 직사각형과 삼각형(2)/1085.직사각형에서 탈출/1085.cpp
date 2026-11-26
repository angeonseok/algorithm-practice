#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int x, y, w, h;
    cin >> x >> y >> w >> h;

    int arr[4] = {w - x, h - y, x, y};
    cout << *min_element(arr, arr + 4);
}