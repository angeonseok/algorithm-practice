#include <iostream>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;

    int days[13] = {
        0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };

    for(int t = 1; t <= T; t++){
        string s;
        cin >> s;

        string y = s.substr(0, 4);
        string m = s.substr(4, 2);
        string d = s.substr(6, 2);

        int month = stoi(m);
        int day = stoi(d);

        if(month < 1 || month > 12){
            cout << '#' << t << ' ' << -1 << endl;
            continue;
        }

        if(day < 1 || day > days[month]){
            cout << '#' << t << ' ' << -1 << endl;
            continue;
        }
        cout << '#' << t << ' ' << y << '/' << m << '/' << d << endl;
    }
}