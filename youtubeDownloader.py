import youtube_dl
import pprint

ydl_opts = {}

def download():
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])

start = 1
while (start == 1):
	url = input("Enter the link: ")
	url = url.strip()

	download()
	pprint(ydl_opts)
	start = int(input("\nEnter 1 if you want to download more videos \nEnter 0 if you are done\n"))