import os
import sys
from gtts import gTTS

# Check if a PDF file is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 pdf_to_audio.py <PDF_FILE>")
    sys.exit(1)

pdf_file = sys.argv[1]
basename = os.path.basename(pdf_file)
txt_file = f"{os.path.splitext(basename)[0]}.txt"
audio_file = f"{os.path.splitext(basename)[0]}.mp3"

# Step 1: Extract text from the PDF using pdftotext
print(f"Extracting text from {pdf_file}...")
os.system(f"pdftotext {pdf_file} {txt_file}")

# Step 2: Check if the text file was created
if not os.path.exists(txt_file):
    print(f"Failed to extract text from {pdf_file}.")
    sys.exit(1)

# Step 3: Convert the extracted text to audio using gTTS
print(f"Converting text to audio and saving as {audio_file}...")
with open(txt_file, "r") as file:
    text = file.read()
    tts = gTTS(text, lang="en")
    tts.save(audio_file)

# Step 4: Clean up the temporary text file
os.remove(txt_file)

print(f"Audio file saved as {audio_file}")
