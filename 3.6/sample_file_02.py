# coding: utf-8

# 경로, 파일명을 filename으로 지정
filename = '/home/pi/python_output/myfile.txt'

# 파일을 append 모드로 열어서 f에 저장
# 줄바꿈 코드와 문자열 is happy!를 써넣기
with open(filename, mode = 'a') as f:
    f.write('\n is happy!')

# 파일을 read 모드를 열어서 f에 저장
# 한 줄씩 읽어서 출력
with open (filename, mode = 'r') as f:
    for line in f:
        print line
