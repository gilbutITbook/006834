# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀번호 대입
LED = 11

# 듀티비 목록 작성
dc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 20, 30, 50, 70, 100]

# 11번 핀을 출력 핀으로 설정, 초기출력은 로우레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# PWM 객체 인스턴스 작성
# 출력 핀: 11번, 주파수: 100Hz
p = GPIO.PWM(LED, 100)

# PWM 신호 출력
p.start(0)

# 예외 처리
try:
    # 무한 반복
    while 1:
        # 듀티비를 0~100까지 목록에 따라 변경
        for val in dc:
            # 듀티비 설정
            p.ChangeDutyCycle(val)
            # 0.1초 대기
            time.sleep(0.1)
        # 목록 나열 순서를 역순으로 변경
        dc.reverse()
        # 0.1초 대기
        time.sleep(0.1)

# 키보드 예외 검출
except KeyboardInterrupt:
    # 아무 것도 안함
    pass

# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()
