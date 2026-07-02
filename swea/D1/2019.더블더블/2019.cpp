#include <iostream>
using namespace std;

int n;
int main(){
    cin >> n;

    for(int i = 0; i <= n; i++){
        int a = 1;
        for(int j = 0; j < i; j++){
            a *= 2;
        }

        cout << a << ' ';
    }
}