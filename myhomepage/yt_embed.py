import urllib.parse as urlparse

def getVideoID(yt_link):
	url_data = urlparse.urlparse(yt_link)
	query = urlparse.parse_qs(url_data.query)
	video = query["v"][0]

	return(video)