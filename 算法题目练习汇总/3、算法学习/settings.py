import csv

with open('c:\\books.csv') as rf:
    reader = csv.reader(rf)
    headers = next(reader)  #读取第1行，返回的内容为一个列表：如：['书名', '作者', “价格”，'出版社']
    with open('books_out.csv', 'w') as wf:
        writer = csv.writer(wf)
        writer.writerow(headers)

        for book in reader:  #book是一个列表，reader = csv.reader(rf),render是返回所有行，每一行是一个列表
            price = book[-2]  #因为返回的是一个列表，价格字段在倒数第2个
            if price and float(price) >= 80.00:
                writer.writerow(book)  #writerow方法是想csv文件写入一行