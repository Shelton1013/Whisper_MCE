import os
import pandas as pd
import re
from pydub import AudioSegment


"""
1. Check the num of audio and csv files
2. unify the dataset format
"""

class MCE_dataset():
    def __init__(self, audio_folder_path, text_folder_path):
        self.audio_folder_path = audio_folder_path
        self.text_folder_path = text_folder_path


    def check_dataset_num(self, start, end):
        """
        check if aduio file num == text num, ensure the MCE num is correct
        :param start: start folder location
        :param end: end folder location
        :return:
        """
        for i in range(start, end):
            audio_folder_name = self.audio_folder_path + f"""\{i}"""
            audio_file_list = os.listdir(audio_folder_name)
            audio_file_num = len(audio_file_list)
            text_folder_name = self.text_folder_path + f"""\data_{i}.csv"""
            df = pd.read_csv(text_folder_name, encoding='GBK')
            row_count = len(df)
            if audio_file_num != row_count:
                print("Folder{}:".format(i), "Audio file num:{}".format(audio_file_num), "Text num:{}".format(row_count),
                      "Correct:{}".format(audio_file_num==row_count))
            else:
                print("Folder{}:".format(i), "Audio file num:{}".format(audio_file_num), "Text num:{}".format(row_count),
                      "Correct:{}".format(audio_file_num == row_count))


    def audio_dislocation(self, filename_pattern, start):
        """
        some audio file name dislocation
        :param filename_pattern: use pattern to get the audio order
        :param start: move file position forward
        :return:
        """
        audio_file_list = os.listdir(self.audio_folder_path)
        for old_filename in audio_file_list:
            pattern = filename_pattern
            match = re.search(pattern, old_filename)
            if match:
                # rename the audio file
                number = match.group(1)
                new_file_name = f"""新錄音 """ + str(int(number)-start)
                old_filename = self.audio_folder_path + r"\\" + old_filename
                new_file_name = self.audio_folder_path + r"\\" + new_file_name + ".m4a"
                print(new_file_name)
                os.rename(old_filename, new_file_name)


    def rename_audio_file(self, start, end, filename_pattern):
        '''
        each folder has their own naming rules, change the audio file name
        :param start: start folder location
        :param end: end folder location
        :param filename_pattern: use pattern to get the audio information
        :return:
        '''
        for i in range(start, end):
            # string like "Recoding(number)"
            audio_folder_name = self.audio_folder_path + f"""\{i}"""
            aduio_file_list = os.listdir(audio_folder_name)
            for old_filename in aduio_file_list:
                pattern = filename_pattern
                match = re.search(pattern, old_filename)
                if match:
                    # rename the audio file
                    number = match.group(1)
                    new_file_name = f"""{i}_""" + str(number)
                    old_filename = audio_folder_name + r"\\" + old_filename
                    new_file_name = audio_folder_name + r"\\" + new_file_name + ".m4a"
                    print(new_file_name)
                    os.rename(old_filename, new_file_name)
                else:
                    # for some audio folder, like 61-75 filename is start from none 1, is not a standard form
                    new_file_name = f"""{i}_""" + "1"
                    old_filename = audio_folder_name + r"\\" + old_filename
                    new_file_name = audio_folder_name + r"\\" + new_file_name + ".m4a"
                    print(new_file_name)
                    os.rename(old_filename, new_file_name)


    def get_sample_rate(self, path, audio_file):
        audio_file = path + r"\\" + audio_file
        audio = AudioSegment.from_file(audio_file)
        sample_rate = audio.frame_rate
        return sample_rate


    def is_mono(self, audio_file):
        # audio = AudioSegment.from_file(audio_file, format="wav")
        audio = AudioSegment.from_file(audio_file, format="m4a")
        channels = audio.channels
        # justify if it is signal channel
        if channels == 1:
            return True
        else:
            return False


    def convert_to_mono(self, input_file, output_file):
        audio = AudioSegment.from_file(input_file, format="wav")
        mono_audio = audio.set_channels(1)
        mono_audio.export(output_file, format="wav")


    def adjust_sample_rate(self, path, new_path, audio_file, target_sample_rate):
        origin_audio_file = path + audio_file

        # change audio type from m4a to wav
        audio = AudioSegment.from_file(origin_audio_file, format="m4a")

        new_audio_file = new_path + audio_file[: -4] + ".wav"
        output_folder = os.path.dirname(new_audio_file)
        if not os.path.exists(new_path):
            os.makedirs(output_folder)
        audio.export(new_audio_file, format="wav")

        # resample sample rate to 16,000Hz
        audio = AudioSegment.from_file(new_audio_file, format="wav")
        audio = audio.set_frame_rate(target_sample_rate)
        audio.export(new_audio_file, format="wav")
        print(f"Save the changed sample rate aduio file: {new_audio_file}")
        audio = AudioSegment.from_file(new_audio_file)
        sample_rate = audio.frame_rate
        print(f"Current sample rate: {sample_rate} Hz")


    def get_audio_length(self, file_path):
        """
        count the audio length
        :param file_path: audio file path
        :return: audio length
        """
        audio = AudioSegment.from_file(file_path)
        duration_in_sec = len(audio) / 1000
        return duration_in_sec

