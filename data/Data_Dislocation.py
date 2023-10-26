from Deal_Dataset import MCE_dataset

audio_folder_path = r'E:\Whisper-base-local\data\MCE Datasets'
text_folder_path = r'E:\Whisper-base-local\data\csv'

MCE_dataset = MCE_dataset(audio_folder_path, text_folder_path)

# 10 people collect this dataset where each people have their own name rule
# handle dislocation for folder_117-130, just change the start num
audio_folder_path_d = audio_folder_path + r"\117"
filename_pattern = r"新錄音 (\d+)"
start = 85
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\118"
start = 165
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\119"
start = 242
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\120"
start = 326
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\121"
start = 402
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\123"
start = 482
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\124"
start = 566
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\125"
start = 642
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\126"
start = 723
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\127"
start = 803
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\128"
start = 882
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\129"
start = 968
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)
audio_folder_path_d = audio_folder_path + r"\130"
start = 1048
MCE_dataset.audio_dislocation(audio_folder_path_d, filename_pattern, start)



