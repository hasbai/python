import os
import config

if __name__ == "__main__":
    admin = os.popen("fltmc>nul&&(echo 1)||(echo 0)").read().strip()

    if admin == "0":
        print("请以管理员模式运行！")
    else:
        print("加入网络......")
        print(os.popen("zerotier-cli join {}".format(config.zerotier_network)).read())
        print("设置允许DNS......")
        print(os.popen("zerotier-cli set {} allowDNS=1".format(config.zerotier_network)).read())
        print("设置 Moon 节点......")
        print(os.popen("zerotier-cli orbit {} {}".format(config.zerotier_moon, config.zerotier_moon)).read())
        print("列出节点......")
        print(os.popen("zerotier-cli peers").read())

    s = input("按 Enter 键以退出")
