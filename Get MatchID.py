src = 'Data2.txt'
champPool = {"25"}

with open(src, 'r') as r:
    lines = r.readlines()
    for line in lines:
        champ = line.split()[1].strip()
        champPool.add(str(champ))

print(champPool)        

{'89', '412', '99', '51', '1', '50', '21', '104', '53', '555', '235', '22', '5', '63', '82', '117', '203', '222', '86', '37', '67', '80', '25', '111', '202', '11'}
