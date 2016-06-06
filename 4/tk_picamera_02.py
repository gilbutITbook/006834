# coding: utf-8

# picamera 라이브러리 임포트
import picamera

# Tkinter 라이브러리 임포트
import Tkinter

# 지정한 해상도, 각도로 촬영하는 함수
def rec_vdo():
    # 선택한 값에 따라 해상도 설정
    if res.get() == 3:
        camera.resolution = (1024, 768)
    elif res.get() == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)

    # 선택한 값에 따라 회전각도 설정
    if rot.get() == 4:
        camera.rotation = int(rotation[3][0])
    elif rot.get() == 3:
        camera.rotation = int(rotation[2][0])
    elif rot.get() == 2:
        camera.rotation = int(rotation[1][0])
    else:
        camera.rotation = int(rotation[0][0])

    # 텍스트 박스에서 파일명 취득
    filename = e.get()
    # 촬영을 시작하고 파일 저장
    camera.start_recording(filename+'.h264')

    # 5초 대기
    camera.wait_recording(5)

    # 촬영 종료
    camera.stop_recording()

    # 라벨 Movie Saved 생성
    label3 = Tkinter.Label(root, text = 'Movie Saved')
    # 라벨 배치
    label3.pack()

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# PiCamera 객체 인스턴스 생성
with picamera.PiCamera() as camera:

    # 해상도와 회전 각도 목록 정의
    resolution = [('320x240', 1), ('640x480', 2), ('1024x768', 3)]
    rotation = [('0', 1), ('90', 2), ('180', 3), ('270', 4)]

    # 해상도를 나타내는 Variable 객체 인스턴스를 정수형으로 생성
    res = Tkinter.IntVar()
    # 기본값 1을 설정
    res.set(1)

    # 회전 각도를 나타내는 Variable 객체 인스턴스를 정수형으로 생성
    rot = Tkinter.IntVar()
    # 기본값 1을 설정
    rot.set(1)

    # 라벨 Resolution 생성
    label1 = Tkinter.Label(root, text = 'Resolution')
    # 라벨 배치
    label1.pack()

    for text, mode in resolution:
        # 해상도 선택용 라디오 버튼 생성
        rb = Tkinter.Radiobutton(root, text = text, variable = res, value = mode)
        # 라디오 버튼 배치
        rb.pack(anchor = 'w')

    # 라벨 rotation 생성
    label2 = Tkinter.Label(root, text = 'rotation')
    # 라벨 배치
    label2.pack()

    for text, mode in rotation:
        # 회전 각도 선택용 라디오 버튼 생성
        rb2 = Tkinter.Radiobutton(root, text = text, variable = rot, value = mode)
        # 라디오 버튼 배치
        rb2.pack(anchor = 'w')

    # 파일명 입력용 텍스트 박스 생성
    e = Tkinter.Entry(root)
    # 텍스트 박스 배치
    e.pack()

    # 촬영 시작 버튼 작성
    b = Tkinter.Button(root, text = "Movie", width = 10, command = rec_vdo)
    # 버튼 배치
    b.pack()

    # root 표시
    root.mainloop()
