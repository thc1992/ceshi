import base64

with open("./facelog.txt", 'r')as f:
    ima = base64.b64decode(f.read())
    file = open('./test.jpg', 'wb')
    file.write(ima)
    file.close()
    print(f.read());
