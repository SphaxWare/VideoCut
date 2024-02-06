from moviepy.editor import VideoFileClip
from datetime import datetime

def convert_timestamp_to_seconds(timestamp):
    time_obj = datetime.strptime(timestamp, '%H:%M:%S')
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def trim_video(input_video, start_timestamp, end_timestamp, output_video):
    clip = VideoFileClip(input_video)

    if start_timestamp and end_timestamp:
        start_time = convert_timestamp_to_seconds(start_timestamp)
        end_time = convert_timestamp_to_seconds(end_timestamp)
        clip = clip.subclip(start_time, end_time)

    # Resize to 9:16 
    clip = clip.resize((1080, 1920))
    # Set bitrate to 10 mb/s
    clip.write_videofile(output_video, codec="libx264", audio_codec="aac", bitrate="10M")

if __name__ == "__main__":
    input_video = input("Enter the path to the input video file: ")
    start_timestamp = input("Enter the start timestamp (hh:mm:ss, press Enter for full video): ").strip()
    end_timestamp = input("Enter the end timestamp (hh:mm:ss, press Enter for full video): ").strip()
    output_video = input("Enter the path for the output video file: ")

    trim_video(input_video, start_timestamp or None, end_timestamp or None, output_video)
