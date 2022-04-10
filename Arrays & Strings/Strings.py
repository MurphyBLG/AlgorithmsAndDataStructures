f = open("INPUT.txt", 'r')
text = f.readlines()

ans = ""
for linet in text:
    i = 0
    line = linet[::-1]
    while i < len(line):
        if line[i] == '.':
            ans += line[i]
            i+=1
            while (i < len(line) and line[i] == ' '):
                i+=1
        else:
            ans+=line[i]
        
        i+=1


print(ans[::-1])