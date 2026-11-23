#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n, m;
  cin >> n >> m;

  vector<int> arr(n);
  for(int x = 0; x < n; x++){
    arr[x] = x + 1;
  }

  for(int y = 0; y < m; y++){
    int i, j;
    cin >> i >> j;

    int tmp = arr[i - 1];
    arr[i - 1] = arr[j - 1];
    arr[j - 1] = tmp;
  }

  for(int z = 0; z < n; z++){
    cout << arr[z] << ' ';
  }
}