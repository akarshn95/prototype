# Find the number of clips matched for each num_id

from glob import glob
import re
import pandas as pd
# fetch all the .txt files
files = glob('*.txt')
i = 0
count = []
for file in files:
    with open (file) as f:
        text = f.read()   
        num_id = file
        num_id = num_id.replace('.txt','')
        count.append([num_id,len(re.findall(r'\[.*?\]',text))])
        i += 1
        # w_file = open(file, 'w')
        # w_file.write(text_edited)
        # w_file.close()

df = pd.DataFrame(count, columns=['num_id','count'])
df.to_csv('num_id_count.csv', index=False)