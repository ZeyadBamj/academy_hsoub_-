from abc import ABC, abstractmethod

class ThirdPartYouTubeLib(ABC):
    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video_info(self, id):
        pass

    @abstractmethod
    def download_video(self, id):
        pass

class YouTubeClass(ThirdPartYouTubeLib):
    def list_videos(self):
        print("Send API Request")
        return "Videos Listed"

    def get_video_info(self, id):
        print("Get Data About Video which id is:", id)
        return id

    def download_video(self, id):
        print("Download a Video", id)
        return id


class CachedYouTubeClass(ThirdPartYouTubeLib):
    def __init__(self, service: YouTubeClass):
        self.__service = service
        self.__list_cache = None
        self.__video_cache = None


    def list_videos(self):
        if self.__list_cache == None:
            self.__list_cache = self.__service.list_videos()
        return self.__list_cache

    def get_video_info(self, id):
        if self.__video_cache == None:
            self.__video_cache = self.__service.get_video_info(id)
        return self.__video_cache

    def download_video(self, id):
        if not self.download_exists(id):
            self.__service.download_video(id)


    def download_exists(self, id):
        print("Downloading....")
        return True


class YouTubeManager:
    def __init__(self, service: ThirdPartYouTubeLib):
        self._service = service

    def render_video_page(self, id):
        info = self._service.get_video_info(id)

    def render_list_panel(self):
        list = self._service.list_videos()

    def react_on_user_input(self):
        self.render_video_page(1)
        self.render_list_panel()


class Application:
    @staticmethod
    def init():
        aYouTubeService = YouTubeClass()
        aYouTubeProxy = CachedYouTubeClass(aYouTubeService)
        manager = YouTubeManager(aYouTubeProxy)
        manager.react_on_user_input()


if __name__ == "__main__":
    Application.init()