#-*- coding: utf-8 -*-
#위는 파이썬 코드에 주석이라도 한글이 들어가면 인코딩 오류가 나기 때문에 파이썬 파일 내의 인코딩을 utf-8로 바꾼다는 주석입니다.
#인터넷 가면 많이 찾을 수 있습니다
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #빈 소켓 생성

s.bind(('127.0.0.1', 1234)) # s라는 소켓으로 127.0.0.1의 1234 포트를
#사용하겠다고 bind함수를 호출함(호출 매개변수 : 튜플(아이피, 포트))

s.listen(1) # 바인드 된 포트에 접속하는 것을 기다리게 한다.(접속을 기다림)
# 최대 1명이 동시 접속 가능함

clientsocket, clientaddr = s.accept() # listening중이다 접속 요청이 온 것이 확인이 되면 accept로
#접속을 허가한다(이 때 상대방의 요청을 받아서 사용할 소켓을 clientsocket에 저장하고 상대방의 정보를 clientaddr에 저장한다)
#accept 함수는 튜플을 리턴하기 때문에 저장을 받을 변수를 두 개를 동시에 선언하며 받게 한다.

message = 'hello my server!'

clientsocket.send(message.encode())
#접속이 허가된 클라이언트 소켓에 'hello my server!'라는 문자열을 보낸다
#문자열 뒤에 붙인 encode는 3.x 버전에서는 send 함수가 문자열이 아닌 bytes 단위로 보내야 해서 오류가 발생해 encode 라는 함수를
#사용해야 한다고 한다

s.close()#소켓을 닫습니다
