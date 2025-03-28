# 创建一个文件 "C:\add_xor.txt"，初始化一个文件
with open("../add_xor.txt", "w") as file:
    file.write("")
# 定义 str 变量，初始值为空字符串
str_var = ""

# 提示用户输入 4 个字节的二进制密文和明文
m_hex = input("请输入4个字节的密文（十六进制）：")
t_hex = input("请输入4个字节的明文（十六进制）：")

# 将十六进制字符串转换为整数
m = int(m_hex, 16)
t = int(t_hex, 16)

# 提取每个字节的二进制值
m1 = m & 0xFF  # 提取第一个字节的二进制值
m2 = (m >> 8) & 0xFF  # 提取第二个字节的二进制值
m3 = (m >> 16) & 0xFF  # 提取第三个字节的二进制值
m4 = (m >> 24) & 0xFF  # 提取第四个字节的二进制值
t1 = t & 0xFF  # 提取第一个字节的二进制值
t2 = (t >> 8) & 0xFF  # 提取第二个字节的二进制值
t3 = (t >> 16) & 0xFF  # 提取第三个字节的二进制值
t4 = (t >> 24) & 0xFF  # 提取第四个字节的二进制值

# 先XOR后ADD
xor = 255
a = 1

with open("../add_xor.txt", "a") as file_xor_add:
    print("先XOR后ADD")
    file_xor_add.write("先XOR后ADD\n")
    for a in range(256):
        add = (m1 ^ xor) - t1  # ^:位运算，二进制异或运算符，两个二进制数的每一位进行比较，如果相同则为0，不同则为1
        if m2 == ((t2 + add) & 0xFF) ^ xor and m3 == ((t3 + add) & 0xFF) ^ xor and m4 == ((t4 + add) & 0xFF) ^ xor:
            add = (0x100 - add) & 0xFF  # 计算溢出部分，确保在 0 到 255 的范围内`
            print(f"{a}.异或={xor}  .加={add}")
            file_xor_add.write(f"{a}.异或={xor}  .加={add}\n")
        xor -= 1

    # 先ADD后XOR
    xor = 255
    print("先ADD后XOR")
    file_xor_add.write("先ADD后XOR\n")
    for a in range(256):
        add = m1 - (t1 ^ xor)
        if m2 == ((t2 ^ xor) + add) & 0xFF and m3 == ((t3 ^ xor) + add) & 0xFF and m4 == ((t4 ^ xor) + add) & 0xFF:
            add = (0x100 - add) & 0xFF
            print(f"{a}.加={add}  .异或={xor}")
            file_xor_add.write(f"{a}.加={add}  .异或={xor}\n")
        xor -= 1
