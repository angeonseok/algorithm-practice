#include <iostream>

using namespace std;

int T;

int main (){
  cin >> T;

  for(int t = 1; t <= T; t++){
    int n;
    cin >> n;

    int speed = 0, dist = 0, cmd, acc;
    for(int i = 0; i < n; i++){
      cin >> cmd;
      if(cmd == 1){
        cin >> acc;
        speed += acc;
      }

      else if(cmd == 2){
        cin >> acc;
        speed -= acc;

        if(speed < 0)
          speed = 0;
      }

      dist += speed;
    }

    cout << '#' << t << ' ' << dist << endl;
  }
}