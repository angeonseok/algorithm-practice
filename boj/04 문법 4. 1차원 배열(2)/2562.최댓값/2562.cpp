#include <iostream>
#include <vector>

using namespace std;

int main(){
  vector<int> arr(9);

  for(int i = 0; i < 9; i++)  cin >> arr[i];

  int ans = 0, idx = -1;
  for(int j = 0; j < 9; j++){
    if(arr[j] > ans){
      ans = arr[j];
      idx = j + 1;
    }
  }

  cout << ans << '\n' << idx;
}