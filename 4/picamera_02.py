# coding: utf-8

# picamera 라이브러리 임포트
import picamera

# time 라이브러리 임포트
import time

# PiCamera 객체 인스턴스 생성
with picamera.PiCamera() as camera:

    # 화면 해상도를 선택
    res = int(raw_input('Resolution(1:320x240, 2:640x480, 3:1024x768)?'))

    # 선택한 값에 따라 해상도 설정
    if res == 3:
        camera.resolution = (1024, 768)
    elif res == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)

    # 파일명 입력
    filename = raw_input('File Name?')

    # 프리뷰 화면 표시
    camera.start_preview()

    # 촬영하고 파일 저장
    camera.start_recording(output = filename + '.h264')

    # 5초 대기
    camera.wait_recording(5)

    # 프리뷰 화면 종료
    camera.stop_preview()

    # 촬영 종료
    camera.stop_recording()
