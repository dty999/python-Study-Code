import socket

def getwebsource(url):
	# 初始信息
	host = url
	port = 80

	# 解析域名获取IP
	ip = socket.gethostbyname(host)
	print ('Ip address of ' + host + ' is ' + ip)

	# 通过IP连接主机
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))

	#Send some data to remote server
	message = b"GET / HTTP/1.1\r\n\r\n"
	 
	try :
	    #Set the whole string
	    s.sendall(message)
	except socket.error:
	    #Send failed
	    sys.exit()
	reply = s.recv(4096)
	return reply
	s.close()
