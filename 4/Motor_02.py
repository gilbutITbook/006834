# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time

# collections 라이브러리 deque를 임포트
from collections import deque

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀번호 대입
AIN1 = 15
BIN1 = 16
AIN2 = 18
BIN2 = 22

# 출력신호 패턴 목록 작성
sig = deque([1, 0, 0, 0])

# 회전할 스텝수
step = 100

# 회전 방향 초기값
dir = 1

# 각 핀을 출력 핀으로 설정
GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BIN2, GPIO.OUT, initial=GPIO.LOW)

# 예외 처리
try:
    # 무한 반복
    while 1:
        # step으로 지정한 스텝수만큼 반복
        for cnt in range( 0, step ):
            # 출력 신호 패턴을 순서대로 출력
            GPIO.output(AIN1, sig[0])
            GPIO.output(BIN1, sig[1])
            GPIO.output(AIN2, sig[2])
            GPIO.output(BIN2, sig[3])
            # 0.01초 대기
            time.sleep(0.01)
            # 출력 신호 패턴을 오른쪽으로 로테이트
            sig.rotate(dir)
        # 로테이트 방향을 반대로 만듬
        dir = dir * -1

# 키보드 예외 검출
except KeyboardInterrupt:
    # 아무 것도 하지 않음
    pass

# GPIO 개방
GPIO.cleanup()
