import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Pillow 라이브러리 사용

# --- 함수 정의 ---
def select_image():
    """파일 선택 대화상자를 열고 이미지를 로드하여 화면에 표시하는 함수"""
    global image_path, photo_image # 함수 종료 후에도 이미지 참조 유지

    # 파일 선택 대화상자 열기 (이미지 파일 형식 필터링)
    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.ppm *.pgm"),
                   ("All files", "*.*")]
    )

    # 사용자가 파일을 선택했는지 확인
    if not file_path:
        print("파일을 선택하지 않았습니다.")
        return # 함수 종료

    image_path = file_path # 선택된 파일 경로 저장 (선택 사항)

    try:
        # Pillow를 사용하여 이미지 열기
        pil_image = Image.open(image_path)

        # (선택 사항) 이미지 크기 조정 (너무 큰 이미지는 창 크기에 맞게 조절)
        max_width = 600
        max_height = 500
        pil_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

        # Pillow 이미지를 Tkinter에서 사용할 수 있는 PhotoImage 객체로 변환
        # *** 중요: photo_image 변수를 전역 또는 클래스 멤버 등으로 유지해야 이미지가 표시됨 ***
        # 함수 내 지역 변수로 선언하면 함수 종료 시 가비지 컬렉션되어 이미지가 사라짐
        photo_image = ImageTk.PhotoImage(pil_image)

        # 이미지 레이블 업데이트
        image_label.config(image=photo_image)
        image_label.image = photo_image # 레이블 객체에 참조 유지 (가비지 컬렉션 방지)

        # 창 제목 업데이트 (선택 사항)
        window.title(f"이미지 뷰어 - {image_path.split('/')[-1]}") # 파일명만 표시

        print(f"이미지 로드 완료: {image_path}")

    except FileNotFoundError:
        print(f"오류: 파일을 찾을 수 없습니다 - {image_path}")
        image_label.config(text="파일을 찾을 수 없습니다.", image='') # 오류 메시지 표시
        window.title("이미지 뷰어")
    except Exception as e:
        print(f"오류: 이미지를 로드하는 중 문제가 발생했습니다 - {e}")
        image_label.config(text=f"이미지 로드 오류:\n{e}", image='') # 오류 메시지 표시
        window.title("이미지 뷰어")


# --- GUI 설정 ---
# 메인 윈도우 생성
window = tk.Tk()
window.title("이미지 뷰어")
window.geometry("700x600") # 초기 창 크기 설정

# 전역 변수 초기화 (이미지 참조 유지를 위해)
image_path = None
photo_image = None

# 파일 선택 버튼 생성
select_button = tk.Button(window, text="이미지 선택", command=select_image, padx=10, pady=5)
select_button.pack(pady=20) # 위쪽에 여백을 주고 배치

# 이미지를 표시할 레이블 생성
# 초기에는 비어있거나 안내 문구를 표시할 수 있음
image_label = tk.Label(window, text="이미지를 선택하세요.", compound=tk.CENTER)
image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10) # 창 크기에 맞춰 확장되도록 설정

# --- 메인 루프 시작 ---
window.mainloop()