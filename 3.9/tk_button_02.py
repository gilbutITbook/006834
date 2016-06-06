# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# 버튼을 눌렀을 때 처리
def func():
    # Label 표시 변경
    label.config(text = 'Pushed')

# 라벨 생성
label = Tkinter.Label(root, text = 'Push Button')

# 라벨 배치
label.pack()

# 버튼 생성
button = Tkinter.Button(root, text = 'Push!', command = func)

# 버튼 배치
button.pack()

# root 표시
root.mainloop()
