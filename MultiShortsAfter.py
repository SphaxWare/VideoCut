"""This script take all the videos details then process them all at once"""
from moviepy.editor import VideoFileClip
from datetime import datetime
import os

def convert_timestamp_to_seconds(timestamp):
    time_obj = datetime.strptime(timestamp, '%H:%M:%S')
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def trim_video(input_video, start_timestamp, end_timestamp, output_video):
    clip = VideoFileClip(input_video)

    if start_timestamp is not None:
        start_time = convert_timestamp_to_seconds(start_timestamp)
    else:
        start_time = 0

    if end_timestamp is not None:
        end_time = convert_timestamp_to_seconds(end_timestamp)
    else:
        end_time = clip.duration

    clip = clip.subclip(start_time, end_time)

    # Crop to 9:16 aspect ratio
    cropped_clip = clip.crop(x1=(clip.w - clip.h * 9 / 16) / 2,
                             x2=clip.w - (clip.w - clip.h * 9 / 16) / 2,
                             y1=0, y2=clip.h)

    # Set bitrate to 10 mb/s
    cropped_clip.write_videofile(output_video, codec="libx264", audio_codec="aac", bitrate="10M")

if __name__ == "__main__":
    input_videos = input("Enter the paths to the input video files (separated by comma): ").split(',')
    input_videos = [video.strip().replace('"', '') for video in input_videos]

    video_details = []

    for input_video in input_videos:
        start_timestamp = input("Enter the start timestamp (hh:mm:ss): ")
        end_timestamp = input("Enter the end timestamp (hh:mm:ss, press Enter for full video): ")
        output_video = input(f"Enter the path for the output video file for {os.path.basename(input_video)}: ") + ".mp4"

        video_details.append((input_video, start_timestamp or None, end_timestamp or None, output_video))

    # Process all videos
    for details in video_details:
        input_video, start_timestamp, end_timestamp, output_video = details
        trim_video(input_video, start_timestamp, end_timestamp, output_video)
