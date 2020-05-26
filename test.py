from zeroclient import zero_client

# TODO 这里需要封装成一个库
# ZeroServer - Android Lib
# zero-rpc - jar
# zero-loader - jar
# ZeroClient - Python Lib - pi
# 用法
# 其他APP，工具直接引用这个2个库
import ast
client = zero_client.SnippetClient()
client.connect()

result = client.rpc("hello")
print("result:")
print(result)

# data = {
#     'className': 'ujvnd.wx.ogp.ul.c.a',
#     'fieldName': 'g'
# }
# client._rpc("GetFieldValue", data)

# data = {
#     'className': 'android.util.Base64',
#     'methodName': 'decode',
#     'arguments': ['EZ5LaexoU7OiZuRcijBTc0DJTu7nFWcNOBHfVE0CMIo=', 2]
# }
# result = client.rpc("InvokeStaticMethod", data)
# print("result:")
# print(result)

# data = {
#     'className': 'ujvnd.wx.ogp.ul.a.a',
#     'methodName': 'a',
#     'arguments': [[17, 158, 75, 105, 236, 104, 83, 179, 162, 102, 228, 92, 138, 48, 83, 115, 64, 201, 78, 238, 231, 21, 103, 13, 56, 17, 223, 84, 77, 2, 48, 138], 'fmsd1234'],
#     'argumentTypes': ['byte[]', 'java.lang.String']
# }
# result = client.rpc("InvokeStaticMethod", data)
# print(result, type(result))
# print(bytearray(result))


data = {
    'className': 'com.inject.WqnqVtPhExE',
    'methodName': 'getVal',
    'arguments': ['EmQAXg8='],
    'argumentTypes': ['java.lang.String']
}
result = client.rpc("InvokeStaticMethod", data)
print(result, type(result))
