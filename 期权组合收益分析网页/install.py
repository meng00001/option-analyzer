import subprocess
import sys

if __name__ == '__main__':
    print("安装依赖...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    print("依赖安装完成")
