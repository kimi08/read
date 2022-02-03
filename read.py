data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('檔案讀取完畢,總共有', len(data) ,'數據')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
    print(sum_len)

print('平均留言長度為', sum_len / len(data))


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])  

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

#good = [d for d in data if 'good' in d]   <<這是快寫法,與上程式相同
