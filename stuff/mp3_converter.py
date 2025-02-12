from pydub import AudioSegment

# Load the audio file (replace 'input_file.wav' with your file name)
input_file = "test1.wav"
audio = AudioSegment.from_wav(input_file)

# Convert to MP3 format (replace 'output_file.mp3' with desired output file name)
output_file = "output_file.mp3"
audio.export(output_file, format="mp3")

print(f"Conversion complete: {output_file}")
