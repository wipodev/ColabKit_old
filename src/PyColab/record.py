from .template import AUDIO_RECORD, SAVED_AUDIO_RECORDING
from scipy.io.wavfile import read as wav_read, write as wav_write
from IPython.display import HTML, display
if 'google.colab' in globals():
    from google.colab.output import eval_js
from .utils import wait_for_file
from base64 import b64decode
import ffmpeg
import io


def get_audio() -> tuple:
    """
    Get audio from user input through the browser.    
    Returns:
        audio (ndarray): Numpy array containing the audio data.
        sr (int): Sample rate of the audio data.
    """
    # Display the audio recording widget in the browser
    display(HTML(AUDIO_RECORD))    
    # Get the audio data from the browser
    data = eval_js("data")
    binary = b64decode(data.split(',')[1])    
    # Convert the binary audio data to a WAV file
    process = (
        ffmpeg
        .input('pipe:0')
        .output('pipe:1', format='wav')
        .run_async(
            pipe_stdin=True,
            pipe_stdout=True,
            pipe_stderr=True,
            quiet=True,
            overwrite_output=True
        )
    )
    output, err = process.communicate(input=binary)    
    # Calculate the size of the RIFF chunk
    riff_chunk_size = len(output) - 8
    q = riff_chunk_size
    b = []
    for i in range(4):
        q, r = divmod(q, 256)
        b.append(r)    
    # Replace the RIFF chunk size in the output
    riff = output[:4] + bytes(b) + output[8:]    
    # Read the WAV file and return the audio data and sample rate
    sr, audio = wav_read(io.BytesIO(riff))
    return audio, sr

def record(file_audio = "record.wav") -> None:
    """
    Records audio using the get_audio function and saves it as a WAV file.
    Waits for the file to be saved and displays a message if successful.
    Args:
        file_audio (str): The name of the WAV file to be saved.
    Returns:
        None
    """
    # Get the audio data and the sample rate
    audio, sr = get_audio()
    # Save the audio as a WAV file
    wav_write(file_audio, sr, audio)
    # Wait for the file to be saved
    if wait_for_file(file_audio):
        # Display a message indicating the audio recording was saved
        display(HTML(SAVED_AUDIO_RECORDING))
