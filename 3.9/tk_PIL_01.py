# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# PIL 임포트
from PIL import Image, ImageTk

# Tk 객체 인스턴스 작성
root = Tkinter.Tk()

# 이미지 파일 열기
image = Image.open('photo.png')

# PhotoImage 호환 이미지 객체로 변환
im = ImageTk.PhotoImage(image)

# root에 표시할 라벨 정의
label = Tkinter.Label(root, image=im)

# 이미지 객체의 참조를 저장
label.image = im

# 라벨 배치
label.pack()

# root 표시
root.mainloop()
