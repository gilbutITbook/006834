# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# Tkinter 라이브러리 임포트
import Tkinter

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀번호를 대입
SW = 7
LED = 11

# 11번 핀을 출력 핀으로 설정, 초기출력은 로우레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# 7번 핀을 풀업 입력 핀으로 설정
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Tk 객체 인스턴스 작성
root = Tkinter.Tk()

# 원을 그리기 위해 Canvas 객체 인스턴스 작성
# 너비: 200, 높이: 200
c = Tkinter.Canvas(root, width = 200, height = 200)
# Canvas 배치
c.pack()

# 원 작성
# 좌표 (50,50)에서 (150,150), 색: 투명
cc = c.create_oval(50, 50, 150, 150, fill = '')

# 스위치가 눌리면 실행할 함수를 정의
def check_SW(channel):
    # 스위치 상태를 변수 key_in에 대입
    key_in = GPIO.input(channel)
    # 변수 key_in 상태를 판별
    if key_in==0:
        # 하이레벨 출력
        GPIO.output(LED, GPIO.HIGH)
        # 원을 빨강으로 채움
        c.itemconfig(cc, fill='red')
    else:
        # 로우레벨 출력
        GPIO.output(LED, GPIO.LOW)
        # 원을 투명하게 바꿈
        c.itemconfig(cc, fill='')

# 스위치 상태가 변화할 때 check_SW함수를 호출
GPIO.add_event_detect(SW, GPIO.BOTH, callback=check_SW)

# root 표시
root.mainloop()

# GPIO 개방
GPIO.cleanup()
