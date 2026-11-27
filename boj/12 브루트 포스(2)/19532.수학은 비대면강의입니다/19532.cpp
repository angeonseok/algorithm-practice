#include <iostream>

using namespace std;

int main(){
    int a, b, c, d, e, f;
    cin >> a >> b >> c >> d >> e >> f;

    bool flag = false;
    for(int i = -999; i < 1000; i++){
        for(int j = -999; j < 1000; j++){
            int x = a * i + b * j;
            int y = d * i + e * j;

            if(x == c && y == f){
                flag = true;
                cout << i << ' ' << j;
                break;
            }
        }
        if(flag)    break;
    }
}