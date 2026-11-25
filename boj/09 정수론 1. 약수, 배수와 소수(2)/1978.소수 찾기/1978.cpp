#include <iostream>
#include <vector>

using namespace std;

int main(){
  int n, cnt = 0;
  cin >> n;

  for(int i = 0; i < n; i++){
    int a;
    cin >> a;

    if(a < 1)  continue;

    vector<int> prime;

    for(int j = 2; j <= a; j++){
      if(a % j == 0)  prime.push_back(j);
    }

    if(prime.size() == 1)   cnt++;
  }

  cout << cnt;
} 