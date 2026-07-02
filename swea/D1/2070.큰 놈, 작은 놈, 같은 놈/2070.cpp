#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int t = 1; t <= T; t++){
        int a, b;
        cin >> a >> b;

        if(a > b){
            cout << '#' << t << ' ' << '>';
        }
        else if(a < b){
            cout << '#' << t << ' ' << '<';
        }
        else{
            cout << '#' << t << ' ' << '=';
        }

        cout << '\n';
    }
}