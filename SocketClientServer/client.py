import socket

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 4000))
        line = input(':')
        s.sendall(line.encode())
        resp = s.recv(1024)
        print(f'>{resp.decode()}')

if __name__ == '__main__':
    run()

'''
def run():
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 4000)) // 호스트와 포트로 서버 연결 진행
    line = input(':') // 입력 값
    s.sendall(line.encode()) // 입력된 값을 서버로 전송
    resp = s.recv(1024) // 서버로부터 recv를 통해 데이터 받음
    print(f'>{resp.decode()}') // 받은 데이터를 출력
if __name__ == '__main__':
  run()
'''