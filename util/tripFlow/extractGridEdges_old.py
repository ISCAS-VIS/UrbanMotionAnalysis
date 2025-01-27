#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Input Data Format
# [hour, id, time, lat, lng, from_lat, from_lng, from_time, to_lat, to_Lng, to_time]
# 
# Output Data Format
# [lng, lat, gid, from/to, speed, direction, angle, strength]

import os
import json
from util.tripFlow.base import getFormatGID
from util.tripFlow.base import getRealDistance
from util.tripFlow.base import getDirection
from util.tripFlow.base import parseFormatGID
from util.tripFlow.base import getGIDByIndex
from math import sqrt, pow, acos, pi
import math


class ExtractGridEdges(object):
	def __init__(self, PROP):
		super(ExtractGridEdges, self).__init__()
		self.INPUT_PATH = os.path.join(PROP['IDIRECTORY'], 'bj-byhour-tf')
		self.OUTPUT_PATH = os.path.join(PROP['ODIRECTORY'], 'bj-byhour-rec')
		self.index = PROP['index']
		self.delta = PROP['delta'] * PROP['delta'] * 2 if PROP['delta'] > 0 else -1.0
		self.resByDir = {'e': {}, 'n': {}, 'w': {}, 's': {}}  # åæ¹åç»æ?
		self.resByCate = {'from': {}, 'to': {}}  # åè¿åºç»æ?
		self.singleDirectionCount = 0
		self.subfix = PROP['subfix']
    
	def run(self):
		ifile = os.path.join(self.INPUT_PATH, 'traveldata-%d' % (self.index))  # å°æ¶æä»¶
		
		self.iterateFile(ifile)
		res = self.outputToFile()
		return {
			'count': self.singleDirectionCount,
			'res': res
		}
		
	def iterateFile(self, file):
		print "Delta for current running %f" % self.delta
		count = 0
		with open(file, 'rb') as f:
			firstLine = True
			currentNo = -1
			fromLat = -1
			fromLng = -1
			fromTime = -1

			for line in f:
				count += 1
				line = line.strip('\n')
				linelist = line.split(',')
				
				# æç¨æ è¯
				no = "%s-%s-%s-%s" % (linelist[5], linelist[6], linelist[8], linelist[9])
				toLat = linelist[3]
				toLng = linelist[4]
				toTime = int(linelist[2])

				if firstLine:  # ç¬¬ä¸è¡åå§å
					firstLine = False
					currentNo = no
					fromLat = toLat
					fromLng = toLng
					fromTime = toTime
				else:
					if currentNo == no:  # åä¸æ®µæç¨?
						# å¦æå½åç¹ä½ç½®ä¸ååç»§ç»­éå
						if (fromLat == toLat and fromLng == toLng) or fromTime == toTime:
							continue

						fPoint = [float(fromLng), float(fromLat)]
						tPoint = [float(toLng), float(toLat)]

						fromGid = getFormatGID(fPoint)['gid']
						toGid = getFormatGID(tPoint)['gid']
						distance = getRealDistance(fromLng, fromLat, toLng, toLat)
						speed = distance / (toTime-fromTime)
						direction = getDirection(fPoint, tPoint)  # w n s e åä¸ªå­ç¬¦ä¹ä¸

						self.updateResByLine(fPoint, tPoint, fromGid, toGid, direction, speed)
						
						fromLat = toLat
						fromLng = toLng
						fromTime = toTime
					else:  # æ°æç¨ç¬¬ä¸ä¸ªç¹
						currentNo = no
						fromLat = toLat
						fromLng = toLng
						fromTime = toTime

		f.close()
		print "Total %d records in this file." % (count)

	def updateResByLine(self, fPoint, tPoint, fromGid, toGid, direction, speed):
		self.singleDirectionCount += 1

		# å¤çæ¹åä¸ç½æ ¼é´çç¸äº¤ç¹
		fGidIPoint, tGidIPoint = self.getGridIntersection(fPoint, tPoint, fromGid, toGid, direction)
		fGidIPointStr = "%.6f,%.6f" % (fGidIPoint[0], fGidIPoint[1])
		tGidIPointStr = "%.6f,%.6f" % (tGidIPoint[0], tGidIPoint[1])

		# åæ¹åç»æå­ç¬¦ä¸²
		# [lng, lat, gid, from/to, speed, direction]
		fromVecStr = "%s,%d,from,%f,%s" % (fGidIPointStr, fromGid, speed, direction)
		toVecStr = "%s,%d,to,%f,%s" % (tGidIPointStr, toGid, speed, direction)

		# å¤çä¸ï¼åæ¹åçæéåæ°æ®å­å¨
		if fromGid in self.resByDir[direction].keys():
			self.resByDir[direction][fromGid].append(fromVecStr)
		else:
			self.resByDir[direction][fromGid] = [fromVecStr]

		if toGid in self.resByDir[direction].keys():
			self.resByDir[direction][toGid].append(toVecStr)
		else:
			self.resByDir[direction][toGid] = [toVecStr]
		# END

		# å¤çäºï¼ååºå¥çæéåæ°æ®ï¼å½ä¸ååéï¼å­å¨
		fX = fPoint[1] - fGidIPoint[1]
		fY = fPoint[0] - fGidIPoint[0]
		tX = tPoint[1] - tGidIPoint[1]
		tY = tPoint[0] - tGidIPoint[0]
		fiDis = sqrt(pow(fX, 2) + pow(fY, 2))
		tiDis = sqrt(pow(tX, 2) + pow(tY, 2))

		# è®¡ç®è¾¹æ¹ååå¶ç»å¯¹è·ç¦?
		vecY = tPoint[0] - fPoint[0]
		vecX = tPoint[1] - fPoint[1]
		vecDis = sqrt(pow(vecY, 2) + pow(vecX, 2))

		angleLng = vecY / vecDis
		angleLat = vecX / vecDis
		tmpLng = fPoint[0] + angleLng
		tmpLat = fPoint[1] + angleLat
		fCircleIPointStr = "%.6f,%.6f" % (tmpLng, tmpLat)
		fangle = acos(angleLat) * 180 / pi
		if angleLng < 0 and fangle > 0.1:
			fangle = 360 - fangle

		fromCVecStr = "%s,%d,from,%f,%s,%.1f,1" % (fCircleIPointStr, fromGid, speed, direction, fangle)

		if fromGid in self.resByCate['from'].keys():
			self.resByCate['from'][fromGid].append(fromCVecStr)
		else:
			self.resByCate['from'][fromGid] = [fromCVecStr]

		# KDE å¤ç from ç¸é»24ä¸ªå°æ ¼æ¹åé®é¢?
		if self.delta > 0:
			for x in xrange(-2, 3):
				for y in xrange(-2, 3):
					if x == 0 and y == 0:
						continue

					newGID = getGIDByIndex(fromGid, x, y)
					newStrength = pow(math.e, -(x*x+y*y)/self.delta)
					fromCVecStr = "%s,%d,from,%f,%s,%.1f,%f" % (fCircleIPointStr, newGID, speed, direction, fangle, newStrength)

					if newGID in self.resByCate['from'].keys():
						self.resByCate['from'][newGID].append(fromCVecStr)
					else:
						self.resByCate['from'][newGID] = [fromCVecStr]
		# KDE END

		tmpLng = tPoint[0] + angleLng
		tmpLat = tPoint[1] + angleLat
		tCircleIPointStr = "%.6f,%.6f" % (tmpLng, tmpLat)
		tangle = acos(angleLat) * 180 / pi
		toCVecStr = "%s,%d,to,%f,%s,%.1f,1" % (tCircleIPointStr, toGid, speed, direction, tangle)

		if toGid in self.resByCate['to'].keys():
			self.resByCate['to'][toGid].append(toCVecStr)
		else:
			self.resByCate['to'][toGid] = [toCVecStr]

		# KDE å¤ç to ç¸é»24ä¸ªå°æ ¼æ¹åé®é¢?
		if self.delta > 0:
			for x in xrange(-2, 3):
				for y in xrange(-2, 3):
					if x == 0 and y == 0:
						continue

					newGID = getGIDByIndex(toGid, x, y)
					newStrength = pow(math.e, -(x*x+y*y)/self.delta)
					toCVecStr = "%s,%d,to,%f,%s,%.1f,%f" % (tCircleIPointStr, newGID, speed, direction, tangle, newStrength)

					if newGID in self.resByCate['to'].keys():
						self.resByCate['to'][newGID].append(toCVecStr)
					else:
						self.resByCate['to'][newGID] = [toCVecStr]
		# KDE END
		# END

		return 0

	def getGridIntersection(self, fPoint, tPoint, fromGid, toGid, direction):
		"""
		è®¡ç®äº¤åç¹ï¼ææç¹æ ¼å¼åä¸º [lng, lat]
			:param self: 
			:param fPoint: æ¥æºç?
			:param tPoint: å°è¾¾ç?
			:param fromGid: æ¥æº gid
			:param toGid: å°è¾¾ gid
			:param direction: æ¹å
		"""

		fGIPoint, tGIPoint = [], []
		fromLat = float(fPoint[1])
		fromLng = float(fPoint[0])
		toLat = float(tPoint[1])
		toLng = float(tPoint[0])

		# å¤ç from/to
		toDirection = {
			'n': 's',
			's': 'n',
			'w': 'e',
			'e': 'w'
		}
		pfRes = parseFormatGID(fromGid, direction)
		ptRes = parseFormatGID(toGid, toDirection[direction])
		fGidLine = pfRes['dlinePoint']
		tGidLine = ptRes['dlinePoint']
		fLng = pfRes['lng']
		fLat = pfRes['lat']
		tLng = ptRes['lng']
		tLat = ptRes['lat']

		# è®¡ç®ç½æ ¼æ¹è¾¹äº¤ç¹
		if direction in ['n', 's']:  # ä¸å¹³è¡ç»´åº¦çº¿ç¸äº¤
			k = (toLng - fromLng) / (toLat - fromLat)
			b1, b2 = fLng, tLng
			fIlng = b1 + (fGidLine - fromLat) * k
			fGIPoint = [fIlng, fGidLine]
			tIlng = b2 + (tGidLine - fromLat) * k
			tGIPoint = [tIlng, tGidLine]
		else:  # ä¸å¹³è¡ç»åº¦çº¿ç¸äº¤
			k = (toLat - fromLat) / (toLng - fromLng)
			b1, b2 = fLat, tLat
			fIlat = b1 + (fGidLine - fromLng) * k
			fGIPoint = [fGidLine, fIlat]
			tIlat = b2 + (tGidLine - fromLng) * k
			tGIPoint = [tGidLine,tIlat]

		return fGIPoint, tGIPoint
	
	def outputToFile(self):
		"""
		éç¨è¾åºæä»¶å½æ°
			:param self: 
			:param res: 
		"""
		
		# å¾æ´æ?
		ores = []
		i = 0
		gidNum, recNum = 0, 0
		memres = [[] for x in xrange(0, 4)]
		for key, val in self.resByDir.iteritems():  # ä¸è¥¿åååä¸ªæ¹åéå
			for subkey ,subval in val.iteritems():  # æ¯ä¸ªæ¹åéä¸å?gid æ°æ®éåï¼subval ä¸ºæ°ç»?
				gidNum += 1
				recNum += len(subval)
				ores.append('\n'.join(subval))
				memres[i] += subval
			i += 1
		
		print "Total %d gids and %d records in four directions" % (gidNum, recNum)

		ofile = os.path.join(self.OUTPUT_PATH, 'triprec-direction-%d-%s' % (self.index, self.subfix))
		with open(ofile, 'wb') as f:
			f.write('\n'.join(ores))
		f.close()

		# smooth - Category and angle
		ofile = os.path.join(self.OUTPUT_PATH, 'triprec-smooth-%d-%s.json' % (self.index, self.subfix))
		with open(ofile, 'wb') as f:
			json.dump(self.resByCate, f)
		f.close()

		return {
			'resByDir': memres, 
			'resByCate': self.resByCate
		}