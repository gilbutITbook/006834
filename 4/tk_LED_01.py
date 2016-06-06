# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# Tkinter 라이브러리 임포트
import Tkinter

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀번호 대입
LED = 11

# 11번 핀을 출력 핀으로 설정, 초기출력은 로우레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# LED를 켜고 끄는 함수를 정의
def func():

    # 11번 핀에서 나오는 입력값을 반전해서 출력
    GPIO.output(LED, not GPIO.input(LED))

# Tk 객체 인스턴스 root 작성
root = Tkinter.Tk()

# root에 표시할 라벨 정의
label = Tkinter.Label(root, text='press button')

# 라벨 배치
label.pack()

# root에 표시할 버튼 정의
button = Tkinter.Button(root, text='LED', command=func)

# 버튼 배치
button.pack()

# root 표시
root.mainloop()

# GPIO 개방
GPIO.cleanup()
