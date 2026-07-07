#include <iostream>
#include <string>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    string s;
    cin >> s;

    char tmp = '0';
    int cnt = 0;
    for(int i = 0; i < s.length(); i++){
      if(tmp != s[i]){
        cnt++;
        tmp = s[i];
      }
    }

    cout << '#' << t << " " << cnt << endl;
  }
}