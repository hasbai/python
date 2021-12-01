import os

old_wd = os.getcwd()
print('当前工作目录初始为：', old_wd)

os.chdir('C:\\')
cwd = os.getcwd()
print('当前工作目录变更为：', cwd)

print('列出此目录下的文件及文件夹：')
print(os.listdir())

os.chdir(old_wd)
print('当前工作目录还原为：', old_wd)
