from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf
import time
import torch
import os
import argparse

device = "cuda:0" if torch.cuda.is_available() else "cpu"

parser = argparse.ArgumentParser()
parser.add_argument("--model_path", help="Whisper-MCE model weight path")
parser.add_argument("--audio_path", help="Test audio path")
args = parser.parse_args()

model_path = args.model_path
audio_path = args.audio_path

start = time.time()
processor = WhisperProcessor.from_pretrained(model_path)
model = WhisperForConditionalGeneration.from_pretrained(model_path).to(device)
# when we generate, so we slice the prefix tokens to: <|lang_id|> <|task|> <|notimestamps|>
forced_decoder_ids = processor.get_decoder_prompt_ids(language="chinese", task="transcribe")

end = time.time()
print('Model Initialize cost time:', end - start)

def Whisper_MCE(audio_path):
    # run code in gpu, test for one time cost 8 seconds
    start2 = time.time()
    data, samplerate = sf.read(audio_path)
    input_features = processor(data, sampling_rate=samplerate, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features.to(device), forced_decoder_ids=forced_decoder_ids, max_new_tokens=2048)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    end2 = time.time()
    print('Transcribe cost time:', end2 - start2)
    return transcription


transcription = Whisper_MCE(audio_path)
print(transcription)
