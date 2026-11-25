#include <iostream>
#include <string>

using namespace std;

string digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main(){
  int n, b;
  string ans = "";
  cin >> n >> b;

  while(n > 0){
    ans = digit[n % b] + ans;
    n /= b;
  }

  cout << ans;
}