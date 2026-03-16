# 문제 5. [평가 지표] 불균형 데이터의 성능 평가 지표 계산

# 설명: 모델이 예측한 결과 배열 y_pred와 실제 정답 배열 y_true가 주어집니다. 
# (1: 불량, 0: 정상). 라이브러리(scikit-learn 등)를 사용하지 않고, 
# 직접 Confusion Matrix의 요소(TP, TN, FP, FN)를 계산한 뒤, 
# **정밀도(Precision)**와 재현율(Recall), 그리고 F1-score를 반환하는 함수를 작성하세요.


def calculate_metrics(y_true, y_pred):
    tp = 0  # True Positives
    tn = 0  # True Negatives
    fp = 0  # False Positives
    fn = 0  # False Negatives
    
    # 1. 요소 계산
    for true_val, pred_val in zip(y_true, y_pred):
        if true_val == 1 and pred_val == 1:
            tp += 1
        elif true_val == 0 and pred_val == 0:
            tn += 1
        elif true_val == 0 and pred_val == 1:
            fp += 1
        elif true_val == 1 and pred_val == 0:
            fn += 1
            
    # 2. 정밀도(Precision) 계산
    # 분모가 0이 되는 경우를 방지하기 위해 조건문 추가
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    
    # 3. 재현율(Recall) 계산
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    
    # 4. F1-score 계산
    f1_score = 0.0
    if precision + recall > 0:
        f1_score = 2 * (precision * recall) / (precision + recall)
    
    return precision, recall, f1_score

# 예시 입력
y_true = [1, 0, 1, 1, 0, 0, 1]
y_pred = [1, 0, 0, 1, 0, 1, 1]
