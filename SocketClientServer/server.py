import socket

def run_server(port=4000):
    host = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)

        conn, addr = s.accept()
        msg = conn.recv(1024)

        print(f'{msg.decode()}')
        conn.sendall(msg)
        conn.close()

if __name__ == '__main__':
    run_server()

'''
import socket // 소켓 import
def run_server(port=4000): // 서버 실행 정의 (포트는 4000으로 임의 지정)
  host = '' // 호스트 저장
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: // 소켓 선언 (s라는 이름으로 지정)
    s.bind((host, port)) // 소켓 바인드(호스트, 포트)
    s.listen(1) // 클라이언트 연결을 받는 상태
    conn, addr = s.accept() // 클라이언트로부터 소켓과 클라이언트 주소 반환
    msg = conn.recv(1024) // 연결된 클라이언트로부터 데이터 받음 (1024 바이트)
    print(f'{msg.decode()}') // 받은 데이터 출력
    conn.sendall(msg) // 다시 데이터 보내기
    conn.close() // 연결 종료
if __name__ == '__main__':
  run_server() // 서버 실행
'''
