#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int T;
string score[10] = {
        "A+", "A0", "A-",
        "B+", "B0", "B-",
        "C+", "C0", "C-",
        "D0"
    };

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int n, k;
    cin >> n >> k;

    vector<pair<double, int>> arr;

    for(int i = 0; i < n; i++){
      int a, b ,c;
      cin >> a >> b >> c;

      double total = a * 0.35 + b * 0.45 + c * 0.2;
      arr.push_back({total, i+1});
    }

    sort(arr.begin(), arr.end(), greater<pair<double,int>>());

    int rank = 0;
    for(int i = 0; i < n; i++){
      if(arr[i].second == k){
        rank = i;
        break;
      }
    }

    int cut = n / 10;

    cout << '#' << t << ' ' << score[rank / cut] << '\n';
  }
}
