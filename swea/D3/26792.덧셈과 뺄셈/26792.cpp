#include <iostream>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int X, Y;
    cin >> X >> Y;

    int a = (X + Y) / 2;
    int b = X - a;

    cout << a << ' ' << b << endl;
  }
}