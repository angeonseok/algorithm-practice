# -*- coding: utf-8 -*-
"""
SWEA 문제용 README.md 생성기

기능:
    난이도 / 번호 / 제목을 입력하고 문제 지문을 붙여넣으면,
    기존 README 규격에 맞춰
        <난이도>/<번호>.<제목>/README.md
    파일을 생성한다.

사용법:
    python make_readme.py

    1) 난이도 입력   (예: D3, 역량테스트)
    2) 번호 입력     (예: 26792)
    3) 제목 입력     (예: 덧셈과 뺄셈)
    4) 문제 지문 붙여넣기 -> 마지막 줄에 EOF 입력(또는 Ctrl+Z 후 Enter)

지문의 [입력] / [출력] / [제약 사항] / [예제] 같은 마커를 각각
## 입력 / ## 출력 / ## 제약사항 / ## 예제 섹션으로 변환한다.
첫 마커 이전의 내용은 ## 문제 설명 이 된다.
섹션 내부의 빈 줄은 제거되어 기존 파일들처럼 문장이 연달아 붙는다.
"""

import os
import re
import sys

try:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SECTION_RE = re.compile(r"^\[\s*(.+?)\s*\]$")

# 마커 이름 -> 헤더 표준화 (공백 제거 후 매핑)
NAME_MAP = {
    "input": "입력",
    "output": "출력",
}

# 문제 설명과 입력 사이에 오도록 정렬할 부가 섹션 우선순위
TAIL = ["핵심 아이디어", "시간복잡도", "구현 포인트", "실수했던 점", "풀이 언어"]


def normalize_lines(text):
    """줄별 정리: BOM/제로폭 제거, 좌우 공백 제거, 불릿 통일, 빈 줄 모두 제거."""
    text = text.replace("﻿", "").replace("​", "")
    out = []
    for ln in text.splitlines():
        ln = ln.strip()
        ln = re.sub(r"^[-*]\s+", "- ", ln)  # 불릿 기호/간격 통일
        if ln:  # 섹션 내부 빈 줄 제거
            out.append(ln)
    return out


def normalize_header(raw_name):
    name = re.sub(r"\s+", "", raw_name)  # "제약 사항" -> "제약사항"
    return NAME_MAP.get(name.lower(), name)


def parse_problem(raw):
    """[...] 마커 기준으로 섹션을 나눈다.
    반환: [(header, body), ...]  (첫 항목은 항상 '문제 설명')."""
    sections = [["문제 설명", []]]
    for ln in raw.splitlines():
        m = SECTION_RE.match(ln.strip())
        if m:
            sections.append([normalize_header(m.group(1)), []])
        else:
            sections[-1][1].append(ln)
    return [(h, "\n".join(normalize_lines("\n".join(b)))) for h, b in sections]


def build(number, title, sections):
    lines = ["# {}.{}".format(number, title), ""]
    for header, body in sections:
        lines.append("## " + header)
        if body:
            lines.append(body)
        lines.append("")
    lines.append("## 풀이 정리")
    lines.append("")
    for sub in TAIL:
        lines.append("### " + sub)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def read_multiline(prompt):
    print(prompt)
    print("(붙여넣은 뒤 마지막 줄에 EOF 입력 후 Enter, 또는 Ctrl+Z 후 Enter)")
    lines = []
    try:
        while True:
            line = input()
            if line.strip() == "EOF":
                break
            lines.append(line)
    except EOFError:
        pass
    return "\n".join(lines)


def main():
    level = input("난이도 (예: D3, 역량테스트): ").strip()
    number = input("문제 번호 (예: 26792): ").strip()
    title = input("제목 (예: 덧셈과 뺄셈): ").strip()

    if not (level and number and title):
        print("난이도/번호/제목은 모두 입력해야 합니다.")
        return

    raw = read_multiline("\n문제 지문을 붙여넣으세요:")
    sections = parse_problem(raw)
    content = build(number, title, sections)

    base = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(base, level, "{}.{}".format(number, title))
    path = os.path.join(folder, "README.md")

    if os.path.exists(path):
        ans = input("\n이미 존재합니다: {}\n덮어쓸까요? (y/N): ".format(path)).strip().lower()
        if ans != "y":
            print("취소했습니다.")
            return

    os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("\n생성 완료: {}".format(path))


if __name__ == "__main__":
    main()
