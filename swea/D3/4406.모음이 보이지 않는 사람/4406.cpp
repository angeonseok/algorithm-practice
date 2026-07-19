#include <iostream>
#include <string>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    string text;
    cin >> text;

    string ans = "";
    for (auto a : text){
      if(string("aeiou").find(a) == string::npos) ans += a;
    }

    cout << '#' << t << ' ' << ans << '\n';
  }
}