import os
from datasets import Audio, Dataset
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--audio_folder_path", help="MCE dataset audio files path")
parser.add_argument("--text_folder_path", help="MCE dataset text files path")
args = parser.parse_args()

audio_folder_path = args.audio_folder_path
text_folder_path = args.text_folder_path

start, end = 1, 160

audio_list = []
for i in range(start, end):
    if i != 85:
        audio_path = audio_folder_path + f"""\\{i}_MCE\\"""
        audio_num = len(os.listdir(audio_path))
        for j in range(1, audio_num + 1):
            audio = audio_path + f"""{i}_{j}.wav"""
            audio_list.append(audio)

#print(audio_list)


MCE = []
for i in range(start, end):
    if i != 85:
        csv_path = text_folder_path + f"""\\data_{i}.csv"""
        df = pd.read_csv(csv_path, encoding='GBK')
        label = df["Instance"]
        label = label.values.tolist()
        content = [element.strip('"') for element in label]
        MCE += content

# print(MCE)


MCE_dataset = {"audio": audio_list, "sentence": MCE}
audio_dataset = Dataset.from_dict(MCE_dataset).cast_column("audio", Audio())
print(audio_dataset)
print(audio_dataset[83])

