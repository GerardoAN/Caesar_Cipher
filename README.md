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


技术文档：凯撒密码安全性分析及改进建议
​一、凯撒密码核心机制
​基本原理

单字母替换加密，通过固定位移（shift）对字母进行循环移位（如shift=3时，A→D）
数学公式：E(x)=(x+shift) mod 26（加密），D(x)=(x−shift) mod 26（解密）
非字母字符保留原值，仅处理英文大小写字母
​传统实现特点

密钥空间仅25种可能位移（shift=1~25），易通过暴力穷举破解
明文与密文字符一一对应，频率分布特征显著（如E字母高频出现）
​二、安全性分析
攻击方式	原理及风险等级	典型示例
​暴力破解	遍历25种位移组合（耗时<1秒）	khoor→hello（shift=3）
​频率分析	统计密文字母出现频率匹配明文	英语中E字母占比12.7%
​已知明文攻击	部分明文-密文对推算位移量	已知hello→khoor可反推shift=3
核心缺陷：

​密钥空间过小​（仅25种可能）
​单字母替换模式​（无法抵抗频率分析）
​无混淆扩散机制​（相同明文必得相同密文）
​三、改进建议
1. ​增强密钥安全性
​扩展密钥空间
使用多表替换（如维吉尼亚密码），密钥长度与明文相关
示例：密钥MATH对应位移序列12,0,19,7
​动态位移生成
基于时间戳或随机数生成动态shift值（如shift=(当前分钟数)%26）
2. ​加密算法优化
​多重加密
串联多个凯撒密码（如先shift=3，再shift=5），密钥空间扩展至25^n（n为加密层数）
​混淆扩散机制
加密前对文本进行置换（如反转字符顺序），破坏频率特征
3. ​工程实现优化
​预生成映射表
使用str.maketrans()生成加密/解密映射字典，提升处理效率（万级字符<15ms）
​混合加密框架
结合非对称加密（如RSA）传输凯撒密码的密钥
4. ​防御性设计
​插入混淆字符
每5个字母插入随机符号（如hello→h@e$l%l!o），干扰频率分析
​支持大小写敏感
区分大小写字母映射（如H→K，h→k），增加破解复杂度
​四、改进后应用场景
场景	适用性说明	改进技术支撑
​教育演示	展示古典密码与改进方案的对比	多表替换、动态密钥
​日志混淆	防止日志明文泄露（低安全需求）	多重加密、混淆字符
​CTF密码题设计	结合频率分析与暴力破解挑战	扩展密钥空间




