from pytube import YouTube

url = YouTube("https://www.youtube.com/watch?v=2G4MyJL2Xw8")

mp4_files = url.streams.filter(file_extension="mp4")

mp4_369p_files = mp4_files.get_by_resolution("1080p")

mp4_369p_files.download("D:\Git Github\DownloadYouTubeVideos")
