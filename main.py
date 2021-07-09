import file_converter
import youtube_downloader

print('''
What do you want?

(1) Download YouTube Videos
(2) Download YouTube Playlist
(3) Download YouTube Videos Audio Into MP3
(4) Download Youtube Videos Audio Into MP4
(5) Download Youtube Playlist Audio

''')
Destination = youtube_downloader.choose_destination()
choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        youtube_downloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)


elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("Downloading...")
        filename = youtube_downloader.download_audio(link)
        print("Converting...")
        file_converter.convert_to_mp3(f'{Destination}{filename}')


elif choice == "4":
    links = youtube_downloader.input_links()
    for link in links:
        youtube_downloader.download_audio(link)


elif choice == '5':
    link = input('Enter the link to the playlist: ')
    print("Downloading playlist...")
    youtube_downloader.download_playlist_audio(link)
    print('Download finished!')


else:
    print("Invalid input! Terminating...")
