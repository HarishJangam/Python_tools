import zlib,base64

file=open("D.pdf","r")
text=file.read();
file.close()
code=base64.b64encode(zlib.compress(text.encode("utf-8"),9))
code=code.decode("utf-8")

f=open("compress.txt","w")
f.write(code)
f.close()