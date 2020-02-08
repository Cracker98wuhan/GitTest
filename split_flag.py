import os
import re
import json
import pandas as pd
from nltk.stem.porter import PorterStemmer 
from pandas.core.frame import DataFrame

# 处理原始数据，拆分description_text字段
# 以[[**##**]]为标识，在标识之前为correlation，在标识之后为uncorrelation
# 进行全部小写并词根化处理
# description_id,paper_id,description_text


def StemmingAndLowcase(content):
    try:
        content = content.lower().replace(","," ,").replace("."," .")
    except:
        return ""
    word_list = content.split(" ")
    stemWordList = []
    st = PorterStemmer()
    for word in word_list:
        stemWordList.append(st.stem(word))
    res = " ".join(stemWordList).replace(" ,",",").replace(" .",".")    
    return res


dataframe = pd.read_csv("./SourceData/train_release.csv")
# dataframe = pd.read_csv("sample_input.csv")
for index, row in dataframe.iterrows():
    lines = str(row['description_text']).replace("et al. ","").split(". ")
    correlation = []
    uncorrelation = []
    for line in lines:
        if line == "":
            continue
        if "**##**" in line:
            line = line.replace("[","").replace("]","").replace("*","").replace("#","")
            correlation.append(line)
        else:
            uncorrelation.append(line)
    content = {}
    content['description_id'] = row['description_id']
    content['paper_id'] = row['paper_id']
    content['description_text'] = StemmingAndLowcase(row['description_text'])
    content['correlation'] = StemmingAndLowcase(".".join(correlation))
    content['uncorrelation'] = StemmingAndLowcase(".".join(uncorrelation))
    file = open('split_flag.json','a+',encoding='utf-8')  
    json.dump(content,file,ensure_ascii=False)   
    file.write("\n")

# a = StemmingAndLowcase("signaling pathways in different stages of MI and interactions with other pathways.")
# print(a)


