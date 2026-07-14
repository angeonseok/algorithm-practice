#include <iostream>
#include <vector>
#include <string>

using namespace std;

int T;
int dir[4][2] = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){

    int n;
    cin >> n;
    
  vector<string> arr(n);
  for(auto& a : arr)  cin >> a;
  
  bool flag = false;
  for(int i = 0; i < n &&  !flag; i++){
    
    for(int j = 0; j < n && !flag; j++){
      
      for(auto& x : dir){
        int k;
        for(int k = 0; k < 5; k++){
          int ni = i + x[0] * k;
          int nj = j + x[1] * k;

          if (ni < 0 || ni >= n || nj < 0 || nj >= n || arr[ni][nj] != 'o')
          break;
          
          if(k == 4){
            flag = true;
            break;
            }
          }
        }
      }
    }
    cout << '#' << t << ' ' << (flag ? "YES":"NO") << '\n';
  }
}