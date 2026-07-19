#include <iostream>
#include <vector>

using namespace std;

int T;

int main(){
  cin >> T;
  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;

    vector<int> arr(n);
    
    int avg = 0;
    for(int i = 0; i < n; i++){
      cin >> arr[i];
      avg += arr[i];
    }
    avg /= n;

    int cnt = 0;
    for(auto x : arr){
      if(x <= avg) cnt++;
    }

    cout << '#' << t << ' ' << cnt << endl;
  }
}