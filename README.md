# 성적 CSV 읽기 프로그램 (load_scores)

## ① 무엇을 하나요 (What)

성적 CSV 파일을 읽어 **유효한 (이름, 점수)만 골라 내고**, 건너뛴 줄은 줄 번호와 이유를 함께 알려 줍니다.

## ② 왜 만들었나요 (Why)

실제 성적 파일에는 빈 점수, 0~100을 벗어난 점수(105점), 정수가 아닌 값("결석"), 열이 하나 더 붙은 줄이 섞여 있습니다.
그냥 읽으면 프로그램이 멈추거나, 더 나쁘게는 오류 없이 틀린 평균을 내 버립니다.
그래서 잘못된 줄은 걸러 내되 **걸러 냈다는 사실을 조용히 넘기지 않고 반드시 알려 주도록** 만들었습니다.
같은 이름이 두 번 나와도 동명이인일 수 있으니 지우지 않고 둘 다 남깁니다.

## ③ 어떻게 쓰나요 (How)

Python 3.9 이상이 필요하고, 외부 라이브러리는 필요 없습니다.

```bash
# 설치
git clone https://github.com/<내아이디>/<저장소이름>.git
cd <저장소이름>

# 실행  (Windows에서는 python)
python3 load_scores.py scores.csv
```

실행 결과:

```
읽은 줄 : 5개
  김하나 88
  최,네번 77
  김하나 91
  윤보람 64
  서한별 95
건너뛴 줄 : 5개
  3행  이두리,105   ← 점수가 0~100 밖
  4행  박세찬,   ← 점수가 비어 있음
  7행  정오름,-5   ← 점수가 0~100 밖
  8행  한겨울,결석   ← 점수가 정수가 아님
  9행  장미르,72,비고없음   ← 열 개수가 2가 아님
```

## ④ 어떻게 테스트하나요

```bash
pip install pytest
pytest test_load_scores.py
```

```
.............                                                            [100%]
13 passed in 0.03s
```

모든 테스트(AI가 만든 비교용 테스트 포함)를 한 번에 돌리려면 `pytest` 만 입력한다. 95개가 통과한다.
`test_ai_bug.py`는 일부러 고장난 `bug3_logic.py`를 시험하는 실험용이라 4개가 실패하는 것이 정상이며, 기본 `pytest`에서는 빠져 있다. 만약 보고 싶으면 `pytest test_ai_bug.py`로 실행한다민.

어느 줄이 테스트를 지나가지 않았는지 보려면 (선택):

```bash
pip install pytest-cov
pytest test_load_scores.py --cov=load_scores --cov-report=term-missing
```

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| `load_scores.py` | CSV를 읽어 `(유효한 목록, 건너뛴 줄 기록)`을 돌려주는 함수. 직접 실행도 가능 |
| `test_load_scores.py` | 직접 설계한 테스트 (정상 · 예외 · 경계값 + 커버리지로 찾은 빈틈) |
| `test_ai_A.py` | AI에게 코드를 줘서 받은 테스트 (고치지 않고 저장) |
| `test_ai_B.py` | AI에게 명세를 줘서 받은 테스트 (고치지 않고 저장) |
| `test_ai_bug.py` | 고장난 코드를 주고 받은 테스트 (고치지 않고 저장) |
| `bug3_logic.py` | 9주차의 고장난 `find_max` · `count_pass` (함정 실험용) |
| `scores.csv` · `empty.csv` · `weird.csv` | 예제 데이터 (지저분한 줄 포함 · 헤더만 있음 · 이상한 값 모음) |
| `pytest.ini` | pytest 설정 |
| `.gitignore` | Git이 무시할 파일 목록 |
| `LICENSE` | MIT 라이선스 (저장소를 만들 때 GitHub이 자동으로 생성) |

## ⑥ 만든 사람 · AI를 어디에 썼는지

- 만든 사람 : 백석훈·2026100053
- AI를 쓴 곳 : Claude(Anthropic)가 테스트 코드 초안, 비교용 테스트(`test_ai_*.py`), README 초안을 작성했습니다.
- 내가 직접 판단한 것 : 케이스 설계(설계표), 어떤 입력이 지나가지 않았는지 보고 추가할 테스트 정하기, 실행 결과 확인과 비교, 커밋과 업로드

## 라이선스

MIT License (LICENSE 파일 참고)
