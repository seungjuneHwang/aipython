# Pillow 라이브러리 임포트
from PIL import Image
import matplotlib.pyplot as plt # 이미지 표시를 위해 사용 (선택 사항)
import numpy as np # 이미지 데이터를 배열로 다루기 위해 사용 (선택 사항)

try:
    # 이미지 파일 열기
    img = Image.open('input.jpg') # 'input.jpg' 파일을 현재 디렉토리에 준비해야 합니다.

    # 이미지 정보 출력 (선택 사항)
    print(f"원본 이미지 형식: {img.format}")
    print(f"원본 이미지 크기: {img.size}")
    print(f"원본 이미지 모드: {img.mode}")

    # 이미지 흑백으로 변환
    grayscale_img = img.convert('L')

    # 변환된 이미지 저장
    grayscale_img.save('output_grayscale.jpg')
    print("흑백 이미지가 'output_grayscale.jpg'로 저장되었습니다.")

    # 이미지 크기 조절 (예: 가로 200픽셀, 세로는 비율 유지)
    width = 200
    ratio = width / float(img.size[0])
    height = int((float(img.size[1]) * float(ratio)))
    resized_img = img.resize((width, height), Image.Resampling.LANCZOS) # 고품질 리샘플링
    resized_img.save('output_resized.jpg')
    print("크기 조절된 이미지가 'output_resized.jpg'로 저장되었습니다.")

    # Matplotlib를 사용하여 이미지 표시 (선택 사항)
    # 이미지를 NumPy 배열로 변환
    img_array = np.array(img)
    grayscale_array = np.array(grayscale_img)
    resized_array = np.array(resized_img)

    # 이미지 표시
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img_array)
    plt.title('Original Image')
    plt.axis('off') # 축 숨기기

    plt.subplot(1, 3, 2)
    plt.imshow(grayscale_array, cmap='gray') # 흑백 이미지는 cmap='gray' 사용
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(resized_array)
    plt.title('Resized Image')
    plt.axis('off')

    plt.tight_layout() # 서브플롯 간 간격 조절
    plt.show()

except FileNotFoundError:
    print("'input.jpg' 파일을 찾을 수 없습니다. 같은 디렉토리에 파일을 위치시켜 주세요.")
except Exception as e:
    print(f"오류 발생: {e}")