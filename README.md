# Whisper-MCE
[Whisper-MCE](https://drive.google.com/file/d/14_IFvi0z8zHNJGYetpW5GHxbS0z6p0dt/view?usp=sharing)</br>
Use our fine-tuned Whisper-MCE for speech recognition
```bash
python Whisper_mce.py --model_path "your model path" --audio_path "your test audio path"
```


## MCE Dataset
[MCE Dataset](https://drive.google.com/file/d/1CFgHxTzYBKnIkRVBdCwlJXahZq3Zi87B/view?usp=sharing)</br>
MCE Dataset folder has two folders:</br>
- Audio: mixed Cantonese and English audio files, 160 audio folders</br>
1-160 is the original audio data</br>
1_deal-160_deal is the cleaned original audio data</br>
1_MCE-160_MCE is the training format audio data</br>
we provided the training format audio data </br>

- Text: mixed Cantonese and English text (Generated by GPT4) files, 160 CSV files</br>
format(topic, text content)</br>

The MCE Dataset is collected by 10 students from HKUST, **each students have their own name rule and their audio files have different formats.**



## Data Cleaning
- step 1: Check the audio file nums(Check_OriginData_num.py)
- setp 2: Prepare for audio file rename(Data_Dislocation.py)
- step 3: Rename the audio file(Rename_dataset.py)
- step 4: Unite the audio format(Unified_dataset_format.py)

### `Check OriginData_num.py`
Check if audio file numbers are equal to text file row numbers to ensure the data number is correct

---

### `Data_Dislocation.py`
Handle dislocation for the audio file folder

---

### `Rename_dataset.py`
Rename the audio file to have a unified name rule

---


### `Unified_dataset_format.py`
Unite the audio type(.wav), sample rate(16,000hz), number of channels(mono)

---

## MCE Text Generation
### `First_Data_Generate.py`
Generate Original Data(topic_dict) which needs to be handwritten

---

### `Data_Generate_plus.py`
Sample new data from the generated CSV file as the new instance of the topic_dict

---


## Data Analysis
### `Audio_Data_info.py`
Analyze the MCE dataset audio file distribution (audio length)
```bash
python Audio_Data_info.py --audio_folder_path "your path" --text_folder_path "your path"
```

### `Text_Data_info.py`
Analyze the MCE dataset text file distribution (English word and Traditional Chinese Character numbers)
```bash
python Text_Data_info.py --text_folder_path "your path"
```

## Load MCE Dataset
Load MCE Dataset

```bash
python Load_MCE.py --audio_folder_path "your path" --text_folder_path "your path"
```

## Model Fine-tune
For model fine-tuning, we use A100(80G) GPUs rented from the Runpod platform.

## Environment
```bash
pip install -r requirements.txt
```

## Upload File
https://github.com/runpod/runpodctl

```bash
wget --quiet --show-progress https://github.com/Run-Pod/runpodctl/releases/download/v1.10.0/runpodctl-linux-amd -O runpodctl && chmod +x runpodctl && sudo cp runpodctl /usr/bin/runpodctl
```

Windows send file
```bash
.\runpodctl send data.txt
```

Linux receive file
```bash
runpodctl receive <code from windows>
```

Unzip
```bash
apt-get install zip -y
zip -FF Finetune.zip --out ft.zip -fz -y
unzip ft.zip
```

