def inputFloat(prompt:str, min:float=None, max:float=None) -> float:
    if min != None and max != None:
        rge = f'({min} - {max})'
    else:
        rge =''
    resultStr = input(f'{prompt} {rge}')
    try:
        result = float(resultStr)        
    except:
        print(f'輸入錯誤格式:{resultStr}')
        return inputFloat(prompt,min,max)
    if min != None and result < min:
        print(f'輸入數值低於{min}')
        return inputFloat(prompt,min,max)
    if max != None and result > max:
        print(f'輸入數值超過{max}')
        return inputFloat(prompt,min,max)
    return float(result)

def main():
    height = inputFloat("請輸入身高(公分):",min=0 , max=300)
    weight = inputFloat("請輸入體重(公斤):",min=0 , max=300)
    bmi = weight / (height / 100) ** 2
    print(f'您的身高:{height} 公分, 您的體重:{weight} 公斤\n您的BMI是: {bmi:.2f}')

    if bmi < 18.5:
        msg = '體重過輕'
    elif bmi < 24:
        msg = '正常範圍'
    elif bmi < 27:
        msg = '過重'
    elif bmi < 30:
        msg = '輕度肥胖'
    elif bmi < 35:
        msg = '中度肥胖'
    else:
        msg = '重度肥胖'

    print(f'您的體重: {msg}')
    
if __name__ == "__main__":
    main()