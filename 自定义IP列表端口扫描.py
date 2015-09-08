#!/usr/bin/python
# encoding=utf-8
# Filename: test.py

import threading,sys,socket
import time,argparse,Queue
import optparse

PortList = [21,22,23,25,53,80,443,445,873,1433,1521,1723,3306,3389,4848,4899,5800,5900,7001,8080,8443,8500,8888,9080,9200,27017]
#PortList1 = range(1,30000)
mutex = threading.Lock()
threads = []
queue = Queue.Queue()

def scan():
	global mutex,queue
	while True:
		try:
			item = queue.get(timeout=0.1)
			sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sk.settimeout(0.1)
			indicator = sk.connect_ex((item['ip'],int(item['port'])))
			if mutex.acquire(1):
				if indicator == 0:
					print('Server %s port %d OK!' % (item['ip'],item['port']))
				else:
					pass
				mutex.release()
		except:
			break

def main(txt,num):
	#把数组压入队列
	for i in txt:
		for j in PortList:
			queue.put({'ip': str(i),'port':int(j)})
	# 先创建线程对象
	for x in xrange(0, num):
		th = threading.Thread(target=scan)
		th.start()
		threads.append(th)
	for t in threads:
		t.join()
		
if __name__ == '__main__':
	txt = []
	parser = optparse.OptionParser('usage: %prog [options] target')
	parser.add_option('-f', '--file', dest='names_file',default='false', type='string',help='files default = false')
	parser.add_option('-t', '--threads', dest='threads_num',default=20, type='int',help='Number of threads. default = 20')
	(options, args) = parser.parse_args()
	var = "false"
	if str(options.names_file) != "false":
		f = open(str(options.names_file),"r")
		for i in f.readlines():
			txt.append(i.strip())
	else:
		if len(args) < 1:
			parser.print_help()
			sys.exit(0)
		for i in range(1,255):
			ip = args[0].split('.')[0]+'.'+args[0].split('.')[1]+'.'+args[0].split('.')[2]+'.'+str(i)
			txt.append(ip)
	time1= time.time()
	main(txt,int(options.threads_num))
	time2= time.time()
	print time2-time1
	