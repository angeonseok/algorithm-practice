/*주어진 숫자만큼 # 을 출력해보세요.
주어질 숫자는 100,000 이하다.*/

#include <iostream>
using namespace std;

int main(){
    int n; 
    cin >> n;

    for(int i = 0; i < n; i++){
        cout << '#';
    }
}