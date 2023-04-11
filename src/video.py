from src.channel1 import Channel

class Video:
    def __init__(self, id_video):
        self.__id_video = id_video
        self.__video = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',id=self.__id_video).execute()
        self.__title = self.video['items'][0]['snippet']['title']
        self.__url = f'https://www.youtube.com/watch?v={self.__id_video}'
        self.__views_count = self.video['items'][0]['statistics']['viewCount']
        self.__likes_count = self.video['items'][0]['statistics']['likeCount']

    @property
    def id_video(self):
        """ инициализация ID видео экземпляра"""
        return self.__id_video

    @property
    def video(self):
        return self.__video
##
    @property
    def title(self):
        """ инициализация названия видео экземпляра"""
        return self.__title
#
    @property
    def url(self):
        """ инициализация ссылки на видео экземпляра"""
        return self.__url
    @property
    def views_count(self):
        """инициализация количества просмотров ID видео экземпляра"""
        return self.__views_count
#
    @property
    def likes_count(self):
        """ инициализация количества лайков видео экземпляра"""
        return self.__likes_count

    def __str__(self):
        """" инициализация Метода str для вывода названия видео экземпляра"""
        return self.title


class PLVideo(Video):
    """ Создание класса с инициализацией атрибутов согласно ТЗ"""
    def __init__(self, id_video, playlist_id):
        self.__playlist_id = playlist_id
        super().__init__(id_video)

        
