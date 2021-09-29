from abc import ABC, abstractmethod


class VideoLibrary(ABC):
    @abstractmethod
    def getVideosList(self) -> None: pass

    @abstractmethod
    def getVideoInfo(self, query: str) -> None: pass

    @abstractmethod
    def getVideo(self, query: str) -> str: pass

    @abstractmethod
    def addVideo(self, new_video: tuple): pass

    @abstractmethod
    def delVideo(self, video_to_del: str): pass


# Service
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
        print(f'\nInformation about "{query}" video:\n{self._videos[query]["info"]}')

    def getVideo(self, query: str) -> str:
        print(f'\nDownloading queried video "{query}" by the following link:\n{self._videos[query]["link"]}')
        return f'"{query}" video'

    def addVideo(self, new_video: tuple) -> None:
        video_name, video_data = new_video
        self._videos[video_name] = video_data
        print(f'\nNew video "{new_video}" was added to the library')

    def delVideo(self, video_to_del: str) -> None:
        del self._videos[video_to_del]
        print(f'\nVideo "{video_to_del}" was removed from the library')


# Proxies
class WebVideoLibraryCacheProxy(VideoLibrary):
    def __init__(self):
        self._service = WebVideoLibrary()
        self._videos_cache = {}

    def getVideosList(self) -> None:
        self._service.getVideosList()

    def getVideoInfo(self, query: str) -> None:
        self._service.getVideoInfo(query)

    def getVideo(self, query: str) -> None:
        if query not in self._videos_cache:
            self._videos_cache[query] = self._service.getVideo(query)
        else:
            print(f'\nGetting cached {self._videos_cache[query]}')

    def addVideo(self, new_video: tuple) -> None:
        self._service.addVideo(new_video)

    def delVideo(self, video_to_del: str) -> None:
        if video_to_del in self._videos_cache:
            del self._videos_cache[video_to_del]
        self._service.delVideo(video_to_del)


# WebVideoLibrarySecurityProxy methods decorator
def checkAccess(method):
    def wrapper(self, *args):
        if self.access: method(self, *args)
        else:
            print(self._accessDenied)
    return wrapper


class WebVideoLibrarySecurityProxy(VideoLibrary):
    def __init__(self):
        self._service = WebVideoLibraryCacheProxy()
        # self._service = WebVideoLibrary()
        self._validTokens = ['sk552sr', 'lp476mu', 'zx557jh']
        self._access = False
        self._accessDenied = 'Access denied. Please, make sure you have permission'

    @property
    def access(self) -> bool:
        return self._access

    @access.setter
    def access(self, user_token: str) -> None:
        if user_token in self._validTokens:
            self._access = True

    @checkAccess
    def getVideosList(self) -> None:
        self._service.getVideosList()

    @checkAccess
    def getVideoInfo(self, query: str) -> None:
        self._service.getVideoInfo(query)

    @checkAccess
    def getVideo(self, query: str) -> None:
        self._service.getVideo(query)

    @checkAccess
    def addVideo(self, new_video: tuple) -> None:
        self._service.addVideo(new_video)

    @checkAccess
    def delVideo(self, video_to_del: str) -> None:
        self._service.delVideo(video_to_del)


# Client code
if __name__ == '__main__':
    def client_code(video_lib: VideoLibrary):
        video_lib.access = 'lp476mu'
        # video_lib.access = 'ld772uo'

        video_lib.getVideosList()
        video_lib.getVideo('trade')

        video_lib.addVideo(('coding', {'info': 'Video about coding', 'link': 'http://web_link_at_video_about_coding'}))
        video_lib.getVideoInfo('coding')

        video_lib.getVideo('trade')
        video_lib.delVideo('war')

        video_lib.getVideosList()


    # client_code(WebVideoLibraryCacheProxy())
    client_code(WebVideoLibrarySecurityProxy())
