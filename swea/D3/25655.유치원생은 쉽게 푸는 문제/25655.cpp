#include <iostream>
#include <string>

using namespace std;

int T; 

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int N;
    cin >> N;
    
    string ans;
    if(N == 1)
      ans = "0";
    else{
      if(N % 2 == 0)
      ans = string(N/2, '8');
      else{
        string tmp(N/2, '8');
        ans = "4" + tmp;
      }
    }

    cout << ans << endl;
  }
}