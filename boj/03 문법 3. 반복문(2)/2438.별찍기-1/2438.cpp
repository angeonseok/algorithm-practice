#include <iostream>

using namespace std;

int main(){
  int n;
  cin >> n;

  for(int t = 1; t <= n; t++){
    for(int i = 0; i < t; i++)  cout << '*';
    cout << '\n';
  }
}