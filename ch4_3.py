#http://tinyurl.com/hkzgqrv

def add_mult(a,b,c,d=100,e=200):
    """Return the result of two optional params
    multiplied by tha additon of 3 required params.
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int.
    :param e: int.
    :return: int.
    """
    return a+b+c*d*e

result = add_mult(10,15,20)
print(result)
