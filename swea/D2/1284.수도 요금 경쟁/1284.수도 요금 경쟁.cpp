#include <iostream>
#include <algorithm>

using namespace std;

int T;

int main() {
  cin >> T;

  for(int t = 1; t <= T; t++){
    int p, q, r, s, w;
    cin >> p >> q >> r >> s >> w;
    
    int c_a = p * w;

    int c_b = 0;
    if(w >= r)
      c_b = q + s * (w - r);
    
    else
      c_b = q;

    cout << '#' << t << ' ' << min(c_a, c_b) << endl;
  }
}