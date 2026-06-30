#include <iostream>

using namespace std;

int arr[9][9];

bool check_row(int r){
  int sum = 0;

  for(int i = 0; i < 9; i++){
    sum += arr[r][i];
  }

  return sum == 45;
}


bool check_col(int c){
  int sum = 0;

  for(int i = 0; i < 9; i++){
    sum += arr[i][c];
  }

  return sum == 45;
}


bool check_box(int sr, int sc){
  int sum = 0;

  for(int i = sr; i < sr + 3; i++){
    for(int j = sc; j < sc + 3; j++){
      sum += arr[i][j];
    }
  }

  return sum == 45;
}


bool sudoku(){
  for(int i = 0; i < 9; i++)
    if(!check_row(i) || !check_col(i))  return false;
  
  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
      if(!check_box(i * 3, j * 3))  return false;
    }
  }

  return true;
}

int T;

int main(){
  cin >> T;

  for(int t = 1; t <= T; t++){

    for(int i = 0; i < 9; i++){
      for(int j = 0; j < 9; j++){
        cin >> arr[i][j];
      }
    }

    if(sudoku())
      cout << '#' << t << ' ' << 1 << endl;
    else
      cout << '#' << t << ' ' << 0 << endl;
  }
}