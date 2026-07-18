#include <iostream>
#include <string>

using namespace std;

int T;

int main(){
  cin >> T;
  for(int t = 1; t <= T; t++){
    string cmd;
    cin >> cmd;

    int a = 1, b = 1;
    for(int i = 0; i < cmd.length(); i++){
      if(cmd[i] == 'L') b += a;
      else a += b;
    }
    
    cout << '#' << t << ' ' << a << ' ' << b << endl;
  }
}