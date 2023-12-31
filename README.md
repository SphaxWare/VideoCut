# VideoCut

This Python script allows you to trim a video file based on specified start and end timestamps. It uses the `moviepy` library for video editing.
https://github.com/Zulko/moviepy

## Prerequisites

- Python 3.x
- `moviepy` library

You can install the required library using the following command:

```bash
pip install moviepy
```
# Usage
1. Clone the Repository:
````
git clone github.com/SphaxWare/VideoCut/edit.git
cd VideoCut
````
2. Run the Script:

```bash
python vidcut.py
```
3. Follow the Prompts:
```
Enter the path to the input video file.
Enter the start timestamp in the format (hh:mm:ss).
Enter the end timestamp in the format (hh:mm:ss).
Enter the path for the output video file.
Output:

The trimmed video will be saved in the specified output path.
```
# Example
```
Enter the path to the input video file: path/to/input/video.mp4
Enter the start timestamp (hh:mm:ss): 00:00:30
Enter the end timestamp (hh:mm:ss): 00:01:30
Enter the path for the output video file: path/to/output/trimmed_video.mp4
```

for the resizer to work you may need to install an older version of pillow
```
pip install Pillow==9.5.0
```
