#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
  int n;
  cin >> n;

  vector<string> arr(n);
  for(int i = 0; i < n; i++)  cin >> arr[i];

  sort(arr.begin(), arr.end(), [](const string& a, const string& b){
    if(a.size() != b.size())  return a.size() < b.size();
    return a < b;
  });

  for(int i = 0; i < n; i++){
    if(i > 0 && arr[i - 1] == arr[i])  continue;
    cout << arr[i] << '\n';
  }
}