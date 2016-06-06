# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# 라벨 생성
label = Tkinter.Label(root, text= 'Hello World')

# 라벨 배치
label.pack()

# root 표시
root.mainloop()
