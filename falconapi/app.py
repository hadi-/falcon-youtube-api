
import falcon
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json

#change with your API_KEY
DEVELOPER_KEY = "YOUR_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
#get lists video
class Lists(object):
    def on_get(self, req, resp):
        # print(req.query_string)
        try:
            resp.body = youtube_search(req.params)
        except HttpError, e:
            print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

#get video detail
class Detail(object):
    def on_get(self, req, resp, video_id):
        print(req)
        try:
            resp.body = youtube_get_detail(video_id)
        except HttpError, e:
            print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)


#search youtube
def youtube_search(object):
    search_response = youtube.search().list(
        q=object,
        part="id,snippet",
        maxResults=10
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append({'title' : search_result["snippet"]["title"],
            'videoid' : search_result["id"]["videoId"]})

    return json.dumps(videos, encoding='utf-8')
# get detail video by ID
def youtube_get_detail(object):
    search_response = youtube.videos().list(
        id=object,
        part="snippet,contentDetails,statistics",
    ).execute()

    videos = search_response.get("items", [])
    return json.dumps(videos, encoding='utf-8')



#defining routes
api = application = falcon.API()
api.add_route('/', Lists())
api.add_route('/details/{video_id}', Detail())
