import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
print(api_key)
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self._init_from_api()

        # print(self.channel_id)
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

    def print_info(self):
        """"Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_service():
        service = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))
        return service

    def _init_from_api(self) -> None:
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel["items"][0]["id"]}'
        self.subscriber_count = int(channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(channel['items'][0]['statistics']['viewCount'])


