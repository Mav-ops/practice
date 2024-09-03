import gzip
f_in=open('test.txt','rb')
f_out=gzip.open('test.txt.gz','wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

f=gzip.open('test.txt.gz','rb')
f_out=open('text3.txt','wb')
file_content=f.read()
f_out.write(file_content)
f.close()
f_out.close()