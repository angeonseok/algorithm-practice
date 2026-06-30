/*연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
[그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)*/

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