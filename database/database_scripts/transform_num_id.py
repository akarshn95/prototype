import pandas as pd
from glob import glob
import re
# fetch all the .txt files
files = glob('*.txt')
df = pd.read_csv('huge_df.csv')

i = 17334
# the function which finds the matched clip number for the meanframe
def convert(match):  
    video = match.group(1)
    frame = match.group(2)
    clip_no = df[(df['video']==int(video)) & (df['meanframe']==int(frame))]['clip_no'].values
    if len(clip_no):
        return "['shot{}_{}.png".format(video,clip_no[0])
    return match

for file in files:
    with open (file) as f:
        text = f.read()
        # using a function to replace matched strings
        text = re.sub(r"\['shot(.*?)_(.*?).png",convert,text)
        
        write_file = open(file,'w')
        write_file.write(text)
        write_file.close()
        print(i, " remaining....", file)
        i-=1