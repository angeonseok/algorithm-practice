#include <iostream>
using namespace std;

int T;

int main(){
    cin >> T;

    for(int t = 1; t <= T; t++){
        int a = 0, b = 0, c = 0, d = 0, e = 0, n;
        cin >> n;

        while(n != 1){
            if(n % 2 == 0){
                a++;
                n /= 2;
            }
            
            else if(n % 3 == 0){
                b++;
                n /= 3;
            }
            
            else if(n % 5 == 0){
                c++;
                n /= 5;
            }
            
            else if(n % 7 == 0){
                d++;
                n /= 7;
            }
            
            else if(n % 11 == 0){
                e++;
                n /= 11;
            }
        }

        cout << '#' << t << ' ' << a << ' ' << b << ' ' << c << ' ' << d << ' ' << e << endl;
    }
}