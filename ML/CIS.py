
f = open('/Users/jackpincombe/Desktop/cis.pages','r').read()

word_replace = {'.',':'}
replaced = ''

for line in f.split("\n"):
    for word , newWord in word_replace.items():
        replaced += line.replace(word,newWord)

f.close()
f = open("/Users/jackpincombe/Desktop",'w')
f.write(replaced)
f.close()