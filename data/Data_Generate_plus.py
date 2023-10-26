import pandas as pd
import random

from Data_Generate import Data_Generate

start_epoch = 100
end_epoch = 160

data_generate = Data_Generate()

for i in range(start_epoch, end_epoch):
    read_csv_path = f"""./csv/data_{i}.csv"""
    df = pd.read_csv(read_csv_path, encoding='GBK')

    topic_list = df['Topic'].unique()

    topic_dict = {}
    for topic in topic_list:
        filtered_df = df[df['Topic'] == topic]
        # instance is <class 'numpy.ndarray'>
        instance_array = filtered_df['Instance'].values

        start, end = 0, len(instance_array)-1
        random_number1, random_number2 = random.randint(start, end), random.randint(start, end)

        # if random1 == random2 select the same instance
        if random_number1 == random_number2:
            if random_number1 != end:
                random_number2 = random_number1 + 1
            else:
                random_number2 = 0

        instance1, instance2 = instance_array[random_number1], instance_array[random_number2]

        topic_dict.setdefault(topic, [instance1, instance2])

    save_csv_path = f"""./csv/data_{i+1}.csv"""

    data_generate.generate(topic_dict, save_csv_path)
    print(f"""{save_csv_path}写入成功""")
