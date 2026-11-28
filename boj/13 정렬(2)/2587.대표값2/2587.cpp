#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int s = 0;
  vector<int> arr(5);
  for(int i = 0; i < 5; i++){
    cin >> arr[i];
    s += arr[i]; 
  }

  sort(arr.begin(), arr.end());

  cout << (int) s / 5 << '\n';
  cout << arr[2];
}