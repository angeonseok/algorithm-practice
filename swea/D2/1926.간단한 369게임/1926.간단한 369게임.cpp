#include <iostream>
#include <string>

using namespace std;

int main(){
  int n;
  cin >> n;

  for(int i = 1; i <= n; i++){
    string s = to_string(i);
    int cnt = 0;

    for(char c : s){
      if(c == '3' || c == '6' || c == '9')
        cnt ++;
    }
    
    if(cnt > 0)
      cout << string(cnt, '-') << ' ';
    
    else
      cout << s << ' ';
  }
}