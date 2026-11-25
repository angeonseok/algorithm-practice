#include <iostream>
#include <string>

using namespace std;

int main(){
    int n;
    cin >> n;

    int ans = n;
    for(int tc = 0; tc < n; tc++){
        string s;
        bool alpha[26] = {false};
        
        cin >> s;
        for(int i = 0; i < s.length(); i++){
            if(i == 0 || s[i] != s[i - 1]){
                if(alpha[s[i] - 'a']){
                    ans --;
                    break;
                }

                alpha[s[i - 1] - 'a'] = true;
            }
        }
    }

    cout << ans;
}