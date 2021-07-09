from moviepy.editor import AudioFileClip
import os


def convert_to_mp3(filename):
    audioclip = AudioFileClip(filename)
    audioclip.write_audiofile(filename[:-4] + ".mp3")
    audioclip.close()
    os.remove(filename)
