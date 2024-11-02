import re

pattern = r"\d{8}\s?"  # 匹配8位数字后跟一个可选的空格

result = re.sub(pattern, "", text, count=1)  # 使用正则表达式替换第一个匹配项

print(result)