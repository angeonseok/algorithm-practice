#include <iostream>

using namespace std;

int T; 

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int a, b; 
    cin >> a >> b;

    int ans = (a >= 1 && a <= 9 && b >= 1 && b <= 9) ? a * b : -1;
    cout << '#' << t << ' ' << ans << endl;
  }
}