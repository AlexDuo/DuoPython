
# 输入交互与格式化输出
username = input("username:")
password = input("password:")
print(username, password)
# 格式化输出，使用''' 来定义字符串 使用+链接变量
name = input("name:")
# 强制类型转换，因为Python 是一个强类型语言
age = int (input("age:"))
salary = input("salary:")

# info = '''
# ---------- info of '''+ name +'''--------
# Name:'''+name+'''
# Age:'''+age+'''
# Salary:'''+salary

# 也可以使用 %s / %d (s/d一定要是小写的 s代表的是String 这个占位符只能够接受字符
# d代表的数字 这个占位符只能接受数字)
# 做占位符 之后按顺序拼接 如下

info = '''
=============== info of %s ==================
Name: %s
Age: %d
Salary: %s
''' % (name,name,age,salary)
# 我们使用info2 来体现另外一种格式化输出

info2 = '''
=============== info of {first} ==================
Name: {first}
Age: {second}
Salary: {third}
'''.format(
    first = name,
    second = age,
    third  = salary
)

# 我们使用 info3 来体现另一种格式化输出方法 这里花括号中的数字表示在format中的位置

info3 = '''
=============== info of {0} ==================
Name: {0}
Age: {1}
Salary: {2}
'''.format(name,age,salary)

print(info3)
# 打印一个变量的数据类型
print(type(age))
