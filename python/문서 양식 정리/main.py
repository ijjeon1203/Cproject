import re

def auto_indent_outline(text: str, indent_unit: int = 2) -> str:
    lines = text.splitlines()
    result = []

    for line in lines:
        match = re.match(r'^(\d+(?:\.\d+)*)(\s*)(.*)', line)
        if match:
            numbering = match.group(1)  # ex: '1.2.3'
            content = match.group(3)
            level = numbering.count('.')  # 점 개수로 수준 계산
            indent = ' ' * (level * indent_unit)
            result.append(f"{indent}{numbering} {content.strip()}")
        else:
            result.append(line)  # 번호 없는 줄은 그대로

    return '\n'.join(result)

# 예시 사용
if __name__ == "__main__":
    raw_text = """\
1. 개요
1.1 목적
1.1.1 배경
1.2 범위
2. 시스템
2.1 구성
2.1.1 하드웨어
2.1.2 소프트웨어
"""

    formatted = auto_indent_outline(raw_text)
    print(formatted)
    
    
---
import re

def auto_indent_outline(text: str, indent_unit: int = 2, fill_char='.', line_width=60) -> str:
    lines = text.splitlines()
    result = []

    for line in lines:
        #match = re.match(r'^(\d+(?:\.\d+)*)(\s*)(.*)', line)
        match = re.match(r'^(\d+(?:\.\d+)*)(\s*)(.*?)(\s+)(\d+)$', line.strip())
        if match:
            numbering = match.group(1)  # ex: '1.2.3'
            content = match.group(3)
            page = match.group(5)
            level = numbering.count('.')  # 점 개수로 수준 계산
            indent = ' ' * (level * indent_unit)

            # 채우기선 계산
            left_text = f"{indent}{numbering} {content}"
            fill_length = line_width - len(left_text) - len(page)
            if fill_length < 0:
                fill_length = 2  # 최소 길이 확보
            filler = fill_char * fill_length
            result.append(f"{left_text} {filler} {page}")

        else:
            result.append(line)  # 번호 없는 줄은 그대로

    return '\n'.join(result)

# 예시 사용
if __name__ == "__main__":
    raw_text = """\


<표 차례>
표 1 		2
표 2 	3
표 3 	1
표 4 	2
표 5 	31. 개요	1
1.1. 적용범위	1
1.2. 체계 개요 	1
1.2.1. 체계 개발 경위	3
1.2.2. 관련 기관 	4
1.2.3. 운용 사이트	4
1.3. 문서 개요	5
1.3.1. 문서 목적	5
1.3.2. 문서 요약	5
1.3.3. 보안 및 주의사항	5
1.3.4. 식별자	6
1.3.4.1. 식별자 부여규칙	6
1.3.4.2. 디바이스 구분	6
2. 관련 문서	7
2.1. 정부문서	7
2.2. 비정부문서	8
3. 시험 개요	9
3.1. 시험명	9
3.2. 시험 목적	9
3.3. 시험 범위	9
3.4. 시험 장소	9
3.5. 시험 일정	9
3.6. 시험 조직	9
3.7. 시험 방법	9
4. 시험 준비사항	10
4.1. 하드웨어 준비사항	10
4.2. 소프트웨어 준비사항	10
4.3. 시험 구성도	10
4.4. 그 외 시험 전 준비사항	10
5. 시험 내역	11
5.1. 시험 항목 목록	11
5.2. T-CUAS-FME-SFR-001(야전점검장치-데이터연동 기능)	11
5.2.1. 요구사항	11
5.2.2. 선행 조건	11
5.2.2.1. 하드웨어/소프트웨어 구성도	11
5.2.2.2. 시험 수행을 위한 선행조건	11
5.2.3. 시험 입력자료	12
5.2.4. 시험 예상 결과	12
5.2.5. 결과 평가를 위한 기준	13
5.2.6. 시험 절차	13
5.2.6.1. 시험절차	13
5.2.7. 가정 및 제약사항	14
5.3. T-CUAS-FME-SFR-002(야전점검제어기-소프트웨어 기능)	15
5.3.1. 요구사항	15
5.3.2. 선행 조건	15
5.3.2.1. 하드웨어/소프트웨어 구성도	15
5.3.2.2. 시험 수행을 위한 선행조건	15
5.3.3. 시험 입력자료	16
5.3.4. 시험 예상 결과	16
5.3.5. 결과 평가를 위한 기준	16
5.3.6. 시험 절차	17
5.3.6.1. 시험절차	17
5.3.7. 가정 및 제약사항	18
5.4. T-CUAS-FME-SQR-001(소프트웨어의 신뢰성)	19
5.4.1. 요구사항	19
5.4.2. 하드웨어/소프트웨어 구성	19
5.4.3. 시험 수행을 위한 선행조건	19
5.4.4. 시험 입력자료	20
5.4.5. 시험 예상 결과	20
5.4.6. 결과 평가를 위한 기준	21
5.4.7. 시험 절차	21
5.4.7.1. 소프트웨어의 신뢰성 코딩규칙 검증  	21
5.4.7.2. 프로그램 정지나 결함발생 시 취해야 할 행동	21
5.4.8. 가정 및 제약사항	21
6. 요구사항 추적성	21
7. 참고사항	22
7.1. 용어/약어 설명	22
7.2. 기타 참고자료	22

<표 차례>
표 1 	2
표 2 	3
표 3 	1
표 4 	2
표 5 	3
"""

    formatted = auto_indent_outline(raw_text)
    print(formatted)