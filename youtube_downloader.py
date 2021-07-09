import os
import pytube
import file_converter

fln = ''  # file name to be used while converting to MP3
Destination = 'Downloads'  # Download Destination by Default


def download_video(url, resolution):
    print('Fetching file ...')
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    global fln
    fln = stream.default_filename
    try:
        print(f'Downloading: {fln}')
        stream.download(f'{Destination}')
    except Exception as ex:
        print(f'{resolution} error {ex}, trying with low resolution ...')
        stream = video.streams.get_by_itag(18)
        stream.download(f'{Destination}')
    return stream.default_filename


def download_audio(url):
    audio = pytube.YouTube(url)
    stream = audio.streams.get_audio_only()
    stream.download(f'{Destination}')
    global fln
    fln = stream.default_filename
    return stream.default_filename


def download_videos(urls, resolution):
    x = 0
    for url in urls:
        x += 1
        try:
            print(f'nb : {x}')
            download_video(url, resolution)
        except Exception as ex:
            print(f'Skipping ... error {ex}')
            pass


def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)


def download_videos_audio(urls):
    x = 0
    for url in urls:
        x += 1
        try:
            print(f'Downloading nb: {x}')
            download_audio(url)
            print('Converting...')
            file_converter.convert_to_mp3(f'{Destination}{fln}')
        except Exception as ex:
            print(f'Skipping ... error {ex}')
            pass


def download_playlist_audio(url):
    playlist = pytube.Playlist(url)
    download_videos_audio(playlist.video_urls)


def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links


def choose_destination():
    dest = input('Choose Destination: ')
    global Destination

    if dest:
        Destination = dest.replace(os.sep, '/')
        print(Destination)
    else:
        Destination = Destination + '/'
        print(f'Choosing Default location {Destination}')

    return Destination + '/'
