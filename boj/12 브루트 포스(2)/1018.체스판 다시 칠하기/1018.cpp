#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    
    vector<string> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    vector<int> ans;
    for(int i = 0; i < n - 7; i++){
        for(int j = 0; j < m - 7; j++){
            int b = 0, w = 0;

            for(int x = 0; x < 8; x++){
                for(int y = 0; y < 8; y++){
                    if((x + y) % 2 == 0){
                        //bwbwbwbw 가정
                        if(arr[x + i][y + j] != 'B')    b++;
                        
                        //wbwbwbwb  가정
                        if(arr[x + i][y + j] != 'W')    w++;
                    }
                    else{
                        // 같은 순서로
                        if(arr[x + i][y + j] != 'W')    b++;
                        if(arr[x + i][y + j] != 'B')    w++;
                    }
                }
            }
            ans.push_back(b);
            ans.push_back(w);
        }
    }

    cout << *min_element(ans.begin(), ans.end());
}