from MCE.Text_Data_Generation.Data_Generate import Data_Generate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--api_type", help="GPT-4 API type")
parser.add_argument("--api_base", help="GPT-4 API base")
parser.add_argument("--api_key", help="GPT-4 API key")
parser.add_argument("--save_csv_path", help="GPT-4 API key")

args = parser.parse_args()

api_type = args.api_type
api_base = args.api_base
api_key = args.api_key
save_csv_path = args.save_csv_path


"""
Generate Original Data(topic_dict) which needs to be hand written
Store the generated data in csv file
Sample new data from this generated csv as the new instance of the topic_dict
"""
data_generate = Data_Generate(api_type, api_base, api_key)

"""
topic_dict = {"天氣": ["你睇咗今日嘅weather forecast未？話係會有heavy rain，記得帶雨傘出門啊！", "睇落去，今晚嘅sky好clear，應該可以見到好多stars。"],
              "食物": ["這間餐廳嘅steak真係好delicious，我一定再嚟!", "我今晚想去食street food，嗰度嘅煎餅同魚蛋好tasty，令我好想念香港嘅夜晚。"],
              "旅遊": ["我好想去travel，特別係想去Europe，嗰度嘅architecture同culture真係好attractive。", "我最喜歡去beach holiday，喺沙灘上sunbathing，然後去海裡surfing，好relaxing啊！"],
              "娛樂": ["我最近好迷Netflix嘅series，尤其係'Stranger Things'，每集都好exciting，我每晚都追睇。", "我鐘意去karaoke，因為我可以唱我最喜歡嘅pop songs，而且跟朋友一齊唱更加開心。"],
              "體育": ["我覺得swimming係一種好全面嘅運動，可以train到全身嘅肌肉，同時都可以relax。", "我好鐘意watch football matches，特別係喺bar同一班朋友一齊睇，氣氛真係好exciting！"],
              "本地時事": ["我睇到新聞話佢哋要建新嘅MTR line，我覺得呢個plan好有用，可以幫助ease traffic congestion。", "最近嘅政府budget有啲controversial，有啲人覺得佢太保守，有啲人覺得佢太radical。你點睇？"],
              "購物": ["我喺weekend鐘意去mall shopping，可以一邊shopping一邊enjoy air conditioning，好comfortable。", "我最鐘意喺online shopping，好方便，我可以喺家中就買到我想要嘅product。"],
              "學習": ["我覺得學習一種新嘅language係一個好interesting嘅挑戰，我現在正在學日語，好fun。", "我覺得self-learning係一種好重要嘅技能，特別係喺呢個information age，我哋可以喺Internet學到好多嘢。"],
              "工作": ["我覺得communication skills係工作中好重要，無論你做咩工，你都需要能夠effective咁同人溝通。", "我覺得work-life balance好重要，雖然我們要hardworking，但係我哋都需要時間relax同埋enjoy life。"]}
"""

topic_dict = {"健康同健身": ["我成日都去gym，係為咗keep fit，健康好重要啊！", "我成日都喺office做嘢，真係要抽多啲時間去做exercise。"],
              "宠物": ["我個貓貓成日都喺度睡覺，真係lazy到爆。", "你見過我個parrot未？佢可以學我哋講嘢嘅，真係好smart。"],
              "科技同新闻": ["我最近都有follow住AI嘅新聞，真係好fascinating。", "我最近都有睇blockchain嘅新聞，聽說嗰個technology對金融業有好大嘅影響。"],
              "电影同电视剧": ["最近我都有追劇，嗰套drama嘅storyline好吸引，每集都令人期待。", "我嘅偶像喺嗰套action movie有演出，佢嘅演技真係好好，我好support佢。"],
              "音乐同艺术": ["我最鍾意嘅band就係嗰個，佢哋嘅音樂好有feel，每次聽都好享受。", "我學緊彈piano，雖然開始有啲難，但係我覺得好有趣，我會繼續學。"],
              "爱好同兴趣": ["我鍾意嘅game就係嗰個，我覺得好有挑戰性，好好玩。", "我最鍾意嘅hobby就係攝影，我成日都會帶我部camera去唔同地方影相。"],
              "历史同文学": ["我上學時候最鍾意嘅subject就係歷史，我覺得佢好有意思。", "我讀過嗰個經典嘅小說，佢嘅plot好吸引，我覺得好好睇。"],
              "社交媒体同网络文化": ["我最鍾意嘅app就係Instagram，我成日都會上嚟睇人地嘅照片同影片", "我成日都會用WhatsApp同我嘅朋友傾計，好方便，可以隨時keep in touch。"],
              "环境": ["我覺得我哋都應該要做啲咩嘢去protect我哋嘅environment，例如recycle同減少用塑膠袋。", "我覺得sustainable living好重要，我哋要珍惜地球資源。"]
              }


data_generate.generate(topic_dict, save_csv_path)
print(f"""{save_csv_path}save successfully""")

