from src.channel import Channel

class Video:
    def __init__(self, id_video):
        self.__id_video = id_video

    @property
    def id_video(self):
        return self.__id_video

    @property
    def video(self):
        return Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',id=self.__id_video).execute()

    @property
    def title(self):
        return self.video[0]['snippet']['title']

    @property
    def url(self):
        return f'https://www.youtube.com/watch?v={self.__id_video}'
    @property
    def views_count(self):
        return self.video[0]['statistics']['viewCount']

    @property
    def likes_count(self):
        return self.video[0]['statistics'][likeCount]

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, id_video, playlist_id):
        self.__id_video = id_video
        self.__playlist_id = playlist_id
        super().__init__(id_video)

