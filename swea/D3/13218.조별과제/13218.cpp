#include <iostream>

using namespace std;

int T;

int main(){
  cin >> T;
  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;

    cout << '#' << t << ' ' << n / 3 << endl;
  }
}