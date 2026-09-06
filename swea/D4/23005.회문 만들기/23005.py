T = int(input())
for tc in range(1, T+1):
    text = input().strip()

    ans = 0

    #양 끝단에서 중앙으로
    i, j = 0, len(text) - 1

    while i <= j:
        #서로 같은 경우 : 양쪽에서 다음 좌표 넘어감
        if text[i] == text[j]:
            i += 1
            j -= 1

        #왼쪽 포인터가 x인 경우: 대응하는 오른쪽 위치에 x 놓고 다음 좌표 확인
        elif text[i] == 'x':
            i += 1
            ans += 1

        #오른쪽 프린터가 x인 경우 : 왼쪽이랑 같은 과정
        elif text[j] == 'x':
            j -= 1
            ans += 1

        #위에 3가지 경우에 해당 없으면 회문 생성 불가
        else:
            ans = -1
            break

    print(ans)