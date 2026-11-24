#include <iostream>
#include <string>

using namespace std;

int main(){
  string s;
  cin >> s;

  int cnt[26] = {0};
  for(int i = 0; i < s.size(); i++) cnt[toupper(s[i]) - 'A']++;

  int idx = 0, max_cnt = 0;
  bool ok = false;
  
  for(int i = 0; i < 26; i++){
    if(cnt[i] > max_cnt){
      max_cnt = cnt[i];
      idx = i;
      ok = false;
    }
    else if(cnt[i] == max_cnt){
      ok = true;
    }
  }

  cout << ((ok) ? '?':(char)('A' + idx));
}