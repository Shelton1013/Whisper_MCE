import openai
import pandas as pd


class Data_Generate():
    def __init__(self, api_type, api_base, api_key):
        openai.api_type = api_type
        openai.api_base = api_base
        openai.api_key = api_key

    def generate(self, topic_dict, save_csv_path):
        data_title = [["Topic", "Instance"]]
        df = pd.DataFrame(data_title, dtype=str)
        df.to_csv(save_csv_path, mode='a', index=False, header=False, encoding='GBK')

        for key in topic_dict:
            instance1, instance2 = topic_dict[key][0], topic_dict[key][1]

            content = f"""你係一個香港local，你嘅講野習慣係粵語同英文混合，同時帶有口頭用語，例如{instance1, instance2},
                                    請你再生成粵語與英語混合的,但唔好刻意生成英文,topic係{key},一行一條文本,僅文本無需輸出編號
                                    """

            response = openai.ChatCompletion.create(
                    engine="gpt4",  # choose the model type
                    api_version="2023-05-15",
                    messages=[
                        {"role": "system",
                         "content": content
                         }
                    ]
                )

            data = response['choices'][0]['message']['content']

            data_list = data.split("\n")
            print(data_list)

            write_data_list = []
            for data in data_list:
                if data != '' and data != '\n':
                    data = [key, data]
                    write_data_list.append(data)

            df = pd.DataFrame(write_data_list, dtype=str)

            print(df)
            df.to_csv(save_csv_path, mode='a', index=False, header=False, encoding='GBK', errors='ignore')


