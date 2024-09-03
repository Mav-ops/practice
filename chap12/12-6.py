def importAs(newname):
    return __import__(newname)
sys = importAs('sys')