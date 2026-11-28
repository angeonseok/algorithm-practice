#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  vector<int> arr(n);
  for(int i = 0; i < n; i++)  cin >> arr[i];

  vector<int> s = arr;
  sort(s.begin(), s.end());
  s.erase(unique(s.begin(), s.end()), s.end());

  
}