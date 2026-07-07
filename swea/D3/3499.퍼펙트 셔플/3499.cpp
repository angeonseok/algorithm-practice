#include <iostream>
#include <vector>
#include <string>

using namespace std;

int T; 

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){

    int N;
    cin >> N;
    
    vector<string> card(N);
    for(int i = 0; i < N; i++) cin >> card[i];
    
    int mid = (N+1) / 2;
    
    cout << '#' << t << ' ';
    for(int i = 0; i < mid; i++){
      cout << card[i] << ' ';
      if(mid + i < N){
        cout << card[mid + i] << ' ';
      }
    }
    cout << '\n';
  }
}
