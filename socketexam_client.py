#-*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#빈 소켓을 생성합니다

s.connect(('127.0.0.1', 1234))#빈 소켓으로 127.0.0.1의 1234 포트로 연결을 시도합니다
message = s.recv(100)#최대 100바이트를 연결된 소켓에서 받아옵니다(받아온 문자열을 message에 저장)

print(message)#받아온 문자열을 출력합니다
s.close()#소켓을 닫습니다
