#include <iostream>
#include <string>
#include <bitset>

using namespace std;

string table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    string code;
    cin >> code;

    //글자마다 그에 대응하는 6자리 2진수로 변환 후, 모아두기
    string decode = "";
    for(int i = 0; i < code.length(); i++){
      bitset<6> b(table.find(code[i]));
      decode += b.to_string();
    }
    
    //8자리씩 잘라서 해독하기.
    string ans = "";
    for(int i = 0; i < decode.length(); i+=8){
      string tmp = decode.substr(i, 8);
      int n = stoi(tmp, nullptr, 2);
      ans += (char)n;
    }

    cout << '#' << t << ' ' << ans << endl;
  }
}