import urllib
import time
from subprocess import call
from bs4 import BeautifulSoup

rss ='http://feeds.soundcloud.com/users/soundcloud:users:67316412/sounds.rss'


try:
	while True:
		print('awake')

		url = urllib.request.urlopen(rss)
		soup  = BeautifulSoup(url,'lxml')

		for episode in soup.find_all('item'):
			for name in episode.find_all('title'):
				name = name.get_text()
				if name.find('Modern')<0:
					episode.decompose() 

		for podname in soup.find_all('itunes:name'):
			podname.contents[0].replace_with('Modern Sabahlar')
		for podtitle in soup.find_all('title'):
			podtitle.contents[0].replace_with('Modern Sabahlar')
		for podauthor in soup.find_all('itunes:author'):
			for i in range(len(podauthor.contents)):
				podauthor.contents[i].replace_with('Ege, Fahir bazen de Oktay') 
		for podimage in soup.find_all('image'):
			for url in podimage.find_all('url'):
				url.contents[0].replace_with('http://i1.sndcdn.com/artworks-000542024913-di980o-original.jpg')  
		for image_url in soup.find_all('itunes:image', href=True):
			image_url['href']='http://i1.sndcdn.com/artworks-000542024913-di980o-original.jpg'

		with open("modernsabahlar.rss", "w") as file:
			file.write(str(soup))
		
		Upload = "/home/pi/Desktop/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/Rss/modernsabahlar.rss /Modern_Sabahlar.rss"
		call ([Upload], shell=True)
		time.sleep(1800)

except KeyboardInterrupt:
	print('Manual break by user')