import socket
import os
import sys

def Banner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connet((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, filename):
	f = open(filename, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print '[+] El Servidor es Vulnerable' +\
				banner.strip('\n')
				

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] ' + filename + '\n no se encuentra o no existe'
			exit(0)
			if not os.access(filename.os.R_OK):
				print '[-] ' +filename + '\n Acceso denegado, no tiene permisos suficientes'
				exit(0)
			else :
				print '[-] Uso: ' + str(sys.argv[0]) + '\n <Archivo con las Vulnerabilidades>'
				exit(0)
				portList = [21,22,25,80,110,443]
				for a in range(147,150):
					ip = '127.0.0.1' + str(x)
					for port in portList:
						banner = retBanner(ip,port)
						if banner:
							print '[+] ' + ip + ': ' + banner
							checkVulns(banner, filename)

if __name__ == '__main__':
	main()
