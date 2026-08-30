import psutil
import os

if __name__ == '__main__':
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and 'main.py' in ' '.join(proc.info['cmdline']):
                proc.terminate()
                print(f"已停止进程 PID: {proc.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
