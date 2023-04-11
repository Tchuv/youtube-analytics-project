import json
import os
import isodate

from dotenv import load_dotenv
from googleapiclient.discovery import build

from setting import ENV_FILE

load_dotenv(ENV_FILE)

# youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:

    __api_key = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)
    def __init__(self, channel_id):
        self.__channel_id = channel_id
        # self.__api_key = os.getenv('API_KEY')
        # self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)
        self.__channel = __youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.__title = self.__channel['items'][0]['snippet']['title']
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__url = f'https://www.youtube/channel/{self.__channel_id}'
        self.subscribers_count = int(self.__channel['items'][0]['snippet']['subscriberCount'])
        self.__video_count = int(self.__channel['items'][0]['snippet']['videoCount'])
        self.__views_count = int(self.__channel['items'][0]['snippet']['viewCount'])

    def print_info(self) -> None:
        channel = self.__youtube.channels().list(id=self.__chanel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) ->str:
        return self.__description

    @property
    def url(self) -> str:
        return self.__url

    @property
    def subscribers_count(self) -> int:
        return self.__subscribers_count

    @property
    def video_count(self) -> int:
        return self.__video_count

    @property
    def views_count(self) -> int:
        return self.__views_count

    @property
    def channel_id(self) -> str:
        return self.__chanel_id

    @channel_id.setter
    def channel_id(self, id):
        print("AttributeError: property 'chdnel_id' of 'Channel' object has no setter")

    @classmethod
    def get_service(cls):
        return cls.__youtube

    def to_json(self, filename) -> None:
        data = {
            'channel_id': self.__chanel_id,
            'title': self.__title,
            'description': self.__description,
            'url': self.__url,
            'subscribers_count': self.__subscribers_count,
            'video_count': self.__video_count,
            'views_count': self.__views_count
        }
        with open(filename, 'w') as file:
            json.dumps(data, file, indent=4)

    def __str__(self) -> str:
        return f'{self.__title} ({self.__url}'


    def __add__(self, other) -> int:
        """ Возможность складывать"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other) ->int:
        """Возможность вычитать"""
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other) -> bool:
        """Возможность строго сравнивать"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other) -> bool:
        """ Возможность не строго сравнивать"""
        return self.subscriber_count >= other.subscriber_count











