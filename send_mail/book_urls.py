#!/usr/bin/python
# -*- coding:utf-8 _*-
# #  FileName    : book_urls
# #  Author      : XiaoHua Wen <wenhua.maker@gmail.com>
# #  Created     : 2018/2/7
# #  Copyright   : 2018-2020
# #  Description :
import os
def getallfiles(path):
    allfile = []
    allname = []
    for dirpath, dirnames, filenames in os.walk(path):
        for name in filenames:
            allname.append(name)
            allfile.append(os.path.join(dirpath, name,))
    return zip(allname,allfile)

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

if __name__ == '__main__':
    path = "F:\\书籍\\"
    allfile = getallfiles(path)
    for file in allfile:
        print(file[0],file[1],get_FileSize(file[1]))
