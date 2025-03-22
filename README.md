# Caesar_Cipher
Caesar Cipher encryptor and decryptor built with python
<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/FH089)

# Caesar Cipher

<p align="center">
<img src="https://images.unsplash.com/photo-1568132930457-20ac2189f20b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1100&q=80" width=50% height=50%>

<!--An image is an illustration for your project, the tip here is using your sense of humour as much as you can :D 

You can copy paste my markdown photo insert as following:
<p align="center">
<img src="your-source-is-here" width=40% height=40%>
-->

## 🛠️ Description
<!--Remove the below lines and add yours -->
Simple Caesar Cipher encryptor and decryptor built with python

## ⚙️ Languages or Frameworks Used
<!--Remove the below lines and add yours -->
The script was created with Python3 and the built-in functions in it
## 🌟 How to run
<!--Remove the below lines and add yours -->
```bash
python3 caesarcypher.py 
Enter string to decrypt: hello
khoor
```
## 📺 Demo
<p align="center">
<img src="https://github.com/ndleah/python-mini-project/blob/main/IMG/caesar-cipher.png" width=70% height=70%>


凯撒密码安全性分析及改进建议
​一、安全漏洞分析
​密钥空间过小：仅25种位移可能，暴力破解仅需数秒
​频率特征暴露：密文保留字母频率分布（如英语中'e'出现率12.7%），易被统计破解
​已知明文攻击：获取任意明密文对即可推算密钥（例如已知"hello→khoor"得shift=3）
​二、改进方案
（一）增强加密机制
​多表替换（维吉尼亚密码）​
使用动态位移序列（密钥决定偏移量）
例：密钥"RELATIONS"对应位移序列[17,4,11,8,14,19,8,14,18]
​随机参数注入
引入伪随机数生成动态位移，使相同明文生成不同密文
​扩展字符集
支持ASCII全字符集（包括符号/数字）提升复杂度
（二）工程优化
​预生成映射表加速
用str.maketrans()创建加密映射，处理万级字符耗时<15ms
​混合加密框架
结合RSA传输凯撒密钥，形成非对称+对称双层保护
（三）防御策略
​插入混淆字符
每5字符插入随机符号（如"hello→h@e$l%l!o"）干扰分析
​动态密钥更新
基于时间戳生成位移量（如shift=(当前分钟数)%26）
​三、方案对比
方案类型	密钥空间	抗频率分析	实现复杂度
经典凯撒	25	❌	★☆☆☆☆
维吉尼亚密码	26^N（N为密钥长）	✔️	★★★☆☆
仿射凯撒	311	✔️	★★☆☆☆
随机参数凯撒	26×随机序列长	✔️	★★★★☆
注：仿射凯撒采用E(x)=(ax+b) mod26，需满足gcd(a,26)=1




