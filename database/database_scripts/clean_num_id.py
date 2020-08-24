# cleaning up the num_id texts

from glob import glob
import re
# fetch all the .txt files
files = glob('*.txt')

i = 17334
for file in files:
    with open (file) as f:
        text = f.read()
        text_edited = text.replace('_cnn_inception100','').replace('csv','png')
        text_edited = re.sub(r'_0+','_',text_edited)
        text_edited = re.sub(r"\[\'[0-9]+\'\,\s\'", "\g<0>shot", text_edited)
        text_edited = re.sub(r"\[\'[0-9]+\',\s","[",text_edited)
        
        w_file = open(file, 'w')
        w_file.write(text_edited)
        w_file.close()
        print(i," remaining....")
        i-=1