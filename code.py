import time
import playsound
import os
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox, ttk

class JiahaoSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("嘉豪模拟器")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # 设置字体和样式
        self.style = ttk.Style()
        self.style.configure("TButton", font=("SimHei", 12))
        self.style.configure("TLabel", font=("SimHei", 12), background="#f0f0f0")
        
        # 添加标题
        self.title_label = ttk.Label(root, text="嘉豪模拟器", font=("SimHei", 16, "bold"))
        self.title_label.pack(pady=20)
        
        # 添加状态标签
        self.status_label = ttk.Label(root, text="点击下方按钮开始模拟")
        self.status_label.pack(pady=10)
        
        # 添加开始按钮
        self.start_button = ttk.Button(root, text="成为嘉豪", command=self.start_simulation)
        self.start_button.pack(pady=20)
        
        # 添加退出按钮
        self.exit_button = ttk.Button(root, text="退出程序", command=root.quit)
        self.exit_button.pack(pady=10)
        
        # 添加进度条
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, length=300, mode='determinate')
        self.progress_bar.pack(pady=10)
        self.progress_bar['value'] = 0
        
    def start_simulation(self):
        # 禁用开始按钮，防止重复点击
        self.start_button.config(state="disabled")
        self.status_label.config(text="准备开始...")
        
        # 在新线程中运行模拟过程，避免阻塞GUI
        simulation_thread = threading.Thread(target=self.run_simulation)
        simulation_thread.daemon = True  # 设为守护线程，主线程结束时自动终止
        simulation_thread.start()
        
    def run_simulation(self):
        # 更新状态
        self.root.after(0, lambda: self.status_label.config(text="3..."))
        self.root.after(0, lambda: self.progress_var.set(33))
        time.sleep(1)
        
        self.root.after(0, lambda: self.status_label.config(text="2..."))
        self.root.after(0, lambda: self.progress_var.set(66))
        time.sleep(1)
        
        self.root.after(0, lambda: self.status_label.config(text="1!"))
        self.root.after(0, lambda: self.progress_var.set(99))
        time.sleep(1)
        
        self.root.after(0, lambda: self.status_label.config(text="来吧嘉豪，开始装逼吧！"))
        self.root.after(0, lambda: self.progress_var.set(100))
        
        # 播放音频 - 添加文件检查和备选音频库方案
        audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Mark Snow - The X-Files (Original Version).mp3")
        
        # 检查文件是否存在
        if not os.path.exists(audio_path):
            self.root.after(0, lambda: messagebox.showerror("错误", f"音频文件不存在: {audio_path}"))
        else:
            audio_played = False
            
            # 尝试使用playsound库播放
            try:
                playsound.playsound(audio_path)
                audio_played = True
            except Exception as e:
                self.root.after(0, lambda: messagebox.showwarning("警告", f"playsound库播放失败: {e}\n尝试使用pygame库播放..."))
                
                # 尝试使用pygame库播放
                try:
                    import pygame
                    pygame.mixer.init()
                    pygame.mixer.music.load(audio_path)
                    pygame.mixer.music.play()
                    # 等待音频播放一小段时间确保开始播放
                    pygame.time.delay(1000)
                    audio_played = True
                except ImportError:
                    self.root.after(0, lambda: messagebox.showwarning("提示", "pygame库未安装，请使用pip install pygame安装后重试"))
                except Exception as e2:
                    self.root.after(0, lambda: messagebox.showerror("错误", f"pygame播放失败: {e2}"))
            
            if not audio_played:
                self.root.after(0, lambda: messagebox.showinfo("提示", "音频播放功能暂时不可用，请安装所需依赖库"))
        
        # 执行系统命令 - 在单独的CMD窗口中从C盘根目录扫盘
        os.system('start cmd /k "color 0A && cd /d C:\ && dir /s"')
        
        # 模拟结束，重新启用按钮
        self.root.after(0, lambda: self.start_button.config(state="normal"))
        self.root.after(0, lambda: self.status_label.config(text="模拟完成，点击下方按钮再次开始"))

# 创建主窗口并启动应用
if __name__ == "__main__":
    root = tk.Tk()
    app = JiahaoSimulator(root)
    root.mainloop()