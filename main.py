import re

def fun6_1(string):

    pas1 = re.search('[\-]*[\d]+[\.]*[\d]*[*/][\-]*[\d]+[\.]*[\d]*',string)
    pas2 = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-]+[\-]*[\d]+[\.]*[\d]*',string)
    pas3 = re.search('[\d][\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',string)
    pas4 = re.search('[\d]',string)


    if pas3 :
        d = re.search('[\d][\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',string).group()
        if str(re.findall('[*]',d)) == '[\'*\']':
            test = d.split('*')
            count1_temp = test[0]
            count2 = float(test[1])
            test2 = count1_temp.split('-')
            count1 = float(test2[1])
            answer = count1 * count2*-1
            answer = '+' + str(answer)
        elif str(re.findall('[/]',d)) == '[\'/\']':
            test = d.split('/')
            count1_temp = test[0]
            count2 = float(test[1])
            test2 = count1_temp.split('-')
            count1 = float(test2[1])
            answer = count1 / count2*-1
            answer = '+' + str(answer)
        output = re.sub('[\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',str(answer),string,1)
        return output
    elif pas1:
        b = re.search('[\-]*[\d]+[\.]*[\d]*[*/][\-]*[\d]+[\.]*[\d]*',string).group()
        if str(re.findall('[*]',b)) == '[\'*\']':
            test = b.split('*')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 * count2
        elif str(re.findall('[/]',b)) == '[\'/\']':
            test = b.split('/')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 / count2
        output = re.sub('[\-]*[\d]+[\.]*[\d]*[*/][\-]*[\d]+[\.]*[\d]*',str(answer),string,1)
        return output
    elif pas2:
        b = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-]+[\-]*[\d]+[\.]*[\d]*',string).group()
        if str(re.findall('[\+]',b)) == '[\'+\']':
            test = b.split('+')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 + count2
        elif str(re.findall('[\-]',b)) == '[\'-\']':
            test = b.split('-')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 - count2
        elif str(re.findall('[\-]',b)) == "['-', '-']":
            c = re.search('[0-9\.]+[\+\-][\-*0-9\.]+',string).group()
            test = c.split('-')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1*-1 - count2
        elif str(re.findall('[\-]',b)) == "['-', '-', '-']":
            d = re.search('[0-9\.]+[\+\-][\-*0-9\.]+',string).group()
            test = d.split('-')
            count1 = float(test[0])
            count2 = float(test[2])
            answer = count1*-1 + count2
        output = re.sub('[\-]*[\d]+[\.]*[\d]*[\+\-]+[\-]*[\d]+[\.]*[\d]*',str(answer),string,1)
        return output
    elif pas4 == None:
        return '請輸入正確的算式'
    else:
        return string
