#include <iostream>

using namespace std;

int main(){
  int n;
  cin >> n;

  for(int t = 1; t <= n; t++){
    for(int i = n - t; i > 0; i--)  cout << ' ';
    for(int j = 0; j < t; j++)  cout << '*';
    cout << '\n';
  }
}