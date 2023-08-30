
def calculate_bmi(weight, height):
    """
    计算BMI指数的函数。
    参数：
    weight（float）：体重，单位为千克。
    height（float）：身高，单位为米。
    
    返回值：
    BMI指数（float）。
    """
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    """
    判断BMI指数所处范围的函数。
    参数：
    bmi（float）：BMI指数。
    
    返回值：
    一个描述BMI范围的字符串。
    """
    if bmi < 18.5:
        return "体重过轻"
    elif bmi < 24.9 and bmi >= 18.5:
        return "正常范围"
    elif bmi >= 24.9 and bmi < 29.9:
        return "超重"
    else:
        return "肥胖"