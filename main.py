import re                                                                                  #regular expression

def fun6_1(string):

    pas1 = re.search('[\-]*[\d]+[\.]*[\d]*[*/][\-]*[\d]+[\.]*[\d]*',string)                # 處理乘除運算式
    pas2 = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-]+[\-]*[\d]+[\.]*[\d]*',string)             # 處理加減運算式
    pas3 = re.search('[\d][\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',string)              # 處理有負數的乘除運算式
    pas4 = re.search('[\d]',string)                                                        # 確認是否為運算式

    
    if pas3 :                                                                              # 先處理有負數的乘法運算 (被乘數是負數的狀況)
        d = re.search('[\d][\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',string).group()     # 抓出第一個乘除的運算
        if str(re.findall('[*]',d)) == '[\'*\']':                                          # 判斷是否為乘法
            test = d.split('*')                                                            # 從乘法運算元分開
            count1_temp = test[0]                                                          # 儲存負的被乘數
            count2 = float(test[1])                                                        # 儲存乘數
            test2 = count1_temp.split('-')                                                 # 把被乘數中之純數字取出
            count1 = float(test2[1])
            answer = count1 * count2*-1                                                    # 乘法運算
            answer = '+' + str(answer)                                                     # 將答案寫運算式 (將原本的乘法部分以計算結果取代)
        elif str(re.findall('[/]',d)) == '[\'/\']':                                        # 判對是否為除法
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
