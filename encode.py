while True:
    word=input('input text to encode : ')
    from hashlib import *
    u=md5(word.encode()).hexdigest()
    v=sha1(word.encode()).hexdigest()
    w=sha224(word.encode()).hexdigest()
    x=sha256(word.encode()).hexdigest()
    y=sha384(word.encode()).hexdigest()
    z=sha512(word.encode()).hexdigest()
    print("*"*22)
    print("md5    : " + u)
    print("sha1   : " + v)
    print("sha224 : " + w)
    print("sha256 : " + x)
    print("sha384 : " + y)
    print("sha512 : " + z)  
    print("*"*78)
