from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient


client2 = VideoClient('127.0.0.1', 9999, '2.mov.mp4')
client2.start_stream()
