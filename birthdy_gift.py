import tkinter as tk  
import random  
import pygame  

class CelebrationAnimation(tk.Canvas):  
    def __init__(self, master=None):  
        super().__init__(master, width=500, height=400)  
        self.pack()  
        self.configure(bg='black')  
        self.candles = []  
        self.fireworks = []  
        self.create_cake()  
        self.bind("<Button-1>", self.light_candle)  
        self.animate_fireworks()  
        self.play_music()  

    def create_cake(self):  
        # 绘制多层蛋糕  
        self.create_rectangle(150, 230, 350, 300, fill="lightpink", outline="black")  # 底层  
        self.create_rectangle(175, 190, 325, 230, fill="lightyellow", outline="black")  # 中层  
        self.create_rectangle(200, 150, 300, 190, fill="lightblue", outline="black")   # 顶层  
        
        # 画蜡烛（螺纹形状）  
        candle_x = 250  
        candle_y = 130  
        self.create_rectangle(candle_x - 5, candle_y, candle_x + 5, candle_y + 30, fill="red", outline="black")  
        self.create_oval(candle_x - 10, candle_y - 10, candle_x + 10, candle_y, fill="yellow")  # 烛光  
        self.candles.append((candle_x, candle_y))  # 记录蜡烛位置  

        # 画蜡烛的螺纹效果  
        for i in range(8):  
            self.create_line(candle_x - 5, candle_y + i * 3, candle_x + 5, candle_y + i * 3 + (i % 2) * 3, fill='red')  

        # 添加祝福语  
        self.create_text(250, 350, text="Happy Birthday!", fill="white", font=("Helvetica", 16))  

    def light_candle(self, event):  
        # 检查是否点击在蜡烛上  
        candle_x, candle_y = self.candles[0]  
        if candle_x - 15 < event.x < candle_x + 15 and candle_y - 5 < event.y < candle_y + 30:  
            self.create_oval(candle_x - 5, candle_y - 10, candle_x + 5, candle_y + 10, fill="yellow", outline="orange")  # 烛光  
            self.launch_fireworks()  

    def launch_fireworks(self):  
        # 启动烟花  
        fireworks_count = 10  # 设置烟花的数量  
        for _ in range(fireworks_count):  
            x = random.randint(50, 450)  
            y = random.randint(50, 200)  
            color = random.choice(['red', 'blue', 'yellow', 'green', 'orange', 'purple'])  
            self.fireworks.append((x, y, color))  
        self.after(500, self.animate_fireworks)  

    def animate_fireworks(self):  
        self.delete("firework")  # 清除旧的烟花  
        for x, y, color in self.fireworks:  
            # 绘制小烟花效果  
            self.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color, outline=color, tags="firework")  
            # 随机生成烟花效果  
            for _ in range(4):  
                self.create_line(x, y, x + random.randint(-15, 15), y + random.randint(-15, 15), fill=color, tags="firework")  
        self.after(300, self.animate_fireworks)  

    def play_music(self):  
        # 播放背景音乐  
        pygame.mixer.init()  
        pygame.mixer.music.load("birthday.mp3")  # 确保有一个名为 birthday.mp3 的文件在同一个目录下  
        pygame.mixer.music.play(-1)  # 循环播放  

if __name__ == "__main__":  
    root = tk.Tk()  
    root.title("Cartoon Cake with Fireworks")  
    animation = CelebrationAnimation(master=root)  
    root.mainloop()  # 确保mainloop是root的，而不是类的cd 