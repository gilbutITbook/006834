# coding: utf-8

# smbus 라이브러리 임포트
import smbus

# time 라이브러리 임포트
import time

# smbus 객체 인스턴스 생성
bus = smbus.SMBus(1)

# IC 주소
address = 0x1D

# 각축 데이터 주소
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

# 센서 IC를 초기화하는 함수
def init_ADXL345():
    # POWER_CTL 레지스터(주소: 0x2D)의 Measure 비트에 1을 써서 계측 시작
    bus.write_byte_data(address, 0x2D, 0x08)

# IC에서 데이터를 취득하는 함수
def measure_acc(adr):
    # 각축의 측정값 하위 바이트를 읽기
    acc0 = bus.read_byte_data(address, adr)
    # 각축의 측정값 상위 바이트를 읽기
    acc1 = bus.read_byte_data(address, adr + 1)

    # 수신한 2바이트 데이터를 10비트 데이터로 합치기
    acc = (acc1 << 8) + acc0
    # 부호가 있는지 여부(10비트째가 1인지) 판정
    if acc > 0x1FF:
        # 음수로 변환
        acc = (65536 - acc) * -1
    # 가속도 값으로 변환
    acc = acc * 3.9 / 1000

    # 결과 반환
    return acc

# 예외 처리
try:
    # IC 초기화
    init_ADXL345()

    # 무한 반복
    while 1:
        # 함수를 호출해서 데이터 취득
        x_acc = measure_acc(x_adr)
        y_acc = measure_acc(y_adr)
        z_acc = measure_acc(z_adr)
        # 결과 표시
        print 'X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]'
        # 0.5초 대기
        time.sleep(0.5)

# 키보드에서 예외 검출
except KeyboardInterrupt:
    # 아무 것도 하지 않음
    pass
