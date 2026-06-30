#include <iostream>
#include <vector>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;
    vector<char> ans;

    for(int i = 0; i < n; i++){
      char c; int k;
      cin >> c >> k;

      for(int j = 0; j < k; j++){
        ans.push_back(c);
      }
    }

    cout << '#' << t << endl;

    int cnt = 0;
    for(auto p : ans){
      cout << p;
      cnt ++;

      if(cnt == 10){
        cout << '\n';
        cnt = 0;
      }
    }
    
    if(cnt != 0)
      cout << '\n';
  }
}