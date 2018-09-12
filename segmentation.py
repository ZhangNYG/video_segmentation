import cmd
import subprocess
import sys

ffmpegPath = "E:\\ffmpeg-4.0-win64-static\\bin\\ffmpeg.exe"
CurMediaPath = "E:\\voley_video\\00051.mp4"
videoStartTime = "00:10:00.0"
videoEndTime = "00:00:02.0"
videoSaveDir = "E:\\voley_video\\save\\save.mp4"
md = ffmpegPath + ' -y -i ' + CurMediaPath + ' -ss ' + videoStartTime + ' -t ' + videoEndTime +\
	' -acodec copy -vcodec copy -async 1 ' + videoSaveDir
subprocess.call(md)
