#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T;

int main(){
  cin >> T;
  
  for(int t = 1 ; t <= T; t++){
    int N, M, K;
    cin >> N >> M >> K;
    
    vector<int> list(N);
    for(int i = 0; i < N; i++) cin >> list[i];
    
    sort(list.begin(), list.end());

    int bread = 0, idx = 0;
    bool flag = true;
    for(int i = 0; i < list[N-1] + 1; i++){
      if(i && i % M == 0) bread += K;
      
      while(idx < N && list[idx] == i){
        bread--;
        idx++;

        if(bread < 0){
          flag = false;
          break;
        }
      }
      if(!flag) break;
    }
    
    if(flag){
      cout << '#' << t << ' ' << "Possible" << endl;
    }
    else{
      cout << '#' << t << ' ' << "Impossible" << endl;
    }
  }
}