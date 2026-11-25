#include <iostream>

using namespace std;

int main(){
    int n, depth = 1, i = 1;
    cin >> n;

    while(depth < n){
        depth += 6 * i;
        i++;
    }

    cout << i;
}