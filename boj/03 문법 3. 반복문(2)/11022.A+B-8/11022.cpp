#include <iostream>

using namespace std;

int main(){
  int n;
  cin >> n;

  for(int t = 0; t < n; t++){
    int a, b;
    cin >> a >> b;

    cout << "Case #" << t + 1 << ": ";
    cout << a << " + " << b << " = " << a + b << '\n';
  }
}