#include <iostream>

using namespace std;

int T;

int main(){
  cin >> T;
  for(int t = 1; t <= T; t++){
    int l, u, x;
    cin >> l >> u >> x;

    int ans = 0;
    if(x < l) ans = l - x;
    else if(x > u) ans = -1;
    else ans = 0;

    cout << '#' << t << ' ' << ans << endl;
  }
}