#version 1.8一个星期完成2024/3/22完工，伪标准版
#version 
#若重复加密已经加密过的字符串则不可逆解密(3/22已经解决了，原因是字符表中没有0)
#2.1 04.05
#2.2 04.08(几乎已经完成了程序，约20天)
#2.3 04.10(加入多行读取，修改了二次加密字典，加入了加入读取剪切板功能)


import os
#需要安装的库
try:
    import pyperclip as cb
except:
    libs = ["pyperclip"]
    #循环遍历安装
    for lib in libs:
        os.system("pip install " + lib)



#定义分隔符
delimiter = "퟿"#ord:55295
#再次加密映射
_to_ = {
    '0': '힧', '1': '힩', '2': '힥', '3': '힫', '4': '힦', '5': '힭', '6': '힮', '7': '힬', '8': '힪', '9': '힨'
}
#总是ASCII码是不一样的就是了

def save(text):
    with open("加密解密文字output.txt", "a", encoding="utf-8") as file:
        # 将变量写入文件，并在每个变量后添加换行符
        file.write(text)

def encrypt(text):
    """
    加密
    """
    output = ""
    #如果输入/get，从剪切板获取文本
    if text == "/get":
        text = cb.paste()
        #替换回车
        new_text = text.replace("\n", "퟉")#\n: 55241
    for char in text:
        #如果char等于分隔符
        if char  == delimiter:
            char = "'unknown charakter'"
        #加密
        output = output + str(ord(char) * password + password) + delimiter
    #使用二次加密字典将数字替换为符号
    for num, letter in _to_.items():
        output = output.replace(num, letter)
    #将output添加到剪切板
    cb.copy(output)
    save(output)
    print(output + "\n" + "Encrypted characters have been added to the clipboard......")

def decrypt(text):
    """
    解密
    """
    if text == "/get":
        text = cb.paste()
        #替换回车
        new_text = text.replace("퟉", "\n")#\n: 55241
    #使用二次加密字典将符号替换为数字
    for num, letter in _to_.items():
        text = text.replace(letter, num)
    print(text)#debug
    #将字符串以分隔符分割为列表
    text_decryption_split = [x for x in text.split(delimiter) if x]
    #解密
    output = ""
    for i in range(len(text_decryption_split)):
        output = output + chr(int((int(text_decryption_split[i]) - password) / password))
        print(output)#debug
    #将output添加到剪切板
    cb.copy(output)
    save(output)
    print(output + "\n" + "Decrypted characters have been added to the clipboard......")




while True:
    password = ""
    #加密模式（1），解密模式（2），停止（3）
    mode = input("Encryption mode (1), decryption mode (2), stop (3): \n")
    input_ = input("Your text (Enter /get to get from the clipboard): \n")
    password_ = str(input("Your password: \n"))
    #把用户输入的密码变成合法的密码
    for char in password_:
        password = int(str(password) + str(ord(char)))
    print(password)#debug
    #退出程序
    if mode == "3":
        break
    #加密模式
    elif mode == "1":
        encrypt(input_)
        #print(text_encryption_full)
    #解密模式
    elif mode == "2":
        #尝试解密
        try:
            decrypt(input_)
            #print(text_decryption_full)
        #如果解密失败
        except:
            print("false password?")
    #如果输入其他的模式
    else:
        print("unknown mode")


input()
