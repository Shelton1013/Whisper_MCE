import os
import pandas as pd
import re
import nltk
folder_path = r'E:\Whisper-base-local\data\csv'

"""
用于统计GPT4数据生成的分布情况（英文和粤语繁体分别有多少个字）
"""

file_list = os.listdir(folder_path)

count_dict = {"天氣_z": 0, "天氣_e": 0,
              "食物_z": 0, "食物_e": 0,
              "旅遊_z": 0, "旅遊_e": 0,
              "娛樂_z": 0, "娛樂_e": 0,
              "體育_z": 0, "體育_e": 0,
              "本地時事_z": 0, "本地時事_e": 0,
              "購物_z": 0, "購物_e": 0,
              "學習_z": 0, "學習_e": 0,
              "工作_z": 0, "工作_e": 0,
              "健康同健身_z": 0, "健康同健身_e": 0,
              "宠物_z": 0, "宠物_e": 0,
              "科技同新闻_z": 0, "科技同新闻_e": 0,
              "电影同电视剧_z": 0, "电影同电视剧_e": 0,
              "音乐同艺术_z": 0, "音乐同艺术_e": 0,
              "爱好同兴趣_z": 0, "爱好同兴趣_e": 0,
              "历史同文学_z": 0, "历史同文学_e": 0,
              "社交媒体同网络文化_z": 0, "社交媒体同网络文化_e": 0,
              "环境_z": 0, "环境_e": 0
              }

def count_english_words(string):
    tokenizer = nltk.tokenize.WordPunctTokenizer()
    tokens = tokenizer.tokenize(string)
    english_words = [word for word in tokens if word.isalpha()]
    word_count = len(english_words)

    return word_count

chinese_count = 0
english_count = 0
for file_name in file_list:
    file_name = folder_path + r'\\' +file_name
    read_csv_path = file_name
    df = pd.read_csv(read_csv_path, encoding='GBK')
    for index, row in df.iterrows():
        topic_z = row['Topic'] +'_z'
        topic_e = row['Topic'] + '_e'
        instance = row['Instance']
        print(instance)
        chinese_count = len(re.findall(r'[\u4e00-\u9fff]', instance))
        english_count = count_english_words(instance)
        print(chinese_count, english_count)
        count_dict[topic_z] += chinese_count
        count_dict[topic_e] += english_count

print(count_dict)
