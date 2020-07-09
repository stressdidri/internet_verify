import os
import sys
import time
import urllib
import subprocess

def main():
	
	try :
		stri = "https://www.google.ro"
		data = urllib.urlopen(stri)
		print "Conectat ..."
		#time.sleep(2)
	except:
		print "!!! DECONECTAT !!!"
		time.sleep(60)
		subprocess.call('(php /var/www/erroare_internet.php)', shell=True)#, '-l'
		subprocess.call('(play internet_offline.mp3)', shell=True)#,


while True:
    main()
    time.sleep(60) #make function to sleep for 10 seconds