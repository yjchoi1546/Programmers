import pandas as pd
import numpy as np

# 1. 단순 회귀분석용 데이터 (결측치 포함)
df_reg = pd.DataFrame({
    'Temperature': [45.2, 50.1, np.nan, 60.5, 65.0, 70.2, np.nan, 80.5, 85.0, 90.1],
    'Wear_Level': [1.2, 1.5, 1.8, 2.5, 2.9, 3.5, 4.0, 5.1, 5.8, 6.5]
})
df_reg.to_csv('sensor_regression.csv', index=False)

# 2. 이미지 분류 라벨 데이터 (실제 코테에서 이미지 경로와 정답이 담긴 파일로 자주 줌)
df_vision = pd.DataFrame({
    'image_file': ['img_001.jpg', 'img_002.jpg', 'img_003.jpg', 'img_004.jpg', 'img_005.jpg'],
    'defect_type': ['정상', '스크래치', '찍힘', '정상', '스크래치']
})
df_vision.to_csv('defect_labels.csv', index=False)

# 3. 시계열 예측용 다변량 데이터 (문자열, 결측치 섞임)
df_ts = pd.DataFrame({
    'Time': pd.date_range(start='2026-03-18 08:00', periods=10, freq='1min'),
    'Temp': [20.1, 20.5, 21.0, np.nan, 22.1, 22.5, 23.0, 23.2, np.nan, 24.0],
    'Vibration': [0.01, 0.02, 0.015, 0.03, 0.05, 0.04, 0.06, 0.08, 0.07, 0.1],
    'Machine_Status': ['ON', 'ON', 'ON', 'WARN', 'WARN', 'ERROR', 'ERROR', 'WARN', 'ON', 'ON']
})
df_ts.to_csv('taco_timeseries.csv', index=False)

print("✅ 코딩테스트용 CSV 파일 3개가 성공적으로 생성되었습니다!")