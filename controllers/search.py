from pytube import Playlist
from pytube import YouTube
import threading

class Search():
    def __init__(self,InputVal):
        super().__init__()
        self.input=InputVal
        self.previousprogress = 0

    @staticmethod
    def Test(InputVal):
        print(InputVal.get())
    
    def Download(self):
        print('started')
        url=self.input.get()
        yt = YouTube(url)
        yt.register_on_progress_callback(self.on_progress)
        yt.streams.filter(only_audio=True).first().download()

    def on_progress(self,stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining 

        liveprogress = (int)(bytes_downloaded / total_size * 100)
        if liveprogress > self.previousprogress:
            self.previousprogress = liveprogress
            print(liveprogress)