# for read the file r 
#code 1:

f1=open('file1','r')
print(f1.read()) 

#code2:

try:
    f=open('file8','r')
except IOError:
    print('file does not exist')
else:
    print(f.closed)
    print(f.mode)
    print(f.name)
    print(f.readable())
    print(f.writable())
finally:
    print('final code is excuted')   


#  for write the file ,create a new file if file does not exists ,w
# it overwrite the previous matter if file already exists
#code1:

f1=open('file1','w')
data=f1.write('hai iam satish ,iam very bad boy')
print(f1.read())

#code2:

try:
    with open('my file', mode='w', encoding='utf-8') as f:
        print(f.writable())  # Shows True
        f.write('iam satish\n')
        f.writelines(["iam gud boy"])
except IOError:
    print('sorry file unable to create')
    print('disk write protected')
finally:
    print("the code executed")
 
 
# r+ read and write > first of all read the file and write the file

f1=open('file1','r+')
print(f1.read())
f1.write('anish')
print(f1.read())

#  for write and read (W+)
f2=open('file2','w+') # it create a new file if it is not exixts
print(f2.tell())
f2.write('hayati')
print(f2.tell())
print(f2.read())

# (a)for append the content
with open ("file1",'a') as f:             #it create a new file if it is not exixts
    c=f.write('\n i will prove my self')  #it append the content at the end of the previous content


# for append and read (A+)
f1=open('file1','a+')     # open a file
print(f1.tell())          # knowing cursor position
f1.write(' iam gud boy')  # writing sentence
print(f1.tell())          # knowing cursor position
f1.seek(0)                # putting cursor at starting index
print(f1.read())          # reading the file inside content
print(f1.tell())          # knowing cursor position