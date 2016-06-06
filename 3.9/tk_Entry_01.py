# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# 리턴키를 눌렀을 때 동작
def func(ev):
    # Label 표시를 변경
    label.config(text = e.get())

# 라벨 생성
label = Tkinter.Label(root, text = 'Input Text')
# 라벨 배치
label.pack()

# 텍스트 박스를 생성
e = Tkinter.Entry(root)

# 텍스트 박스 배치
e.pack()

# 리턴키를 눌렀을 때의 이벤트 추가
e.bind('<Return>', func)

# root 표시
root.mainloop()
