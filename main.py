f=open("C:\\Code\\files\\vy.txt","r")
f_out = open("C:\\Code\\files\\vy_count.txt","w")
line=0
for lines in f:
    wc=lines.split(' ')
    print(len(wc))
    f_out.write(lines + str(len(wc)))

f.close()
f_out.close()