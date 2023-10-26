# Whisper_MCE

## MCE Dataset
Data folder have two folder:</br>
- csv: mixed Cantonese and English text(Generated by GPT4) files, 160 csv files</br>
format(topic, text content)</br>
- MCE Datasets: mixed Cantonese and English audio files, 160 audio folders</br>
1-160 is the original audio data</br>
1_deal-160_deal is the dealed original audio data</br>
1_MCE-160_MCE is the training format audio data</br>

The MCE Dataset is collected by 10 students from HKUST, **each students have their own name rule and their audio file have different types.**

### `Check_OriginData_num.py`
Check if aduio file numbers equal to text row numbers, ensure the data number is correct

---

### `Data_Dislocation.py`
Handle dislocation for folder

---

### `Rename_dataset.py`
Rename audio file to have unified name rule

---

### `Unified_dataset_format.py`
unite the audio type(.wav), sample rate(16,000hz), number of channels(mono)

---
