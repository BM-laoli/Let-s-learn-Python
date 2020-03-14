# 1.打开文件
# 2．读取文件．写入文件
# 3.关闭文件

file_read = open("dasd.txt")

file_write = open("dasd[复件].txt",'w')

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()


# 大文件的操作呢？读一行就写一行



file_read = open("dasd.txt")

file_write = open("dasd[复件].txt",'w')

while True:

    text = file_read.readline()

    if not text:
        break

    file_write.write(text)

file_read.close()
file_write.close()