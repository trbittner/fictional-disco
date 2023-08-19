import ast

three_kay = []
ef = []

with open('raw_words_3000.txt') as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    if line:
        map = ast.literal_eval(line)
        three_kay.append(map['word'])
        
with open('raw_ef_edu_3000.txt') as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    if line:
        ef.append(line)
    
in_3k_not_ef = []
in_ef_not_3k = []

for item in three_kay:
    if item not in ef:
        in_3k_not_ef.append(item)
        
for item in ef:
    if item not in three_kay:
        in_ef_not_3k.append(item)
        
with open('in_3k_not_ef.txt','w') as file:
    for str in in_3k_not_ef:
        file.write(str + '\n')
        
with open('in_ef_not_3k.txt','w') as file:
    for str in in_ef_not_3k:
        file.write(str + '\n')
        