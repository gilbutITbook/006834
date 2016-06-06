# coding: utf-8

#GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

#time 라이브러리 임포트
import time

# 핀번호 할당법은 커넥터 핀번호로 설정
GPIO.setmode(GPIO.BOARD)

# 핀번호 대입
SRV = 12

# 출력 핀으로 설정
GPIO.setup(SRV, GPIO.OUT)

# 주파수 설정
freq = 100.0
# 각도의 최소값 설정
deg_min = 0.0
# 각도의 최대값 설정
deg_max = 180.0
# PWM 신호의 최소 듀티 설정
dc_min = 5.0
# PWM 신호의 최대 듀티 설정
dc_max = 22.0

# 각도를 듀티비로 환산하는 함수 정의
def convert_dc( deg ):
    return ( (deg - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)

# PWM 객체 인스턴스 생성
# 출력핀: SRV, 주파수: freq
p = GPIO.PWM(SRV, freq)

# PWM 신호 출력 시작
p.start(0)

# 예외 처리
try:
   # 무한 반복
   while 1:
        # 각도를 0~180까지 10씩 변화
        for deg in range(0, 181, 10):
            # 듀티비를 설정
            dc = convert_dc( float(deg) )
            # PWM 신호 듀티비를 변경해서 PWM 신호 출력
            p.ChangeDutyCycle( dc )
            # 1초 대기
            time.sleep(1)
        # 각도를 180~0까지 -10씩 변화
        for deg in range(180, -1, -10):
            # 듀티비 설정
            dc = convert_dc( float(deg) )
            # PWM 신호 듀티비를 변경해서 PWM 신호 출력
            p.ChangeDutyCycle( dc )
            # 1초 대기
            time.sleep(1)

# 키보드 예외 검출
except KeyboardInterrupt:
   # 아무 것도 하지 않음
   pass

# PWM 정지
p.stop()

# GPIO 해방
GPIO.cleanup()
