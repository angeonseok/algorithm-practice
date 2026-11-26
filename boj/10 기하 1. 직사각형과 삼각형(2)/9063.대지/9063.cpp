#include <iostream>

using namespace std;

int main(){
    int n; 
    cin >> n;

    int max_x = -10001, max_y = -10001, min_x = 10001, min_y = 10001;
    int x, y;

    for(int i = 0; i < n; i++){
        cin >> x >> y;
        if(x > max_x)   max_x = x;
        if(x < min_x)  min_x = x;

        if(y > max_y)   max_y = y;
        if(y < min_y)   min_y = y;
    }

    cout << (max_x - min_x) * (max_y - min_y);
}