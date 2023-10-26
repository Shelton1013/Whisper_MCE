from Deal_Dataset import MCE_dataset

audio_folder_path = r'E:\Whisper-base-local\data\MCE Datasets'
text_folder_path = r'E:\Whisper-base-local\data\csv'

MCE_dataset = MCE_dataset(audio_folder_path, text_folder_path)

# check if aduio file num == text num, ensure the data num is correct
MCE_dataset.check_dataset_num(1, 31)
MCE_dataset.check_dataset_num(61, 75)
MCE_dataset.check_dataset_num(86, 160)