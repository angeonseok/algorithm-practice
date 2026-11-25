#include <iostream>

using namespace std;

int main(){
    int x, cnt = 0, line = 0, a, b;
    cin >> x;

    while(cnt < x){
        line++;
        cnt += line;

        int end = cnt - x;
        
        if(line % 2 == 0){
            a = line - end;
            b = end + 1;
        }
        else{
            a = end + 1;
            b = line - end;
        }
    }

    cout << a << '/' << b;
}