#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;
    
    vector<int> arr;
    int a;
    for(int i = 0; i < n; i++){
      cin >> a;
      arr.push_back(a);
    }

    sort(arr.begin(), arr.end());

    cout << '#' << t << ' ';
    for(int i = 0; i < n; i++)
      cout << arr[i] << ' ';
    
    cout << '\n';
  }
}