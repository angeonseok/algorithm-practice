#include <iostream>

using namespace std;

int coin[4] = {25, 10, 5, 1};

int main(){
  int n;
  cin >> n;

  for(int i = 0; i < n; i++){
    int c;
    cin >> c;

    for(int j = 0; j < 4; j++){
      int a = c / coin[j];
      c %= coin[j];
      cout << a << ' ';
    }
    cout << '\n';
  }
}