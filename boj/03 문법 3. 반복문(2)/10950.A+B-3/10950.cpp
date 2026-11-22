#include <iostream>

using namespace std;

int main(){
  int n;
  
  cin >> n;

  for(int T = 0; T < n; T++){
    int a, b;

    cin >> a >> b;

    cout << a + b << '\n';
  }
}