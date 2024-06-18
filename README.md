# MCE and Whipser_MCE
Recently Whisper has approached human-level robustness and accuracy in English speech recognition, while in minor language and mixed language speech recognition, there remains a compelling need for further improvement. In this work, we present the impressive results of **Whisper-MCE**, our fine-tuned Whisper, which was trained using our self-collected dataset, Mixed Cantonese and English **(MCE)** audio dataset, which is generated by our **Multi-Agent Data Generation Framework(MADGF)**. Whisper-MCE achieved an impressive Mix Error Rate (MER) of **14.28%**, which is **35.13%** lower than the original model. It also achieved **12.61%** Character Error Rate (CER) in Common voice zh-HK, positioning it as state-of-the-art.

The MCE dataset covers 18 topics related to daily life, comprising a total of 34.8 hours of audio files. The corresponding annotated text consists of 307,540 Chinese characters and 70,132 English words. Among the topics, the "Food" category has the highest frequency of English words, with a Chinese character to English word ratio of approximately 3:1. On the other hand, the "Tech News" topic has the lowest frequency of English words, approximately 8:1. We randomly sampled all audio files and divided them into training and testing sets in a 9:1 ratio. The resulting training set contains 31.3 hours of speech files, and the distribution of topics in the training and testing sets is relatively consistent. Most audio files contain only one segment of speech. The duration of audio files is concentrated in the 5-12 seconds range, with the longest audio file being 28 seconds. In most large-scale speech recognition models, there is no need for additional audio segmentation processing. During audio recording, all volunteers replicated their habitual speaking speed, intonation, and other speaking habits from daily life. Volunteers with both fast and slow speech rates were selected, with faster speech rates potentially presenting more challenges for accurate recognition due to increased assimilation or pronunciation inaccuracies.

You can download the [MCE Dataset from the Google cloud](https://drive.google.com/file/d/1CFgHxTzYBKnIkRVBdCwlJXahZq3Zi87B/view?usp=sharing).

Our fine-tuned [Whisper-MCE](https://drive.google.com/file/d/14_IFvi0z8zHNJGYetpW5GHxbS0z6p0dt/view?usp=sharing)</br>

Baseline: [Whisper](https://github.com/openai/whisper)

Use our fine-tuned Whisper-MCE for speech recognition
```bash
python Whisper_mce.py --model_path "your model path" --audio_path "your test audio path"
```


## MCE Dataset
[MCE Dataset](https://drive.google.com/file/d/1CFgHxTzYBKnIkRVBdCwlJXahZq3Zi87B/view?usp=sharing)</br>
MCE Dataset folder has two folders:</br>
- Audio: mixed Cantonese and English audio files, 160 audio folders</br>
  - `1-160` is the original audio data</br>
  - `1_deal-160_deal` is the cleaned original audio data</br>
  - `1_MCE-160_MCE` is the training format audio data</br>
we provided the training format audio data </br>

- Text: mixed Cantonese and English text (Generated by MADGF) files, 160 CSV files</br>
format(topic, text content)</br>

The MCE Dataset is collected by 20 students from HKUST, **each students have their own name rule and their audio files have different formats.**



### Data Prepared
- step 1: Check the audio file nums(`Check_OriginData_num.py`)
- setp 2: Prepare for audio file rename(`Data_Dislocation.py`)
- step 3: Rename the audio file(`Rename_dataset.py`)
- step 4: Unite the audio format(`Unified_dataset_format.py`)

### MCE Text Generation
- step 1: Generate Original Data(topic_dict) which needs to be handwritten(`First_Data_Generate.py`)
- setp 2: Sample new data from the generated CSV file as the new instance of the topic_dict(`Data_Generate_plus.py`)

### Data Analysis
1. Analyze the MCE dataset audio file distribution (audio length).
```bash
python Audio_Data_info.py --audio_folder_path "your path" --text_folder_path "your path"
```

2. Analyze the MCE dataset text file distribution (English word and Traditional Chinese Character numbers)
```bash
python Text_Data_info.py --text_folder_path "your path"
```

## Model Fine-tune
For model fine-tuning, we use A100(80G) GPUs rented from the Runpod platform.

```bash
pip install -r requirements.txt
wget --quiet --show-progress https://github.com/Run-Pod/runpodctl/releases/download/v1.10.0/runpodctl-linux-amd -O runpodctl && chmod +x runpodctl && sudo cp runpodctl /usr/bin/runpodctl
.\runpodctl send data.txt # Windows send file
runpodctl receive <code from windows> # Linux receive file
apt-get install zip -y
zip -FF Finetune.zip --out ft.zip -fz -y
unzip ft.zip
```
![appendix](./appendix.png)
