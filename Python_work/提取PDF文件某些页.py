# -*- coding: utf-8 -*-
"""
先下载PyPDF2这个库
1.讲目标文件读取至Python内存，并且以二进制的方式读取（用rb表示二进制读取）
2.创建一个写对象，将需要提取的PDF文件赋值到写对象里(用wb表示二进制写入)
3.将写对象的变量导出，并储存为PDF文件
"""
import PyPDF2
with open(r"C:\Users\Administrator\Desktop\Python编程：从入门到实践.pdf",
          "rb") as f:
    f_0 = PyPDF2.PdfFileReader(f)
    f_0_w = PyPDF2.PdfFileWriter()
    for page in range(0,9):
        page_object = f_0.getPage(page)
        f_0_w.addPage(page_object)
        with open("提取一些页儿.pdf", "wb") as file:
            f_0_w.write(file)


























