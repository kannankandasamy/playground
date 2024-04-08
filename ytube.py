from pytube.cli import on_progress
from pytube import YouTube
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def download_the_video(link, target_folder=None, time_ranges=None):
    yt = YouTube(link)
    video_stream = yt.streams.get_highest_resolution()
    video_path = video_stream.download(output_path=target_folder)
    video_filename = os.path.basename(video_path)

    if time_ranges is not None:
        index = 1
        for start_time, end_time in time_ranges:
            start_time = parse_time(start_time)
            end_time = parse_time(end_time)
            clip_filename = f"{os.path.splitext(video_filename)[0]}_clip{index}.mp4"
            clip_path = os.path.join(target_folder, clip_filename)
            ffmpeg_extract_subclip(
                video_path, start_time, end_time, targetname=clip_path
            )
            print(f"Video clip saved: {clip_path}")
            index += 1
        os.remove(video_path)
    else:
        print(
            "Please provide time_ranges to specify the start_time and end_time for cutting the video clip."
        )


def parse_time(time_str):
    h, m, s = time_str.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


links = ["https://www.youtube.com/watch?v=2QXnPPXWM-o"]
time_ranges = [("00:00:58", "00:01:02")]
target_folder = r"c:\test\mov"  # Replace with the desired target folder path

if __name__ == "__main__":
    for link in links:
        download_the_video(link, target_folder, time_ranges=time_ranges)