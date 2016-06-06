# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# 라디오 버튼 1을 선택했을 때 처리
def func1():
    # 라벨 표시 변경
    label.config(text = 'Button 1')

# 라디오 버튼 2를 선택했을 때 처리
def func2():
    # 라벨 표시 변경
    label.config(text = 'Button 2')

# 라디오 버튼 값을 저장하는 정수형 Variable 객체 생성
sel = Tkinter.IntVar()

# sel에 1 대입
sel.set(1)

# 라벨 생성
label = Tkinter.Label(root, text = 'Select Button')

# 라벨 배치
label.pack()

# 라디오 버튼 1 생성
rb1 = Tkinter.Radiobutton(root, text = 'Button 1', variable = sel, value = 1, command = func1)

# 라디오 버튼 1 배치
rb1.pack()

# 라디오 버튼 2 생성
rb2 = Tkinter.Radiobutton(root, text = 'Button 2', variable = sel, value = 2, command = func2)

# 라디오 버튼 2 배치
rb2.pack()

# root 표시
root.mainloop()
