#include <iostream>
#include <string>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){

    string s;
    cin >> s;
    
    for(int i = 1; i < 11; i++){
      bool flag = true;
      
      for(int l = i; l < 30; l++){
        if(s[l] != s[l - i]){
          flag = false;
          break;
        }
        
      }

      if(flag){
        cout << '#' << t << ' ' << i << endl;
        break;
      }
    }
  }
}