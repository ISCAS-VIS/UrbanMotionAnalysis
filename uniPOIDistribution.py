#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 

import sys
import time
import logging
import getopt
from multiprocessing import Process
# from util.preprocess import mergeMultiProcessMatFiles
from util.UniPOIDisBasic import UniPOIDisBasic
from util.dbopts import connectMongo


def processTask(x, city, directory, inum, onum, poiMap, subopath): 
	PROP = {
		'INDEX': x, 
		'CITY': city, 
		'DIRECTORY': directory, 
		'INUM': inum, 
		'ONUM': onum,
		'poiMap': poiMap,
		'SUBOPATH': subopath
	}

	task = UniPOIDisBasic(PROP)
	task.run()


def usage():
	"""
	使用说明函数
	"""
	print "python -d /datasets -i 86"


def main(argv):
	"""
	主入口函数
		:param argv: city 表示城市， directory 表示路径， inum 表示输入文件总数， onum 表示输出文件总数， jnum 表示处理进程数，通常和 onum 一致， subopath 为结果存储的子目录名字
	"""
	try:
		argsArray = ["help", "city=", 'directory=', 'inum=', 'onum=', 'jnum=']
		opts, args = getopt.getopt(argv, "hc:d:i:o:j:", argsArray)
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit(2)

	city, directory, inum, onum, jnum, stdoutdir = 'beijing', '/home/tao.jiang/datasets/JingJinJi/records', 86, 20, 20, 'bj-newvis-sg'
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ("-c", "--city"):
			city = arg
		elif opt in ("-d", "--directory"):
			directory = arg
		elif opt in ('-i', '--inum'):
			inum = int(arg)
		elif opt in ('-o', '--onum'):
			onum = int(arg)
		elif opt in ('-j', '--jnum'):
			jnum = int(arg)

	STARTTIME = time.time()
	print "Start approach at %s" % STARTTIME

	# 固定网格总数
	poiMap = {}
	conn, db = connectMongo('stvis')
	plist = list(db['grids'].find({}, {
		'pid': 1,
		'nid': 1
	}))
	conn.close()
	
	print "POI List length: %d" % len(plist)
	for each in plist:
		poiMap[each['nid']] = each['pid']
	# plist = None

	# @多进程运行程序 START
	jobs = []

	for x in xrange(0, jnum):
		jobs.append(Process(target=processTask, args=(x, city, directory, inum, onum, poiMap, stdoutdir)))
		jobs[x].start()

	for job in jobs:
		job.join()

	# 文件过于庞大，故不做合并处理
	# mergeMultiProcessMatFiles(directory, stdoutdir, jnum)

	# @多进程运行程序 END

	print "END TIME: %s" % time.time()


if __name__ == '__main__':
	logging.basicConfig(filename='logger-unipoidistribution.log', level=logging.DEBUG)
	main(sys.argv[1:])