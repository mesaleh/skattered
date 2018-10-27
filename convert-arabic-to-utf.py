import sys
import codecs
import os.path

try:
	fansi_name = sys.argv[1]
except:
	print("No input file name provided")
	sys.exit()
	
if(not os.path.exists(fansi_name) or not os.path.isfile(fansi_name)):
	print("File doesn't exist")
	sys.exit()
	

fansi = open(fansi_name, mode="rb")
ofpath, ext = os.path.splitext(fansi_name)
fansiout = open(ofpath + "-utf" + ext, mode="wb")


futf = codecs.StreamRecoder(fansi,
    codecs.getencoder('utf-8'), codecs.getdecoder('utf-8'),
    codecs.getreader('cp1256'), codecs.getwriter('cp1256') )


fbytes = futf.read()
fansiout.write(fbytes)
fansi.close()
fansiout.close()
