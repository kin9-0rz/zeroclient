from zeroclient import zero_client

# TODO 这里需要封装成一个库
# ZeroServer - Android Lib
# zero-rpc - jar
# zero-loader - jar
# ZeroClient - Python Lib - pi
# 用法
# 其他APP，工具直接引用这个2个库

client = zero_client.SnippetClient()
client.connect()

client.rpc("hello")

# data = {
#     'className': 'ujvnd.wx.ogp.ul.c.a',
#     'fieldName': 'g'
# }
# client._rpc("GetFieldValue", data)

data = {
    'className': 'android.util.Base64',
    'methodName': 'decode',
    'arguments': ['X/2pNiEW6Vc=', 2]
}
client.rpc("InvokeStaticMethod", data)

data = {
    'className': 'ujvnd.wx.ogp.ul.a.a',
    'methodName': 'a',
    'arguments': [[95, 253, 169, 54, 33, 22, 233, 87], 'fmsd1234'],
    'argumentTypes': ['byte[]', 'java.lang.String']
}
client.rpc("InvokeStaticMethod", data)
