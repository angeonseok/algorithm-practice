#include <iostream>
#include <vector>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  vector<int> arr(10001);
  for(int i = 0; i < n; i++){
    int a;  cin >> a;
    arr[a]++;
  }

  for(int j = 0; j < 10001; j++){
    if(arr[j]){
      for(int k = 0; k < arr[j]; k++) cout << j << '\n';
    }
  }
}