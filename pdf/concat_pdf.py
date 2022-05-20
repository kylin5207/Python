"""
合并pdf
"""
import PyPDF2 as p # 导入PyPDF2，注意区分大小写

pdf=open('initial.pdf','rb') #打开待添加水印的原文件

rd = p.PdfFileReader(pdf)

sp=rd.getPage(0)

psy=open('test.pdf','rb') #打开水印的文件

rd2 = p.PdfFileReader(psy)

sp2=rd2.getPage(0)

sp.mergePage(sp2) #执行合并

jg=p.PdfFileWriter() #新的PDF

jg.addPage(sp) #将合并好的放入新的PDF

wc=open('after.pdf','wb')#另存为结果

jg.write(wc)

wc.close()

