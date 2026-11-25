#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main(){
  int n;

  while(cin >> n){
    if(n == -1) break;

    vector<int> arr;
    for(int i = 1; i < n; i++){
      if(n % i == 0)  arr.push_back(i);  
    }

    int sum_num = accumulate(arr.begin(), arr.end(), 0);
    if(n == sum_num){
      cout << n << " = ";

      for(int j = 0; j < arr.size(); j++){
        if(j > 0) cout << " + ";
        cout << arr[j];
      }
    }
    else{
      cout << n << " is NOT perfect.";
    }

    cout << '\n';
  }
}