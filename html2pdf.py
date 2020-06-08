import time
import pdfkit
wk_path = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=wk_path)


result=[]
with open('D:\\urls.txt','r') as f:
	for line in f:
		result.append(list(line.strip('\n').split(',')))
print(result)

url='https://www.cnblogs.com/sriba/p/8043294.html'
path='D:\pdf'
time1 = time.time()
for i in range (1,len(result)):
	output = path +"\\" + str(i) + ".pdf"
	pdfkit.from_url(result[i-1], output, configuration=config)

time2 = time.time()
print(str(time2 - time1)+" s")