# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# 핀번호 할당법을 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)
# 사용하는 핀번호를 대입
SW = 7
LED = 11

# 11번 핀을 출력 핀으로 설정, 초기출력은 로우레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# 7번 핀을 입력핀으로 설정
GPIO.setup(SW, GPIO.IN)

# 예외 처리
try:
    # 무한 반복
    while 1:
        # 스위치 상태를 변수 key_in에 대입
        key_in = GPIO.input(SW)
        # 변수 key_in 상태 판별
        if key_in==0:
            # 하이레벨 출력
            GPIO.output(LED, GPIO.HIGH)
        else:
            # 로우레벨 출력
            GPIO.output(LED, GPIO.LOW)

# 키보드 예외 검출
except KeyboardInterrupt:
    # 아무 것도 하지 않음
    pass

# GPIO 해방
GPIO.cleanup()
