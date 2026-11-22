#include <iostream>

using namespace std;

int main(){
  int n, t, total = 0;
  
  cin >> n >> t;

  for(int T = 0; T < t; T++){
    int a, b;

    cin >> a >> b;
    total += a * b;
  }

  cout << ((total == n) ? "Yes":"No");
}