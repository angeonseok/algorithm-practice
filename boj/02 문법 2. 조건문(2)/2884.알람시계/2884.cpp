#include <iostream>

using namespace std;

int main(){
  int a, b;

  cin >> a >> b;

  if(b < 45){
    if(a == 0){
      a = 23;
      b += 60;
    }
    else{
      a -= 1;
      b += 60;
    }
  }

  cout << a << " " << b - 45;
}