#include <iostream>
#include <vector>

using namespace std;

int main(){
  vector<int> arr(30, 0);
  
  for(int i = 0; i < 28; i++){
    int a;
    cin >> a;
    arr[a - 1] = 1;
  }

  for(int j = 0; j < 30; j++){
    if(arr[j] == 0) cout << j + 1 << '\n';
  }
}