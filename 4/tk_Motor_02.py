# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# Tkinter 라이브러리 임포트
import Tkinter

# time 라이브러리 임포트
import time

# collections 라이브러리 deque 임포트
from collections import deque

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀번호 대입
AIN1 = 15
BIN1 = 16
AIN2 = 18
BIN2 = 22

# 출력신호 패턴 deque 객체 작성
sig = deque([1, 0, 0, 0])

# 각 핀을 출력 핀으로 설정
GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)

# Tk 객체 인스턴스 작성
root = Tkinter.Tk()

# 방향을 지시하는 Variable 객체 인스턴스를 정수형으로 작성
dir = Tkinter.IntVar()
# 초기값을 1로 설정
dir.set(1)

# 시계방향(CW)을 뜻하는 라디오 버튼 작성
rb1 = Tkinter.Radiobutton(root, text = 'CW', variable = dir, value = 1)
# 라디오 버튼(CW) 배치
rb1.pack()

# 반시계방향(CCW)을 뜻하는 라디오 버튼 작성
rb2 = Tkinter.Radiobutton(root, text = 'CCW', variable = dir, value = -1)
# 라디오 버튼(CCW) 배치
rb2.pack()

# root에 표시할 라벨 정의
label = Tkinter.Label(root, text='Input STEP')
# label 배치
label.pack()

# 회전수를 입력할 텍스트 박스 작성
e = Tkinter.Entry(root)
# 텍스트 박스 배치
e.pack()

# 지정한 스텝수만큼 모터를 회전시키는 함수 정의
def rot_mtr():
    # 1회전
    for cnt in range( 0, int( e.get() ) ):
        # 출력 신호 패턴을 순서대로 출력
        GPIO.output(AIN1, sig[0])
        GPIO.output(BIN1, sig[1])
        GPIO.output(AIN2, sig[2])
        GPIO.output(BIN2, sig[3])

        # 0.01초 대기
        time.sleep(0.01)
        # 출력 신호 패턴 로테이트
        sig.rotate( dir.get() )

# 회전 시작 버튼 작성
b = Tkinter.Button(root, text="rotate", width=10, command=rot_mtr)
# 버튼 배치
b.pack()

# root 표시
root.mainloop()

# GPIO 해방
GPIO.cleanup()
