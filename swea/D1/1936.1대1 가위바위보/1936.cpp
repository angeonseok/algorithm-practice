#include <iostream>
using namespace std;

int a, b;

int main(){
    cin >> a >> b;

    if((a == 1 && b == 3) || (a == 2 && b == 1) || (a == 3 && b == 2))
        cout << 'A';
    else 
        cout << 'B';
}