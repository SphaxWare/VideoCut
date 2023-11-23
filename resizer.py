from moviepy.editor import VideoFileClip
from datetime import datetime

def convert_timestamp_to_seconds(timestamp):
    time_obj = datetime.strptime(timestamp, '%H:%M:%S')
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def trim_video(input_video, start_timestamp, end_timestamp, output_video):
    start_time = convert_timestamp_to_seconds(start_timestamp)
    end_time = convert_timestamp_to_seconds(end_timestamp)

    clip = VideoFileClip(input_video)
    clip = clip.subclip(start_time, end_time)

    # Resize to 9:16 
    clip = clip.resize((1080, 1920))
    # Set bitrate to 10 mb/s
    clip.write_videofile(output_video, codec="libx264", audio_codec="aac", bitrate="10M")

if __name__ == "__main__":
    input_video = input("Enter the path to the input video file: ")
    start_timestamp = input("Enter the start timestamp (hh:mm:ss): ")
    end_timestamp = input("Enter the end timestamp (hh:mm:ss): ")
    output_video = input("Enter the path for the output video file: ")

    trim_video(input_video, start_timestamp, end_timestamp, output_video)
