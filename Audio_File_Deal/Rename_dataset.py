from Deal_Dataset import MCE_dataset
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--audio_folder_path", help="MCE dataset audio files path")
parser.add_argument("--text_folder_path", help="MCE dataset text files path")
args = parser.parse_args()

audio_folder_path = args.audio_folder_path
text_folder_path = args.text_folder_path

MCE_dataset = MCE_dataset(audio_folder_path, text_folder_path)


# second, use re to rename audio file
filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(1, 16, filename_pattern)

filename_pattern = r"語音  \((\d+)\)"
MCE_dataset.rename_audio_file(16, 17, filename_pattern)

filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(17, 31, filename_pattern)

filename_pattern = r"魁籹 \((\d+)\)"
MCE_dataset.rename_audio_file(31, 36, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(36, 46, filename_pattern)

filename_pattern = r"Recording\((\d+)\)"
MCE_dataset.rename_audio_file(46, 47, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(47, 50, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(50, 51, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(51, 54, filename_pattern)

filename_pattern = r"(\d+)"
MCE_dataset.rename_audio_file(54, 55, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(55, 57, filename_pattern)

filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(57, 58, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(58, 59, filename_pattern)

filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(59, 60, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(60, 61, filename_pattern)

filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(61, 76, filename_pattern)

filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(76, 80, filename_pattern)

filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(80, 85, filename_pattern)

filename_pattern = r"新錄音 (\d+)"
MCE_dataset.rename_audio_file(86, 101, filename_pattern)

filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(100, 116, filename_pattern)

filename_pattern = r"新錄音 (\d+)"
MCE_dataset.rename_audio_file(116, 130, filename_pattern)

filename_pattern = r"新錄音 (\d+)"
MCE_dataset.rename_audio_file(130, 131, filename_pattern)

filename_pattern = r"录音（(\d+)）"
MCE_dataset.rename_audio_file(131, 133, filename_pattern)

filename_pattern = r"New Recording (\d+)"
MCE_dataset.rename_audio_file(133, 160, filename_pattern)
