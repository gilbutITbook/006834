# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# Canvas 객체 인스턴스 생성
# 너비: 500、높이: 500
c = Tkinter.Canvas(root, width = 500, height = 500)
# Canvas 배치
c.pack()

# 선을 그림
# 좌표(0,0)에서 (50,50), 색: 검정
c.create_line(0, 0, 50, 50)

# 사각형을 그림
# 좌표(100,100)에서 (150,150), 색: 빨강
c.create_rectangle(100, 100, 150, 150, fill = 'red')

# 원을 그림
# 좌표(100,200)에서 (150,250), 색: 파랑
c.create_oval(100, 200, 150, 250, fill = 'blue')

# 다각형을 그림
# 8개의 좌표를 연결한 팔각형, 색: 녹색
c.create_polygon(250, 200, 350, 200, 400, 250, 400, 350, 350, 400, 250, 400,\
                200, 350, 200, 250, fill = 'green')

# root 표시
root.mainloop()
