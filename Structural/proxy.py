from abc import ABC, abstractmethod


class VideoLibrary(ABC):
    @abstractmethod
    def getVideosList(self): pass

    @abstractmethod
    def getVideoInfo(self, query: str): pass

    @abstractmethod
    def getVideo(self, query: str): pass

    @abstractmethod
    def addVideo(self, new_video: tuple): pass

    @abstractmethod
    def delVideo(self, video_to_del: str): pass


class WebVideoLibrary(VideoLibrary):
    def __init__(self):
        self._videos = {
            'nature': {
                'info': 'Video about nature',
                'link': 'http://web_link_at_video_about_nature'
            },
            'space': {
                'info': 'Video about space',
                'link': 'http://web_link_at_video_about_space'
            },
            'war': {
                'info': 'Video about war',
                'link': 'http://web_link_at_video_about_war'
            },
            'trade': {
                'info': 'Video about trade',
                'link': 'http://web_link_at_video_about_trade'
            },
        }

    def getVideosList(self) -> None:
        print('\nThe library contains such videos as:')
        for video in self._videos: print(video)

    def getVideoInfo(self, query: str) -> None:
        print(f"\nInformation about {query} video:\n{self._videos[query]['info']}")

    def getVideo(self, query: str) -> None:
        print(f'\nDownloading queried video "{query}" by the following link:\n{self._videos[query]["link"]}')

    def addVideo(self, new_video: tuple) -> None:
        video_name, video_data = new_video
        self._videos[video_name] = video_data
        print(f'\nNew video "{new_video}" was added to the library')

    def delVideo(self, video_to_del: str):
        del self._videos[video_to_del]
        print(f'\nVideo "{video_to_del}" was removed from the library')


class WebVideoLibraryProxy(VideoLibrary):
    def __init__(self):
        self._service = WebVideoLibrary()

    def getVideosList(self):
        self._service.getVideosList()

    def getVideoInfo(self, query: str):
        self._service.getVideoInfo(query)

    def getVideo(self, query: str):
        self._service.getVideo(query)

    def addVideo(self, new_video: tuple):
        self._service.addVideo(new_video)

    def delVideo(self, video_to_del: str):
        self._service.delVideo(video_to_del)


if __name__ == '__main__':
    def client_code(video_lib: VideoLibrary):
        video_lib.getVideosList()

        video_lib.getVideo('trade')

        video_lib.addVideo(('coding', {'info': 'Video about coding', 'link': 'http://web_link_at_video_about_coding'}))
        video_lib.getVideoInfo('coding')

        video_lib.delVideo('trade')
        video_lib.getVideosList()


    client_code(WebVideoLibraryProxy())
