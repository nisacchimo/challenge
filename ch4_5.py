#http://tinyurl.com/hkzgqrv

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Cloud not convert the string to a float.")

c = convert("hi")
print(c)
