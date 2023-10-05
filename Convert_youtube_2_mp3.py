#### to run type:
##   python  Convert_youtube_2_mp3.py  <URL from youtube video>
##
### Dont`t forget the $>   pip install pytube moviepy tqdm b


import sys
from pytube import YouTube
from moviepy.editor import VideoFileClip
from tqdm import tqdm

# Check if a YouTube video URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Please provide a valid YouTube video URL as a command-line argument.")
    sys.exit()

# YouTube video URL
video_url = sys.argv[1]

# Download the YouTube video
yt = YouTube(video_url)
video = yt.streams.get_highest_resolution()

# Set up the progress bar
progress_bar = tqdm(total=video.filesize, unit='bytes', unit_scale=True)

# Callback function to update the progress bar
def progress_callback(stream, chunk, file_handle, remaining):
    progress_bar.update(len(chunk))

# Download the video
video.download(filename='temp_video.mp4')

# Convert the video to audio
video_path = 'temp_video.mp4'
audio_path = f"{yt.title}.mp3"

video_clip = VideoFileClip(video_path)
video_clip.audio.write_audiofile(audio_path)

# Print the location of the audio file
print(f"Audio file saved: {audio_path}")

# Close the progress bar
progress_bar.close()
