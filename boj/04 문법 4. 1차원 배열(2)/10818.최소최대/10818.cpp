#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int n;
  cin >> n;

  vector<int> arr(n);
  
  for(int i = 0; i < n; i++)  cin >> arr[i];

  cout << *min_element(arr.begin(), arr.end()) << ' ' << *max_element(arr.begin(), arr.end());
}