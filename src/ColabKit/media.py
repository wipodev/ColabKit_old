from .template import VIDEO_SHOW, AUDIO_SHOW
from .utils import file_exists, remove_file
from IPython.display import display, HTML
from moviepy.editor import VideoFileClip
from base64 import b64encode
import ffmpeg

def showMedia(file_path, media) -> None:
    """
    Display media file on Jupyter Notebook.
    Args:
        file_path (str): The path to the media file.
        media (str): The type of media file ('video' or 'audio').
    Returns:
        None
    """
    # Check if the file exists
    if file_exists(file_path):
        # Set the content type and media type based on the media type
        content_type = 'video/mp4' if media == "video" else 'audio/wav'
        media_type = VIDEO_SHOW if media == "video" else AUDIO_SHOW        
        # Read the file data and encode it as base64
        data = open(file_path, 'rb').read()
        data_url = f"data:{content_type};base64," + b64encode(data).decode()        
        # Display the media file
        display(HTML(media_type % data_url))
    else:
        # Print an error message if the file does not exist
        print(f"\033[43m\033[101mThe {media} file {file_path} is not found in the directory.\033[0m")

def video_duration(video_path) -> float:
    """
    Returns the duration of a video.
    :Args:
        video_path (str) The path to the video file.
    :return: 
        (float) The duration of the video in seconds.
    """
    return VideoFileClip(video_path).duration


def get_video_resolution(video_path) -> tuple:
    """
    Get the resolution of a video file.    
    Args:
        video_path (str): The path to the video file.    
    Returns:
        tuple: A tuple containing the width and height of the video.
    """
    video = VideoFileClip(video_path)
    return (video.size[0], video.size[1])


def ffmpeg_err(stderr) -> str:
    """
    Extracts and formats error lines from the stderr output of the ffmpeg command.
    Args:
        stderr (bytes): The stderr output of the ffmpeg command.
    Returns:
        str: A formatted string containing the error lines.
    """
    # Convert the stderr output to a string and split it into lines
    lines = stderr.decode('utf-8').splitlines()
    # Filter out the lines that start with "Error"
    error_lines = [line for line in lines if line.startswith("Error")]
    # Format the error lines and return them
    for error_line in error_lines:
        return f"\033[43m\033[101m{error_line}\033[0m"


def ffmpeg_proc(output_stream, output_file, msg) -> bool:
    """
    Run FFmpeg with the specified output stream and file.
    Parameters:
    output_stream (str): The output stream to be processed by FFmpeg.
    output_file (str): The file path where the output will be saved.
    msg (str): A message to be displayed in the console.
    Returns:
    bool: True if FFmpeg ran successfully, False otherwise.
    """
    try:
        # Run FFmpeg with the specified output stream and options
        ffmpeg.run(output_stream, capture_stderr=True, overwrite_output=True)        
        # Print the success message
        print(f'File {msg} and saved as {output_file}')        
        # Return True to indicate success
        return True
    except ffmpeg.Error as e:
        # Print the FFmpeg error message
        print(ffmpeg_err(e.stderr))        
        # Remove the output file if an error occurs
        remove_file(output_file)        
        # Return False to indicate failure
        return False

def ffmpeg_conv(input_file: str, output_file: str) -> bool:
    """
    Convert a video file from one format to another using FFmpeg.
    Args:
        input_file: The path to the input video file.
        output_file: The path to save the converted video file.
    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    # Print the conversion message
    print(f"Converting {input_file} to {output_file}...")
    # Create the input stream
    input_stream = ffmpeg.input(input_file)
    # Create the output stream
    output_stream = ffmpeg.output(input_stream, output_file)
    # Execute the FFmpeg process and return the output
    return ffmpeg_proc(output_stream, output_file, "converted")


def ffmpeg_trim(input_file, start, interval, output_file) -> str:
    """
    Trims a video file using FFmpeg.
    Args:
        input_file (str): The path to the input video file.
        start (int): The starting point in seconds.
        interval (int): The duration in seconds to trim.
        output_file (str): The path to the output trimmed video file.
    Returns:
        str: The path to the trimmed video file.
    """
    # Print the progress
    print(f"Trimming {input_file} to {interval} seconds...")
    # Create the input stream
    input_stream = ffmpeg.input(input_file, ss=start)
    # Create the output stream
    output_stream = ffmpeg.output(input_stream, output_file, t=interval)
    # Run FFmpeg to trim the video
    return ffmpeg_proc(output_stream, output_file, "trimmed")


def resize_video(video_path: str, new_resolution: int):
    """
    Resize a video to a new resolution.
    Args:
        video_path (str): The path to the video file.
        new_resolution (int): The new resolution height in pixels.
    Returns:
        (str, bool): The path to the resized video file if successful, otherwise False.
    """
    # Generate the new path for the resized video
    new_path = f"{video_path.split('.')[0]}_{new_resolution}p.mp4"
    # Get the current resolution of the video
    video_resolution = get_video_resolution(video_path)
    print(f"Video resolution: {video_resolution}")
    if video_resolution[0] >= 1920 or video_resolution[1] >= 1080:
        # Resize the video to the new resolution
        print(f"Resizing video to {new_resolution}p...")
        new_width = 2 * int((video_resolution[0] / video_resolution[1] * new_resolution / 2))
        input_stream = ffmpeg.input(video_path)
        output_stream = ffmpeg.output(
            input_stream, new_path, vf=f'scale={new_width}:{new_resolution}', vcodec='libx264')
        # Check if the resizing was successful
        return new_path if ffmpeg_proc(output_stream, new_path, "resized") else False
    else:
        print("No need to change the size")
        return video_path
