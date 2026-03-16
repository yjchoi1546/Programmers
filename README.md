# Programmers

알고리즘 문제 풀이와 머신러닝 실습 코드를 함께 정리한 학습용 저장소입니다.

## 소개

이 저장소는 다음 두 가지 흐름으로 구성되어 있습니다.

- `Level1`, `Level2`, `Level3`: 프로그래머스 스타일 알고리즘 문제 풀이
- `Gemini_example`: 데이터 처리, 평가 지표, PyTorch 기반 모델링 예제

간단한 문제 해결부터 DFS/BFS, 동적 계획법(DP), 전이 학습(Transfer Learning)까지 단계적으로 학습할 수 있도록 구성했습니다.

## 폴더 구조

아래 구간은 자동 업데이트됩니다.

<!-- AUTO-TREE-START -->
```text
Programmers/
├─ .github/
│  └─ workflows/
│     └─ update-readme-tree.yml
├─ Algorithm/
│  └─ Test.ipynb
├─ Gemini_example/
│  ├─ Confusion_Matrix.py
│  ├─ Custom_Dataset.py
│  ├─ Equipment_error.py
│  ├─ Exam_Test.ipynb
│  ├─ Sensor_Data_Missing_Value_Handling_and_Sliding_Window.py
│  └─ Transfer_Learning.py
├─ Level1/
│  ├─ Add_missing_num.py
│  ├─ Add_negative_positive_.py
│  ├─ array_of_numbers_that_fall_apart.py
│  ├─ change_str_to_int.py
│  ├─ Determination_int_square_root.py
│  ├─ Even_Odd.py
│  ├─ Find_remainder1.py
│  ├─ Harshad_Num.py
│  ├─ Int_descending_order.py
│  ├─ mean.py
│  ├─ Number_of_py_in_str.py
│  ├─ reversing_array.py
│  ├─ sep_x_with_n_number.py
│  ├─ sum_of_divisors.py
│  ├─ sum_of_each_digit.py
│  └─ sum_of_integers_between_two_numbers.py
├─ Level2/
│  ├─ correct_parentheses.py
│  ├─ make_min.py
│  ├─ max_min.py
│  └─ Perfect_Crime.py
├─ Level3/
│  ├─ DFS_BFS.py
│  └─ Int_triangle.py
├─ scripts/
│  └─ update_readme_tree.py
├─ .gitignore
├─ .gitmessage.txt
├─ .python-version
├─ pyproject.toml
├─ README.md
└─ uv.lock
```
<!-- AUTO-TREE-END -->

## 주요 학습 내용

### 1) 알고리즘 문제 풀이

- `Level1` (기초): 짝/홀 판별, 문자열/정수 변환, 약수/자리수 합, 배열 처리
- `Level2` (중급): 올바른 괄호, 최솟값 만들기, 문자열 내 최댓값/최솟값 처리
- `Level3` (심화): 네트워크(DFS/BFS), 정수 삼각형(DP)

### 2) 머신러닝/딥러닝 예제 (`Gemini_example`)

- Confusion Matrix 기반 분류 성능 지표 계산
- 센서 데이터 전처리(결측치 처리, 슬라이딩 윈도우)
- PyTorch `Dataset` 커스텀 구현
- 사전학습 모델(예: ResNet) 전이학습 분류기 수정
- 로그 파싱 기반 설비 오류 분석 예제

## 실행 방법

### 1) 환경 준비

Python 3.10 이상이 필요합니다.

```bash
pip install -e .
```

또는 `uv`를 사용하는 경우:

```bash
uv sync
```

### 2) 개별 파일 실행

```bash
python Level1/Even_Odd.py
python Level2/correct_parentheses.py
python Level3/DFS_BFS.py
python Gemini_example/Confusion_Matrix.py
```

노트북 파일은 Jupyter에서 실행합니다.

```bash
jupyter notebook
```

## 목표

- 알고리즘 문제 해결 능력 향상
- 실무형 데이터 처리 및 모델링 기초 학습
- Python 코딩 습관과 문제 분해 능력 강화

## 참고

- 프로젝트 의존성 및 실행 환경은 `pyproject.toml`에 정의되어 있습니다.
- 커밋 메시지 템플릿은 `.gitmessage.txt`를 사용합니다.
- 폴더 구조 자동 갱신 스크립트: `scripts/update_readme_tree.py`
- 자동 실행 워크플로: `.github/workflows/update-readme-tree.yml`

