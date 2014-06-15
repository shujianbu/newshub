import json

dic = {}
subDic = {}

dic['a'] = 1
dic['b'] = "what a funny story"

subDic['aa'] = [1,2,3,4]
subDic['bb'] = (6,7,8,9) 

dic['sub_dic'] = subDic

encoded = json.dumps(dic)

F = open("sample.json", 'a')
F.write('\n')
F.write(encoded)
F.write('\n ************** \n')
#F.write(dic)
F.close()

