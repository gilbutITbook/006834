# coding: utf-8

# spi 라이브러리 임포트
import spidev

# time 라이브러리 임포트
import time

# SpiDev 객체 인스턴스 생성
spi = spidev.SpiDev()

# 포트 0, 디바이스 0의 SPI 오픈
spi.open(0, 0)

# 최대 클럭 스피드를 1MHz로 설정
spi.max_speed_hz=1000000

# 한 글자당 8비트로 설정
spi.bits_per_word=8

# 더미 데이터 설정(1111 1111)
dummy = 0xff

# 스타트 비트 설정(0100 0111)
start = 0x47

# 싱글 엔드 모드 설정(0010 0000)
sgl = 0x20

# ch0 선택(0000 0000)
ch0 = 0x00

# ch1 선택(0001 0000)
ch1 = 0x10

# MSB 퍼스트 모드 선택(0000 1000)
msbf = 0x08

# IC에서 데이터를 취득하는 함수 정의
def measure(ch):
    # SPI 인터페이스로 데이터 송수신
    ad = spi.xfer2( [ (start + sgl + ch + msbf), dummy ] )
    # 수신한 2바이트 데이터를 10비트 데이터로 합침
    val = ( ( ( (ad[0] & 0x03) << 8) + ad[1] ) * 3.3 ) / 1023
    # 결과 반환
    return val

# 예외 처리
try:
    # 무한 반복
    while 1:
        # 함수를 호출해서 ch0 데이터 취득
        mes_ch0 = measure(ch0)
        # 함수를 호출해서 ch1 데이터 취득
        mes_ch1 = measure(ch1)
        # 결과 표시
        print 'ch0 = %2.2f' % mes_ch0,'[V], ch1 = %2.2f' % mes_ch1,'[V]'
        # 0.5초 대기
        time.sleep(0.5)

# 키보드 예외 검출
except KeyboardInterrupt:
    # 아무 것도 하지 않음
    pass

# SPI 개방
spi.close()
