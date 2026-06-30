#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> turn90(vector<vector<int>> arr){
  int n = arr.size();

  vector<vector<int>> r_arr(n, vector<int>(n));

  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      r_arr[i][j] = arr[n-j-1][i];
    }
  }

  return r_arr;
}

int T;

int main(){
  cin >> T;

  int n;
  for(int t = 1; t <= T; t++){
    cin >> n;
    vector<vector<int>> arr(n, vector<int>(n));
    
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        cin >> arr[i][j];
      }
    }

    auto arr90 = turn90(arr);
    auto arr180 = turn90(arr90);
    auto arr270 = turn90(arr180);

    cout << '#' << t << endl;

    for(int x = 0; x < n; x++){
      for(int y = 0; y < n; y++){
        cout << arr90[x][y];
      }
      cout << ' ';
      
      for(int y = 0; y < n; y++){
        cout << arr180[x][y];
      }
      cout << ' ';
      
      for(int y = 0; y < n; y++){
        cout << arr270[x][y];
      }
      cout << '\n';
    }
  }
}