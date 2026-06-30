/*1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
주어질 숫자는 30을 넘지 않는다.
*/

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