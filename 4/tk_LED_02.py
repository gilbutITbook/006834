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

# PWM 객체 인스턴스 생성
# 출력 핀: 11번, 주파수: 100Hz
p = GPIO.PWM(LED, 100)

# Tk 객체 인스턴스 root 작성
root = Tkinter.Tk()

# 슬라이드바 값으로 사용할 Variable 객체 인스턴스를 부동소수으로 작성
led_val = Tkinter.DoubleVar()
# 0 지정
led_val.set(0)

# PWM 신호 출력
p.start(0)

# 듀티비를 변경하는 함수를 정의
def change_duty(dc):
    # 듀티비 변경
    p.ChangeDutyCycle(led_val.get())

# root에 표시할 슬라이드 바를 정의
# 라벨 LED, 수평으로 표시, 숫자 범위는 0~100
s = Tkinter.Scale(root, label = 'LED', orient = 'h',\
                    from_ = 0, to = 100, variable = led_val, command = change_duty)

# 슬라이드 바 배치
s.pack()

# root 표시
root.mainloop()

# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()
