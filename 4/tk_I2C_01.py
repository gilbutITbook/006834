# coding: utf-8

# Tkinter 라이브러리 임포트
import Tkinter

# smbus 라이브러리 임포트
import smbus

# smbus 객체 인스턴스 생성
bus = smbus.SMBus(1)

# IC 주소
address = 0x1D

# 각축 데이터 주소
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# Canvas 객체 인스턴스 생성
# 폭: 200, 높이: 200
c = Tkinter.Canvas(root, width = 500, height = 500)
# 캔버스 배치
c.pack()

# 원 작성
# 좌표 (200, 200)에서 (220, 220), 색: 녹색
cc = c.create_oval(200, 200, 220, 220, fill = 'green')

# IC 초기화하는 함수
def init_ADXL345():
    # POWER_CTL 레지스터(주소: 0x2D) Measure 비트에 1을 써서 측정 시작
    bus.write_byte_data(address, 0x2D, 0x08)

# IC에서 데이터를 취득하는 함수
def measure_acc(adr):
    # 각축의 측정값 하위 바이트를 읽음
    acc0 = bus.read_byte_data(address, adr)
    # 각축의 측정값 상위 바이트를 읽음
    acc1 = bus.read_byte_data(address, adr + 1)

    # 수신한 2바이트 데이터를 10비트 데이터로 합침
    acc = (acc1 << 8) + acc0
    # 부호가 있는지(10비트째가 1인지) 판정
    if acc > 0x1FF:
        # 음수로 변환
        acc = (65536 - acc) * -1
    # 가속도 값으로 변환
    acc = acc * 3.9 / 1000

    # 결과 반환
    return acc

# 측정값에서 원 이동량을 결정하는 함수
def movement(val):
    # 측정값에서 이동량을 결정
    m_val = 0
    if val > 0.5 :
        m_val = 10
    elif val > 0.2 :
        m_val = 5
    elif val < -0.5 :
        m_val = -10
    elif val < -0.2 :
        m_val = -5
    # 결과 반환
    return m_val

# 각 채널 측정값에서 이동량을 구하는 함수
def check_acc():
    # x방향 데이터 취득
    x_acc = measure_acc(x_adr) * -1
    # y방향 데이터 취득
    y_acc = measure_acc(y_adr)
    # 결과를 리스트로 반환
    return [movement(x_acc), movement(y_acc)]

# 원을 움직이는 함수
def draw():
    # 이동량 취득
    diff = check_acc()
    # 이동량에 따라 움직임
    c.move(cc, diff[0], diff[1])
    # 0.05초 뒤에 자기 자신을 호출
    root.after(50, draw)

# IC 초기화
init_ADXL345()

# draw 함수 실행
draw()

# root 표시
root.mainloop()
