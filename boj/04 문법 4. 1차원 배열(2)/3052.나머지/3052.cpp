#include <iostream>
#include <set>

using namespace std;

int main(){
  set<int> arr;

  for(int i = 0; i < 10; i++){
    int a;
    cin >> a;

    
    arr.insert(a % 42);
  }

  cout << arr.size();
}