def order(sentence):
    s = sentence.split(' ')
    res = ['' for k in range(len(s))]
    for i in range(1, len(s)+1):
        for k in range(0, len(s)):
            if str(i) in s[k]:
                res[i-1]=s[k]
    return ' '.join(res)
