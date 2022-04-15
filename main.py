# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import moviepy.editor as mp


def print_hi(name):
    clip = mp.VideoFileClip("middle east loop - malfuf 90 bpm.mp4").subclip(0, 20)
    clip.audio.write_audiofile("malfuf90bpm.mp3")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
