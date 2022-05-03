def splitStr(stroka):
    buf = []
    for elent in stroka:
        if elent != ' ':
            buf.append(int(elent))
    return buf