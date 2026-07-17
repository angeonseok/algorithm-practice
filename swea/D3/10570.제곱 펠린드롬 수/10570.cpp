#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int T; 

bool pal(int num){
  string s = to_string(num);
  string r(s.rbegin(), s.rend());
  return s == r;
}

int main(){
  cin >> T; 
  for(int t = 1; t <= T; t++){
    int a, b;
    cin >> a >> b;

    int cnt = 0;
    for(int i = (int)sqrt(a-1) + 1; i <= (int)sqrt(b); i++){
      if(pal(i) && pal(i * i)) cnt ++;
    }

    cout << '#' << t << ' ' << cnt << endl;
  }
}