from pytube import YouTube


def downloadYTvideos(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_highest_resolution().download(outpath)


if __name__ == "__main__":

    downloadYTvideos(
        "https://www.youtube.com/watch?v=2G4MyJL2Xw8",
        "./downloaded",
    )