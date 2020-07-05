
para = 'ram mar she hes is si a good boy'
splited = para.split(" ")

for i in range(len(splited)):
    ana = []
    ana.append(splited[i])
    for j in range(i+1,len(splited)):
        
        if sorted(splited[i])==sorted(splited[j]):
            ana.append(splited[j])
            
            splited.remove(splited[j])
        if len(ana)!=1:
            print(ana)