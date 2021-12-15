import re                                                                                  #regular expression

def fun6_1(string):

    pas1 = re.search('[\-]*[\d]+[\.]*[\d]*[*/][\-]*[\d]+[\.]*[\d]*',string)                # 處理乘除運算式
    pas2 = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-]+[\-]*[\d]+[\.]*[\d]*',string)             # 處理加減運算式
    pas3 = re.search('[\d][\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',string)              # 處理有負數的乘除運算式
    pas4 = re.search('[\d]',string)                                                        # 確認是否為運算式

    
    if pas3 :                                                                              # 先處理有負數的乘法運算 (被乘數是負數的狀況)
        d = re.search('[\d][\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',string).group()     # 抓出第一個含負數之乘除的運算
        if str(re.findall('[*]',d)) == '[\'*\']':                                          # 判斷是否為乘法
            test = d.split('*')                                                            # 從乘法運算元切開
            count1_temp = test[0]                                                          # 儲存負的被乘數
            count2 = float(test[1])                                                        # 儲存被乘數
            test2 = count1_temp.split('-')                                                 # 把被乘數中之純數字取出
            count1 = float(test2[1])
            answer = count1 * count2*-1                                                    # 乘法運算
            answer = '+' + str(answer)                                                     
        elif str(re.findall('[/]',d)) == '[\'/\']':                                        # 判對是否為除法
            test = d.split('/')                                                            # 從除法運算元切開
            count1_temp = test[0]                                                          # 儲存負的被除數
            count2 = float(test[1])                                                        # 儲存除數
            test2 = count1_temp.split('-')                                                 # 把被除數中之純數字取出
            count1 = float(test2[1])                                                       
            answer = count1 / count2*-1                                                    # 除法運算
            answer = '+' + str(answer)                                                     
        output = re.sub('[\-][\d]+[\.]*[\d]*[*/][\-][\d]+[\.]*[\d]*',str(answer),string,1) # 將答案寫回原運算式
        return output
    elif pas1:                                                                             # 處理正數的乘除法
        b = re.search('[\-]*[\d]+[\.]*[\d]*[*/][\-]*[\d]+[\.]*[\d]*',string).group()       # 抓出第一個乘除的運算
        if str(re.findall('[*]',b)) == '[\'*\']':                                          # 處理乘法
            test = b.split('*')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 * count2
        elif str(re.findall('[/]',b)) == '[\'/\']':                                        # 處理除法
            test = b.split('/')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 / count2
        output = re.sub('[\-]*[\d]+[\.]*[\d]*[*/][\-]*[\d]+[\.]*[\d]*',str(answer),string,1)  # 將答案寫回原運算式
        return output
    elif pas2:                                                                             # 處理加減運算式
        b = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-]+[\-]*[\d]+[\.]*[\d]*',string).group()    # 抓出第一個加減法運算式
        if str(re.findall('[\+]',b)) == '[\'+\']':                                         # 判斷加法
            test = b.split('+')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 + count2
        elif str(re.findall('[\-]',b)) == '[\'-\']':                                       # 判斷減法
            test = b.split('-')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1 - count2
        elif str(re.findall('[\-]',b)) == "['-', '-']":                                    # 判斷運算式中是否包含兩個負號 (EX. 1--3 = 1+3 =4)
            c = re.search('[0-9\.]+[\+\-][\-*0-9\.]+',string).group()                      
            test = c.split('-')
            count1 = float(test[0])
            count2 = float(test[1])
            answer = count1*-1 - count2
        elif str(re.findall('[\-]',b)) == "['-', '-', '-']":                               # 判斷運算式中是否包含三個負號 (EX. -7--2 = -7+2 = -5)
            d = re.search('[0-9\.]+[\+\-][\-*0-9\.]+',string).group()
            test = d.split('-')
            count1 = float(test[0])
            count2 = float(test[2])
            answer = count1*-1 + count2
        output = re.sub('[\-]*[\d]+[\.]*[\d]*[\+\-]+[\-]*[\d]+[\.]*[\d]*',str(answer),string,1)   # 將答案寫回原運算式
        return output
    elif pas4 == None:                                                                    # 處理非數字運算式的case
        return '請輸入正確的算式'
    else:                                                                                 # 若運算式處理到只剩一個數字，則該數字最終運算結果
        return string
