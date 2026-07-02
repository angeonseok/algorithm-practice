#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T;

int main(){
  cin >> T;
  
  for(int t = 1; t <= T; t++){
    int N, M;
    cin >> N >> M;

    vector<vector<int>> arr(N, vector<int>(N));
    for(int i = 0; i < N; i++){
      for(int j = 0; j < N; j++){
        cin >> arr[i][j];
      }
    }

    vector<vector<int>> prefix(N + 1, vector<int>(N+1));
    for(int i = 1; i < N+1; i++){
      for(int j = 1; j < N+1; j++){
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1];
      }
    }

    int ans = 0;
    for(int i = M; i < N+1; i++){
      for(int j = M; j < N+1; j++){
        int tmp = prefix[i][j] - prefix[i-M][j] - prefix[i][j-M] + prefix[i-M][j-M];

        ans = max(ans, tmp);
      }
    }

    cout << '#' << t << ' ' << ans << endl;
  }  
}