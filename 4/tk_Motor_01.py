# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# Tkinter 라이브러리 임포트
import Tkinter

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀번호 대입
AIN1 = 13
AIN2 = 15
PWMA = 12

# 각 핀을 출력 핀으로 설정
GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

# PWM 객체 인스턴스 작성
# 출력 핀: 12번, 주파수: 100Hz
p = GPIO.PWM(PWMA, 100)

# Tk 객체 인스턴스 root 작성
root = Tkinter.Tk()

# 방향 변경 슬라이드 바로 사용할 Variable 객체 인스턴스(정수형) 작성
dir = Tkinter.IntVar()
# 초기값으로 1(정지) 설정
dir.set(1)

# 속도 변경 슬라이드 바로 사용할 Variable 객체 인스턴스(부동소수점형) 작성
spd = Tkinter.DoubleVar()
# 초기값으로 0(속도 0) 설정
spd.set(0)

# PWM 신호 출력 시작
p.start(0)

# 회전 방향을 변경하는 함수 정의
def change_dir(dr):
    if(dir.get() == 0):
        # 시계 방향으로 회전 방향 변경
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
    elif(dir.get() == 1):
        # 정지
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
    elif(dir.get() == 2):
        # 반시계 방향으로 회전 방향 변경
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)

# 듀티비를 변경하는 함수 정의
def change_pw( pw ):
    # 듀티비 변경
    p.ChangeDutyCycle(spd.get())

# 방향 변경용 슬라이드 바 정의
# 라벨 Direction, 수평 표시, 숫자 범위는 0~2
s1 = Tkinter.Scale(root, label = 'Direction', orient = 'h',\
                    from_ = 0, to = 2, variable = dir, command = change_dir)

# 방향 변경용 슬라이드 바 배치
s1.pack()

# 속도 변경용 슬라이드 바 정의
# 라벨 Speed, 수평 표시, 숫자 범위는 0~100
s2 = Tkinter.Scale(root, label = 'Speed', orient = 'h',\
                    from_ = 0, to = 100, variable = spd, command = change_pw)

# 속도 변경용 슬라이드 바 배치
s2.pack()

# root 표시
root.mainloop()

# PWM 신호 정지
p.stop()

# GPIO 개방
GPIO.cleanup()
