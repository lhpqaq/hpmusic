def msTotime(ms):
	sec = int(ms/1000)
	mi = int(sec/60)
	sec = sec%60
	if(mi<10):
		smi = '0'+str(mi)
	else:
		smi = str(mi)
	if(sec<10):
		ssec = '0'+str(sec)
	else:
		ssec = str(sec)
	st = smi+':'+ssec
	return mi,sec,st

