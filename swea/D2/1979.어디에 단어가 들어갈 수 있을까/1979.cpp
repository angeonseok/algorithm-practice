#include <iostream>
#include <vector>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int N, K;
    cin >> N >> K;

    vector<vector<int>> arr(N, vector<int>(N));
    for(int i = 0; i < N; i++){
      for(int j = 0; j < N; j++){
        cin >> arr[i][j];
      }
    }

    int ans = 0;
    for(int i = 0; i < N; i++){
      int cnt = 0;
      for(int j = 0; j < N; j++){
        if(arr[i][j] == 1){
          cnt++;
        }
        else{
          if(cnt == K){
            ans ++;
          }
          cnt = 0;
        }
      }
      if(cnt == K)
        ans++;
    }
    
    for(int i = 0; i < N; i++){
      int cnt = 0;
      for(int j = 0; j < N; j++){
        if(arr[j][i] == 1){
          cnt++;
        }
        else{
          if(cnt == K){
            ans ++;
          }
          cnt = 0;
        }
      }
      if(cnt == K)
        ans++;
    }

    cout << '#' << t << ' ' << ans << endl;
  }
}