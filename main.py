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
    
    
    
# 主程式    
if __name__ == "__main__":    
    if text[0:2] == '計算' and text[-4:] == '等於多少':     # 判斷 "計算(計算式)等於多少"  EX.計算6*9-12等於多少
        string = text[2:-4]
        plus = re.search('[(][\d\+\-*/.]+[)]',string)      # 判斷計算式中是否有括號
        if plus:                                           # 若有括號，先算括號內之運算式
            while plus:
                d = str(plus)
                s = d.split("'")
                response_plus = HW.fun6_1(s[1][1:-1])      # 呼叫 fun6_1() 計算程式
                b = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-*/][\-]*[\d]+[\.]*[\d]*',response_plus)   # 判斷式子中是否存在還未運算完的部分
                while b:
                    if b:
                        response_plus = HW.fun6_1(response_plus)                                  # 重複疊帶運算式，直到該括號內運算式處理完畢
                        b = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-*/][\-]*[\d]+[\.]*[\d]*',response_plus)
                string = re.sub('[(][\d\+\-*/.]+[)]', str(response_plus), string, 1)              # 將括號運算式替換成計算的結果
                plus = re.search('[(][\d\+\-*/.]+[)]',string)                                     # 尋找是否還有其他外擴號 EX. ((12-6)*8)，若有則回到84行，繼續處理外括號運算
        response_temp = HW.fun6_1(string)                                                         # 處理不含括號的運算式    
        a = re.search('[\-]*[\d]+[\.]*[\d]*[\+\-*/][\-]*[\d]+[\.]*[\d]*',response_temp)           # 判斷算式是否還有未完成的部分
        while a:                                                                                  # 疊代運算式直到完成
            if a:
                response_temp = HW.fun6_1(response_temp)
                a = re.search('[0-9\.]+[*/\+\-][0-9\.]+',response_temp)
        if a == None:                                                                             # 計算完成
            response = response_temp
    print("運算結果為",response)
