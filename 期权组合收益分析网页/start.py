import subprocess
import sys
import os

if __name__ == '__main__':
    src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
    main_py = os.path.join(src_dir, 'main.py')
    
    process = subprocess.Popen([sys.executable, main_py])
    print(f"服务器已启动，PID: {process.pid}")
    process.wait()
