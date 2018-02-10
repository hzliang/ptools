import os
import sys
import re

TIME_REGEX = re.compile('(\d.+\d) ')
WORD_REGEX = re.compile('.*>(.*)')
a_file ='/Users/huzuoliang/lifeifei/CS231n Lecture 14 - Videos and Unsupervised Learning--CSii0dy98E.en.vtt'
dirname = os.path.dirname(a_file)

for file_name in os.listdir(dirname):
    if file_name.endswith('vtt'):
        
        file_path = os.path.join(dirname, file_name)
        print(file_path)
        content=[]
        idx=1
        (a,_) = os.path.splitext(file_path)
        (b,_) = os.path.splitext(a)
        with open(file_path,encoding='utf-8') as fh:
            for line in fh:
                m = TIME_REGEX.match(line)
                if m:
                    content.append(str(idx)+'\n')
                    content.append(m[1].strip().replace('.',',')+'\n')
                    idx = idx+1
                else :
                    strs = line.split('<')
                    w=False
                    words=[]
                    for i in strs:
                        if len(strs) >=2 and not('>' in i) and len(i)>0:
                            words.append(i.strip())
                            w=True
                            continue
                        m = WORD_REGEX.match(i)
                        if m:
                            if len(m[1].strip()) > 0:
                                words.append(m[1].strip())
                                w=True
                    if w:
                        if(len(words) > 1):
                            content.append(' '.join(words)+'\n')
                            content.append('\n')
                        else:
                            content.append(''.join(words)+'\n')
                            content.append('\n')
            
        with open(b+'.srt','w',encoding='utf-8') as fh:
                fh.write(''.join(content))
                    
   

       
        