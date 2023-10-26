from Deal_Dataset import MCE_dataset

audio_folder_path = r'E:\Whisper-base-local\data\MCE Datasets'
text_folder_path = r'E:\Whisper-base-local\data\csv'

MCE_dataset = MCE_dataset(audio_folder_path, text_folder_path)

# second, use re to rename audio file
filename_pattern = r"Recording \((\d+)\)"
MCE_dataset.rename_audio_file(1, 16, filename_pattern)
filename_pattern = r"語音  \((\d+)\)"
MCE_dataset.rename_audio_file(16, 17, filename_pattern)
filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(17, 30, filename_pattern)
filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(61, 76, filename_pattern)
MCE_dataset.filename_pattern = r"新錄音 (\d+)"
MCE_dataset.rename_audio_file(86, 100, filename_pattern)
filename_pattern = r"錄製 \((\d+)\)"
MCE_dataset.rename_audio_file(100, 115, filename_pattern)
filename_pattern = r"新錄音 (\d+)"
MCE_dataset.rename_audio_file(115, 131, filename_pattern)
filename_pattern = r"录音（(\d+)）"
MCE_dataset.rename_audio_file(131, 133, filename_pattern)
filename_pattern = r"New Recording (\d+)"
MCE_dataset.rename_audio_file(133, 160, filename_pattern)
