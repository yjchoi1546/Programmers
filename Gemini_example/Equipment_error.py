# 문제 1. [문자열/구현] 설비 에러 로그 파싱

# 설명: 반도체 장비에서 발생한 로그 데이터가 문자열 배열로 주어집니다. 
# 각 로그는 "[시간] [장비ID] [상태코드]" 형식입니다. 
# 상태 코드가 "ERR_001"부터 "ERR_005" 사이인 로그만 추출하여, 각 장비ID별로 에러가 발생한 횟수를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.


def parser_error_logs(logs):
    error_counts = {}
    target_errors = {"ERR_001", "ERR_002", "ERR_003", "ERR_004", "ERR_005"} # set 설정
    
    for log in logs:
        parts = log.split(" ") # 공백 기준으로 나누기
        if len(parts) != 3:
            continue # 로그 형식이 잘못된 경우 무시 (예외처리)
        _, equipment_id, status_code = parts
        # 타겟 에러 코드에 해당하는 경우에만 카운트
        if status_code in target_errors:
            # get 메서드를 사용하여 장비ID별로 키가 없을 때의 기본갑을 0으로 설정하여 카운트 증가
            error_counts[equipment_id] = error_counts.get(equipment_id, 0) + 1
    
    
    # 1. 에러 발생 횟수 기준 내림차순 정렬
    # 2. 횟수가 같을 경우 장비ID 기준 오름차순 정렬
    sorted_error_counts = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    return [eq[0] for eq in sorted_error_counts] # 장비ID만 추출하여 반환
        
# 예시 입력
sample_logs = [
    "[10:00] [EQ_01] [ERR_002]",
    "[10:01] [EQ_02] [ERR_001]",
    "[10:05] [EQ_01] [ERR_002]",
    "[10:06] [EQ_03] [INFO_001]",
    "[10:10] [EQ_02] [ERR_005]"
]

print(parser_error_logs(sample_logs)) 