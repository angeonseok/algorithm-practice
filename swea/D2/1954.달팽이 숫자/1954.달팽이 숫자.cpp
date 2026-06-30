#include <iostream>
#include <vector>

using namespace std;

int T;
int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;

    vector<vector<int>> arr(n, vector<int>(n, 0));
    int x = 0, y = 0, d = 0, cnt = 1;

    for(int i = 0; i < n * n; i++){
      arr[x][y] = cnt;
      
      int nx = x + dir[d][0];
      int ny = y + dir[d][1];

      if((nx >= 0 && nx < n) && (ny >= 0 && ny < n) && arr[nx][ny] == 0){
        x = nx;
        y = ny;
      }
      
      else{
        d = (d + 1) % 4;
        x = x + dir[d][0];
        y = y + dir[d][1];
      }

      cnt ++;
    }

    cout << '#' << t << endl;
    for(int x = 0; x < n; x++){
      for(int y = 0; y < n; y++){
        cout << arr[x][y] << ' ';
      }

      cout << '\n';
    }
  }
}