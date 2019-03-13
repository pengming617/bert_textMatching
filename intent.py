from predict import predicts

sentences = [['长的清新是什么意思', '小清新的意思是什么']]
for sentence in sentences:
    dic = predicts([sentence])
    print(dic)

file = open('data/test.txt', 'r')
f = open('data/erro.txt', 'w')
sentences = []
tag = []
for line in file.readlines():
    data = line.replace("\n", "").split("\t")
    sentences.append([data[0], data[1]])
    tag.append(data[2])
resule = predicts(sentences)
erro = 0
for x in range(len(resule)):
    if resule[x][0] != tag[x]:
        erro += 1
        print(sentences[x])
        f.writelines(sentences[x][0]+"\t"+sentences[x][1]+"\t"+resule[x][0]+"\t"+str(resule[x][1])+"\n")
print("test数据集的accuracy为："+str(1-erro/len(resule)))
