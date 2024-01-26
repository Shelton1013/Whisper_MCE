from Deal_Dataset import MCE_dataset
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--audio_folder_path", help="MCE dataset audio files path")
parser.add_argument("--text_folder_path", help="MCE dataset text files path")
args = parser.parse_args()

audio_folder_path = args.audio_folder_path
text_folder_path = args.text_folder_path


MCE_dataset = MCE_dataset(audio_folder_path, text_folder_path)


# unified dataset format
# First, audio type wav, sample rate 16,000 hz
for i in range(130, 131):
    audio_folder_name = audio_folder_path + f"""\{i}\\"""
    new_path = audio_folder_path + f"""\{i}_deal\\"""
    aduio_file_list = os.listdir(audio_folder_name)
    for audio in aduio_file_list:
        sample_rate = MCE_dataset.get_sample_rate(audio_folder_name, audio)
        print(f"Origin audio sample rate: {sample_rate} Hz")
        MCE_dataset.adjust_sample_rate(audio_folder_name, new_path, audio, 16000)


# Second change to mono
for i in range(130, 131):
    input_file_folder = audio_folder_path + f"""\\{i}_deal\\"""
    audio_file_list = os.listdir(input_file_folder)
    for audio in audio_file_list:
        input_file = input_file_folder + audio
        output_file = audio_folder_path + f"""\\{i}_MCE\\""" + audio
        output_folder = os.path.dirname(output_file)
        if not os.path.exists(audio_folder_path + f"""\\{i}_MCE\\"""):
            os.makedirs(output_folder)
        MCE_dataset.convert_to_mono(input_file, output_file)