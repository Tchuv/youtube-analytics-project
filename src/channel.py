import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
print(api_key)
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
        self._init_from_api()

        # print(self.channel_id)
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

    def print_info(self):
        """"Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id



    def get_service(self):
        service = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))
        return service

    def _init_from_api(self) -> None:
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel["items"][0]["id"]}'
        self.subscriber_count = int(channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(channel['items'][0]['statistics']['viewCount'])

    def to_json(self, filename: str) -> None:
            dict_to_write = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count,
        }
            with open(filename, 'w') as fp:
                json.dump(dict_to_write, fp)

    def __str__(self):
        return f"{self.title} {self.url}"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

