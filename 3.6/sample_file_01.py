# coding: utf-8

# 경로, 파일명을 filename에 지정
filename = '/home/pi/python_output/myfile.txt'

# 파일을 write 모드로 열고, f에 대입
# 문자열 Python을 써넣기
with open(filename, mode = 'w') as f:
    f.write('Python')

# 파일을 read 모드로 열고, f에 대입
# 한 줄을 읽어서 출력
with open (filename, mode = 'r') as f:
    print f.readline()
