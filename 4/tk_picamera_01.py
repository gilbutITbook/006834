# coding: utf-8

# picamera 라이브러리 임포트
import picamera

# Tkinter 라이브버리 임포트
import Tkinter

# 지정한 해상도로 촬영하는 함수
def cap_img():
    # 선택한 값에 따라 해상도 설정
    if res.get() == 3:
        camera.resolution = (1024, 768)
    elif res.get() == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)

    # 선택한 값에 따라 이펙트 설정
    if eff.get() == 3:
        camera.image_effect = effect[2][0]
    elif eff.get() == 2:
        camera.image_effect = effect[1][0]
    else:
        camera.image_effect = effect[0][0]

    # 텍스트 박스에서 파일명 취득
    filename = e.get()

    # 촬영하고 파일에 저장
    camera.capture(filename + '.jpg')

    # 라벨 Picture Saved 표시
    label3 = Tkinter.Label(root, text = 'Picture Saved')
    # 라벨 배치
    label3.pack()

# Tk 객체 인스턴스 생성
root = Tkinter.Tk()

# PiCamera 객체 인스턴스 생성
with picamera.PiCamera() as camera:

    # 라디오 버튼에 표시하는 라벨 목록을 정의
    resolution = [('320x240', 1), ('640x480', 2), ('1024x768', 3)]
    effect = [('none', 1), ('oilpaint', 2), ('negative', 3)]

    # 해상도를 표시하는 Variable 객체 인스턴스를 정수형으로 생성
    res = Tkinter.IntVar()
    # 기본값 1을 설정
    res.set(1)

    # 이펙트를 표시하는 Variable 객체 인스턴스를 정수형으로 생성
    eff = Tkinter.IntVar()
    # 기본값 1을 설정
    eff.set(1)

    # 라벨 Resolution 생성
    label1 = Tkinter.Label(root, text = 'Resolution')
    # 라벨 배치
    label1.pack()

    for text, mode in resolution:
        # 해상도 선택용 라디오 버튼 생성
        rb = Tkinter.Radiobutton(root, text = text, variable = res, value = mode)
        # 라디오 버튼 배치
        rb.pack(anchor='w')

    # 라벨 Effect 작성
    label2 = Tkinter.Label(root, text = 'Effect')
    # 라벨 배치
    label2.pack()

    for text, mode in effect:
        # 이펙트 선택용 라디오 버튼 생성
        rb2 = Tkinter.Radiobutton(root, text = text, variable = eff, value = mode)
        # 라디오 버튼 배치
        rb2.pack(anchor='w')

    # 파일명 입력용 텍스트 박스 생성
    e = Tkinter.Entry(root)
    # 텍스트 박스 배치
    e.pack()

    # 촬영 버튼 생성
    b = Tkinter.Button(root, text = 'Picture', width = 10, command = cap_img)
    # 버튼 배치
    b.pack()

    # root 표시
    root.mainloop()
