# 문제 3. [Vision / PyTorch] Custom Dataset 구현
# 설명: data_dir 폴더 안에 normal/ 폴더와 defect/ 폴더가 있고, 
# 각각 이미지 파일(.jpg)들이 들어있습니다. 
# 이 디렉토리 구조를 읽어들여 이미지 파일 경로와 라벨(정상=0, 불량=1)을 매핑하는 PyTorch의 Dataset 클래스를 작성하세요.
# __getitem__ 메서드에서는 이미지를 불러와 $224 \times 224$로 리사이즈하고, 텐서로 변환하여 반환해야 합니다.

# 핵심 포인트: __init__, __len__, __getitem__ 3가지 필수 메서드의 역할 분리와 메모리 효율성(이미지는 __getitem__에서 로드).

import os
from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision import transforms

class DefectDataset(Dataset):
    def __init__(self, data_dir):
        self.image_paths = []
        self.labels = []
        # 라벨 딕셔너리
        class_to_idx = {'normal' : 0, 'defect' : 1}
        
        # 디렉토리 순회하며 파일 경로 저장
        for class_name, label_idx in class_to_idx.items():
            class_dir = os.path.join(data_dir, class_name)
            # 해당 디렉토리가 존재하는지 확인
            if os.path.isdir(class_dir):
                for img_name in os.listdir(class_dir):
                    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        self.image_paths.append(os.path.join(class_dir, img_name))
                        self.labels.append(label_idx)
        # 텐서 변환 및 리사이징 정의
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])
        
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert('RGB') # 이미지 로드 및 RGB 변환
        
        # 전처리
        if self.transform:
            image = self.transform(image)
        label = self.labels[idx]
        
        # 라벨을 PyTorch 텐서로 변환
        return image, torch.tensor(label, dtype=torch.long)
