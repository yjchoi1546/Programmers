# 문제 4. [모델링] 전이 학습(Transfer Learning) 분류기 수정

# 설명: 불량 여부를 판별하기 위해, PyTorch를 활용하여 ResNet50과 같은 사전 학습된(Pre-trained) 비전 모델을 불러온 뒤, 마지막 Fully Connected Layer(분류기)를 클래스가 2개(정상, 불량)인 출력으로 변경하는 코드를 작성하세요.

# 목적: 실제 현업에서 자주 쓰이는 백본(Backbone) 모델의 구조를 이해하고 과제에 맞게 변형할 수 있는지 평가.

# 문제 4. [모델링] 전이 학습(Transfer Learning) 분류기 수정
# 핵심 포인트: torchvision 모델의 구조를 파악하고, 마지막 레이어(fc 또는 classifier)의 입출력 차원을 맞추는 방법.
import torch.nn as nn
import torchvision.models as models

def get_modified_resnet():
    # 1. ImageNet으로 사전 학습된 ResNet50 모델 불러오기
    model = models.resnet50(pretrained=True)
    # 모델의 특성 추출기 가중치를 동결하고 싶을 때
    # for param in model.parameters():
    #     param.requires_grad = False
    
    # 2. 기존 마지막 Fully Connected Layer(fc)의 입력 차원 확인
    num_ftrs = model.fc.in_features
    
    # 3. 우리가 원하는 클래스 개수(2개: 정상, 불량)로 마지막 레이어 교체
    model.fc = nn.Linear(num_ftrs, 2)
    
    return model