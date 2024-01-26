import sys
import os

current_path = os.getcwd()
Audio_file_deal = current_path + r"\Audio_File_Deal"

sys.path.append(Audio_file_deal)

from Deal_Dataset import MCE_dataset
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--audio_folder_path", help="MCE dataset audio files path")
parser.add_argument("--text_folder_path", help="MCE dataset text files path")
args = parser.parse_args()

audio_folder_path = args.audio_folder_path
text_folder_path = args.text_folder_path


MCE_dataset = MCE_dataset(audio_folder_path, text_folder_path)
audio_dict = {}

for i in range(1, 161):
    if i != 85:
        audio_path = audio_folder_path + f"""\\{i}_MCE\\"""
        audio_file = os.listdir(audio_path)
        for audio in audio_file:
            audio_p = audio_path + audio
            audio_length = round(MCE_dataset.get_audio_length(audio_p))
            if audio_length not in audio_dict:
                audio_dict[audio_length] = 0
            audio_dict[audio_length] += 1
        print("audio dictionary:", audio_dict)


audio_length = 0
for i in range(1, 161):
    if i != 85:
        audio_path = audio_folder_path + f"""\\{i}_MCE\\"""
        audio_file = os.listdir(audio_path)
        for audio in audio_file:
            audio_p = audio_path + audio
            audio_length += MCE_dataset.get_audio_length(audio_p)



x = list(audio_dict.keys())
y = list(audio_dict.values())
plt.bar(x, y)
plt.xlabel('Seconds of Audio')
plt.ylabel('Number of Audio')
plt.show()
