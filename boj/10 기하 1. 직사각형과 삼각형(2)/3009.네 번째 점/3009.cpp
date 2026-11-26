#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int x[3] = {0};
    int y[3] = {0};

    for(int i = 0; i < 3; i++){
        cin >> x[i];
        cin >> y[i];
    }

    int x2, y2;
    for(int i = 0; i < 3; i++){
        if(count(x, x + 3, x[i]) == 1)  x2 = x[i];
        if(count(y, y + 3, y[i]) == 1)  y2 = y[i];
    }

    cout << x2 << ' ' << y2;
}