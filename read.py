data = []

with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
       

print('檔案讀取完畢,總共有', len(data) ,'數據')

print(data[0])