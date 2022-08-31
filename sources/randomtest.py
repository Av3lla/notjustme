import random

numdict_102 = {1: '강민재', 2: '강승주', 3: '권일훈', 4: '김동혁', 5: '김현준', 6: '민지환', 7: '박건우', 8: '박시준', 9: '송성제', 10: '송종우', 11: '용승환', 12: '유현준', 13: '이시훈', 14: '이정현', 15: '이지원', 16: '이창현', 17: '임태호', 18: '정세윤', 19: '조정민', 20: '지관우', 21: '하재명'}

a = []

for i in range(10000):
    b = random.randint(1, 21)
    a.append(b)

print('1:', a.count(1), '\n2:', a.count(2), '\n3:', a.count(3), '\n4:', a.count(4), '\n5:', a.count(5), '\n6:', a.count(6), '\n7:', a.count(7), '\n8:', a.count(8), '\n9:', a.count(9), '\n10:', a.count(10), '\n11:', a.count(11), '\n12:', a.count(12), '\n13:', a.count(13), '\n14:', a.count(14), '\n15:', a.count(15), '\n16:', a.count(16), '\n17:', a.count(17), '\n18:', a.count(18), '\n19:', a.count(19), '\n20:', a.count(20), '\n21:', a.count(21))