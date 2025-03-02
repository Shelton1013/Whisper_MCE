# Developing a Multilingual Dataset and Evaluation Metrics for Code-Switching: A Focus on Hong Kong's Polylingual Dynamics

we present the impressive results of **Whisper-MCE**, our fine-tuned Whisper, which was trained using our self-collected dataset, Mixed Cantonese and English **(MCE)** audio dataset, which is generated by our **Multi-Agent Data Generation Framework(MADGF)**. Whisper-MCE achieved an impressive Mix Error Rate (MER) of **14.28%**, which is **35.13%** lower than the original model. It also achieved **12.61%** Character Error Rate (CER) in Common voice zh-HK, positioning it as state-of-the-art. [[Paper](https://arxiv.org/pdf/2310.17953)]

## 🚀 News
- [02/03/2025] We will release a more extensive code-switching dataset [SwitchiLingua](https://github.com/Shelton1013/SwitchLingua) with support for additional languages
- [21/12/2024] MCE is accepted by ICASSP 2025!
- [12/06/2024] The MCE Dataset is released! 
- [27/10/2023] The manuscript can be found on [arXiv](https://arxiv.org/pdf/2310.17953).

  
## 📊 MCE Dataset
You can download the [MCE Dataset from the Google cloud](https://drive.google.com/file/d/1CFgHxTzYBKnIkRVBdCwlJXahZq3Zi87B/view?usp=sharing).

MCE Dataset folder has two folders:</br>
- Audio: mixed Cantonese and English audio files, 160 audio folders</br>
  - `1-160` is the original audio data</br>
  - `1_deal-160_deal` is the cleaned original audio data</br>
  - `1_MCE-160_MCE` is the training format audio data</br>
we provided the training format audio data </br>

- Text: mixed Cantonese and English text (Generated by MADGF) files, 160 CSV files</br>
format(topic, text content)</br>

The MCE Dataset is collected by students from HKUST, **each students have their own name rule and their audio files have different formats.**


## 🏋️ Whisper-MCE

## Requirements
1. Clone this repository and navigate to MMed-RAG folder
```bash
git clone git@github.com:Shelton1013/Whisper_MCE.git
cd Whisper_MCE
pip install -r requirements.txt
```

Our fine-tuned Model: [Whisper-MCE](https://drive.google.com/file/d/14_IFvi0z8zHNJGYetpW5GHxbS0z6p0dt/view?usp=sharing)</br>

Baseline: [Whisper](https://github.com/openai/whisper)

Use our fine-tuned Whisper-MCE for speech recognition
```bash
python Whisper_mce.py --model_path "your model path" --audio_path "your test audio path"
```

For model fine-tuning, we use single A100(80G) GPUs.


## 📅 Schedule
We are currently working on a more extensive code-switching dataset [SwitchiLingua](https://github.com/Shelton1013/SwitchLingua) with support for additional languages, which will be released in the near future. We look forward to sharing it with the research community.


## 📚Citation

```bibtex
@article{xie2023whisper,
  title={Whisper-mce: Whisper model finetuned for better performance with mixed languages},
  author={Xie, Peng and Liu, XingYuan and Chen, ZiWei and Chen, Kani and Wang, Yang},
  journal={arXiv preprint arXiv:2310.17953},
  volume={6},
  year={2023}
}
```

## 📄License
The MCE dataset is intended solely for research purposes to support advancements in automatic speech recognition (ASR). Any commercial use without prior authorization is strictly prohibited. For potential collaborations or licensing inquiries, please reach out to 📮[shelton1013@outlook.com](shelton1013@outlook.com).

## 🙏Acknowledgement
We sincerely thank the students from the Hong Kong University of Science and Technology (HKUST) for their invaluable assistance in recording the dataset. 

