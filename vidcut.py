from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from datetime import datetime

def convert_timestamp_to_seconds(timestamp):
    time_obj = datetime.strptime(timestamp, '%H:%M:%S')
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def trim_video(input_video, start_timestamp, end_timestamp, output_video):
    start_time = convert_timestamp_to_seconds(start_timestamp)
    end_time = convert_timestamp_to_seconds(end_timestamp)

    clip = VideoFileClip(input_video)
    trimmed_clip = clip.subclip(start_time, end_time)

    trimmed_clip.write_videofile(output_video, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    input_video = input("Enter the path to the input video file: ")
    start_timestamp = input("Enter the start timestamp (hh:mm:ss): ")
    end_timestamp = input("Enter the end timestamp (hh:mm:ss): ")
    output_video = input("Enter the path for the output video file: ")

    trim_video(input_video, start_timestamp, end_timestamp, output_video)
