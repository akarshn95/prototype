import json
import glob
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

files = glob.glob("*.json")
stop_words = set(stopwords.words('english'))
stop_words.update(["I","I'm", "I've", "I'd"])

i = 5607
for file in files:
    with open(file) as f:
        asr_dict = json.load(f)
        for k,v in asr_dict.items():
            words = v.split(' ')
            words_cleaned = []
            for word in words:
                if word not in stop_words:
                    words_cleaned.append(word)
            asr_dict[k] = " ".join(words_cleaned)
    json_f = json.dumps(asr_dict, indent=4)
    w_file = open(file, 'w')   
    w_file.write(json_f)
    w_file.close()
    print(i, " remaining...")
    i -= 1