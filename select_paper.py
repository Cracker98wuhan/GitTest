
import json
import time 
start  = time.time()
papers = []

paper_data = open('./ProcessRes/candidate_paper.json','r',encoding='utf-8') 
# paper_data = open('./ProcessRes/sample_candidate.json','r',encoding='utf-8') 
paper_content = paper_data.readlines()
print("------------ Candidate Paper Loaded ------------")
paper_data.close()


source_file = open('./ProcessRes/split_flag.json','r',encoding='utf-8') 
# source_file = open('./ProcessRes/sample_input.json','r',encoding='utf-8') 
f = open("CanAndVal.json","a+",encoding="utf-8")
try:
    while True:
        text_line = source_file.readline()
        if text_line:
            data = json.loads(text_line)
            if isinstance(data,dict):
                paper_id = data['paper_id']
                for paper in paper_content:
                    if paper_id in paper:
                        paper = paper.replace("\n","")
                        paper = json.loads(paper)
                        data["title"] = paper["title"]
                        data["abstract"] = paper["abstract"]
                        json.dump(data,f)
                        f.write("\n")
                else:
                    continue
        else:
            break
finally:
    source_file.close()

end = time.time()
print(int(end-start))