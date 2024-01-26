from Deal_Dataset import MCE_dataset
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--audio_folder_path", help="MCE dataset audio files path")
parser.add_argument("--text_folder_path", help="MCE dataset text files path")
args = parser.parse_args()

audio_folder_path = args.audio_folder_path
text_folder_path = args.text_folder_path

MCE_dataset = MCE_dataset(audio_folder_path, text_folder_path)

# check if aduio file num == text num, ensure the MCE num is correct
MCE_dataset.check_dataset_num(1, 85)
MCE_dataset.check_dataset_num(86, 85)
