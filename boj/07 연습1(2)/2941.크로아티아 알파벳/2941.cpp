#include <iostream> 
#include <string> 
#include <vector>

using namespace std;

vector<string> c_alpha = {
  "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="
};

int main(){
  string s;
  cin >> s;

  for(int i = 0; i < 8; i++){
    while(true){
      int n = s.find(c_alpha[i]);

      if(n == string::npos) break;
      
      s.replace(n, c_alpha[i].size(), "#");
    }
  }

  cout << s.length();
}