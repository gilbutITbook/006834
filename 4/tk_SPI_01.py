# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# spi 라이브러리 임포트
import spidev

# SpiDev 객체 인스턴스 생성
spi = spidev.SpiDev()

# 포트 0, 디바이스 0 SPI 오픈
spi.open(0, 0)

# 최대 클럭 스피드는 1MHz
spi.max_speed_hz=(1000000)

# 한 글자당 8비트
spi.bits_per_word=(8)

# 더미 데이터 설정(1111 1111)
dummy = 0xff

# 스타트 비트 설정(0100 0111)
start = 0x47

# 싱글엔드 모드 설정(0010 0000)
sgl = 0x20

# ch0 선택(0000 0000)
ch0 = 0x00

# ch1 선택(0001 0000)
ch1 = 0x10

# MSB 퍼스트 모드 선택(0000 1000)
msbf = 0x08

# Tk 객체 인스턴스 작성
root = Tkinter.Tk()

# Canvas 객체 인스턴스 작성
# 너비: 500, 높이: 500
c = Tkinter.Canvas(root, width = 500, height = 500)

# Canvas 배치
c.pack()

# 원 그리기
# 좌표 (200, 200)에서 (220, 220), 색상: 파랑
cc = c.create_oval(200, 200, 220, 220, fill = 'blue')

# IC에서 데이터를 취득하는 함수 정의
def measure(ch):
    # SPI 인터페이스로 데이터 송수신
    ad = spi.xfer2( [ (start + sgl + ch + msbf), dummy ] )
    # 수신한 2바이트 데이터를 10비트 데이터로 합침
    val = ( ( (ad[0] & 0x03) << 8) + ad[1] ) - 512
    # 결과 반환
    return val

# 측정값으로 원 이동량을 결정하는 함수 정의
def movement(val):
    # 측정값으로 이동량을 결정
    m_val = 0
    if val > 255 :
        m_val = -10
    elif val > 63 :
        m_val = -5
    elif val < -255 :
        m_val = 10
    elif val < -63 :
        m_val = 5
    # 결과 반환
    return m_val

# 각 채널의 측정값에서 이동량을 구하는 함수를 정의
def check_AD():
    # ch0 데이터 취득
    mes_ch0 = measure(ch0)
    # ch1 데이터 취득
    mes_ch1 = measure(ch1)
    # 결과를 리스트로 반환
    return [ movement(mes_ch0), movement(mes_ch1) ]

# 원을 움직이는 함수 정의
def draw():
    # 이동량 취득
    diff = check_AD()
    # 이동량만큼 원을 움직임
    c.move(cc, diff[0], diff[1] )
    # 0.05초 뒤에 자기 자신을 호출
    root.after(50, draw)

# draw 함수 실행
draw()

# root 표시
root.mainloop()
