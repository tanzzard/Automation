import os
os.startfile('C:\\Users\\TANDIN TSHEWANG\\Music\\Music')
import vlc
import random

MUSIC_FOLDER_PATH = 'C:\\Users\\TANDIN TSHEWANG\\Music\\Music'

music_files = [f for f in os.listdir(MUSIC_FOLDER_PATH)]

if not music_files:
    print("No music files found in the folder.")
else:
    random_song = random.choice(music_files)
    song_path = os.path.join(MUSIC_FOLDER_PATH, random_song)

    player = vlc.MediaPlayer(song_path)

    player.play()

    print(f"Playing: {random_song}")

    input("Press Enter to exit...")

    player.stop()
    player.release()