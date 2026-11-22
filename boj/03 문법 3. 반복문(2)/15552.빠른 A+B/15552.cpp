#include <iostream>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  
  cin >> n;

  for(int tc = 0; tc < n; tc++){
    int a, b;

    cin >> a >> b;

    cout << a + b << '\n';
  }
}