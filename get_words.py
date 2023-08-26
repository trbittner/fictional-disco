import ast

count = 0

with open('raw_words_3000.txt') as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    if line:
        map = ast.literal_eval(line)
        if 'A1' in map['level']:
            pos_list = map['pos'].split(',')
            
