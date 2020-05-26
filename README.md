# ZeroClient(ZC)

Zero是一个Android端的RPC应用，而ZC是Zero的客户端。

## 目的

希望Python代码能够与Android的APK交互，譬如调用APK中特定的方法，解密等等。

## install
```
pip install zeroclient
```

## Example
zc默认端口为8888，Zero程序的端口可以自定义，默认9999。
```
adb forward tcp:8888 tcp:9999
python3 test.py
```

## 使用的项目

- dexsim，利用动态加载和PRC的方式解密。