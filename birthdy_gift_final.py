import tkinter as tk
import random
import pygame
from math import sin, cos, pi
from typing import List, Tuple

class Star:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 400)
        self.size = random.randint(1, 3)
        self.twinkle_speed = random.uniform(0.01, 0.05)
        self.alpha = 0
        self.star_id = self.draw()

    def draw(self):
        return self.canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill="white", outline=""
        )

    def twinkle(self):
        self.alpha += self.twinkle_speed
        brightness = int(127 + 127 * sin(self.alpha))
        self.canvas.itemconfig(self.star_id, fill=f"#{brightness:02x}{brightness:02x}{brightness:02x}")

class Balloon:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.x = random.randint(0, 500)
        self.y = 400
        self.speed = random.uniform(0.5, 1.5)
        self.color = random.choice(['red', 'yellow', 'blue', 'green', 'purple'])
        self.balloon_id = self.draw()

    def draw(self):
        # Draw balloon
        self.canvas.create_oval(
            self.x - 20, self.y - 30,
            self.x + 20, self.y + 30,
            fill=self.color, outline="black"
        )
        # Draw string
        return self.canvas.create_line(
            self.x, self.y + 30,
            self.x, self.y + 60,
            fill="black"
        )

    def float_up(self):
        self.y -= self.speed
        self.canvas.move(self.balloon_id, 0, -self.speed)

class Cake:
    def __init__(self):
        self.candles = []
        self.create()

    def create(self):
        # Add candles
        self.add_candles(5)
        self.animate_flames()

    def add_candles(self, count: int):
        for i in range(count):
            self.candles.append({
                'x': i * 2 + 1,
                'lit': True,
                'angle': random.uniform(-15, 15)
            })

    def draw_candles(self):
        print("\n" * 30)  # Clear console
        for candle in self.candles:
            if candle['lit']:
                # Draw candle with flame
                print(" " * int(candle['x'] + 5 * sin(candle['angle'] * pi / 180)) + "|")
                print(" " * int(candle['x'] + 5 * sin(candle['angle'] * pi / 180)) + "*")
            else:
                # Draw extinguished candle
                print(" " * int(candle['x']) + "|")
        print("\n" + " " * 10 + "🎂 Happy Birthday! 🎂")

    def animate_flames(self):
        for candle in self.candles:
            if candle['lit']:
                # Random flame movement
                candle['angle'] += random.uniform(-5, 5)
                if candle['angle'] > 15:
                    candle['angle'] = 15
                elif candle['angle'] < -15:
                    candle['angle'] = -15

    def blow_out(self):
        # Blow out random candle
        lit_candles = [c for c in self.candles if c['lit']]
        if lit_candles:
            candle = random.choice(lit_candles)
            candle['lit'] = False
            return True
        return False

    def all_out(self):
        return all(not c['lit'] for c in self.candles)
import tkinter as tk
import random
import pygame
from math import sin, cos, pi
from typing import List, Tuple

class Star:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 400)
        self.size = random.randint(1, 3)
        self.twinkle_speed = random.uniform(0.01, 0.05)
        self.alpha = 0
        self.star_id = self.draw()

    def draw(self):
        return self.canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill="white", outline=""
        )

    def twinkle(self):
        self.alpha += self.twinkle_speed
        brightness = int(127 + 127 * sin(self.alpha))
        self.canvas.itemconfig(self.star_id, fill=f"#{brightness:02x}{brightness:02x}{brightness:02x}")

class Balloon:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.x = random.randint(0, 500)
        self.y = 400
        self.speed = random.uniform(0.5, 1.5)
        self.color = random.choice(['red', 'yellow', 'blue', 'green', 'purple'])
        self.balloon_id = self.draw()

    def draw(self):
        # Draw balloon
        self.canvas.create_oval(
            self.x - 20, self.y - 30,
            self.x + 20, self.y + 30,
            fill=self.color, outline="black"
        )
        # Draw string
        return self.canvas.create_line(
            self.x, self.y + 30,
            self.x, self.y + 60,
            fill="black"
        )

    def float_up(self):
        self.y -= self.speed
        self.canvas.move(self.balloon_id, 0, -self.speed)

class Cake:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.candles = []
        self.create()

    def create(self):
        # Draw cake layers
        self.canvas.create_rectangle(150, 230, 350, 300, fill="lightpink", outline="black")  # Bottom
        self.canvas.create_rectangle(175, 190, 325, 230, fill="lightyellow", outline="black")  # Middle
        self.canvas.create_rectangle(200, 150, 300, 190, fill="lightblue", outline="black")  # Top
        
        # Add candles with precise positioning
        self.add_candles(5)

    def add_candles(self, count: int):
        cake_width = 100  # Top layer width
        spacing = cake_width / (count + 1)
        for i in range(count):
            x = 200 + (i + 1) * spacing
            y = 130
            self.candles.append((x, y, True))  # (x, y, lit)
            self.draw_candle(x, y, True)

    def draw_candle(self, x: int, y: int, lit: bool):
        # Candle body
        self.canvas.create_rectangle(
            x - 3, y,
            x + 3, y + 30,
            fill="red", outline="black"
        )
        # Candle flame
        if lit:
            self.flame_id = self.canvas.create_oval(
                x - 5, y - 10,
                x + 5, y,
                fill="yellow", outline="orange",
                tags="flame"
            )
            self.animate_flame(x, y)

    def animate_flame(self, x: int, y: int):
        # Random flame movement
        dx = random.uniform(-2, 2)
        dy = random.uniform(-2, 2)
        self.canvas.move(self.flame_id, dx, dy)
        self.canvas.after(100, lambda: self.animate_flame(x, y))

    def blow_out(self, x: int, y: int):
        for i, (cx, cy, lit) in enumerate(self.candles):
            if cx - 10 < x < cx + 10 and cy - 10 < y < cy + 40:
                if lit:
                    self.candles[i] = (cx, cy, False)
                    self.canvas.delete("flame")
                    self.show_celebration()
                    return True
        return False

    def show_celebration(self):
        # Show celebration text
        self.canvas.create_text(
            250, 100,
            text="Happy Birthday!",
            font=("Arial", 24, "bold"),
            fill="yellow",
            tags="celebration"
        )
        # Animate text
        self.animate_text()

    def animate_text(self):
        self.canvas.move("celebration", random.uniform(-2, 2), random.uniform(-2, 2))
        self.canvas.after(100, self.animate_text)

class Firework:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.x = random.randint(100, 400)
        self.y = 400
        self.color = random.choice(['red', 'yellow', 'blue', 'green', 'purple'])
        self.stage = 0  # 0: rising, 1: exploding, 2: fading
        self.particles = []
        self.trail = []
        self.speed = random.uniform(2, 4)
        self.explosion_size = random.randint(50, 100)
        self.life = 50  # Shorter life
        self.trail_life = 3  # Faster trail disappearance

    def update(self):
        if self.stage == 0:
            self.y -= self.speed
            self.trail.append((self.x, self.y))
            if len(self.trail) > self.trail_life:
                self.trail.pop(0)
            if self.y < 200:
                self.stage = 1
                self.explode()
        elif self.stage == 1:
            self.life -= 1
            if self.life < 0:
                self.stage = 2
                self.cleanup()
        self.draw()

    def explode(self):
        for angle in range(0, 360, 10):
            speed = random.uniform(1, 3)
            dx = cos(angle * pi / 180) * speed
            dy = sin(angle * pi / 180) * speed
            self.particles.append({
                'x': self.x,
                'y': self.y,
                'dx': dx,
                'dy': dy,
                'life': 30  # Shorter particle life
            })

    def draw(self):
        # Clear previous drawing
        self.canvas.delete(f"firework_{id(self)}")
        
        # Draw trail
        for i in range(1, len(self.trail)):
            self.canvas.create_line(
                self.trail[i-1][0], self.trail[i-1][1],
                self.trail[i][0], self.trail[i][1],
                fill=self.color, width=2,
                tags=f"firework_{id(self)}"
            )
        
        # Draw particles
        for particle in self.particles:
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']
            particle['life'] -= 1
            if particle['life'] > 0:
                self.canvas.create_oval(
                    particle['x'] - 2, particle['y'] - 2,
                    particle['x'] + 2, particle['y'] + 2,
                    fill=self.color, outline="",
                    tags=f"firework_{id(self)}"
                )

    def cleanup(self):
        self.canvas.delete(f"firework_{id(self)}")

class CelebrationApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Fantastic Birthday Celebration")
        
        # Setup canvas
        self.canvas = tk.Canvas(root, width=500, height=400, bg="black")
        self.canvas.pack()
        
        # Create background with fewer stars
        self.stars = [Star(self.canvas) for _ in range(50)]
        self.balloons = [Balloon(self.canvas) for _ in range(5)]
        
        # Create cake
        self.cake = Cake(self.canvas)
        
        # Create fireworks
        self.fireworks = []
        
        # Setup event bindings
        self.canvas.bind("<Button-1>", self.on_click)
        
        # Start animation
        self.animate()
        
        # Play music
        self.play_music()

    def on_click(self, event):
        # Try to blow out candles first
        if not self.cake.blow_out(event.x, event.y):
            # If not clicking on candle, launch firework
            self.fireworks.append(Firework(self.canvas))

    def animate(self):
        # Update stars
        for star in self.stars:
            star.twinkle()
        
        # Update balloons
        for balloon in self.balloons:
            balloon.float_up()
            if balloon.y < -100:
                self.balloons.remove(balloon)
                self.balloons.append(Balloon(self.canvas))
        
        # Update fireworks
        if random.random() < 0.03:  # Fewer fireworks
            self.fireworks.append(Firework(self.canvas))
        
        for firework in self.fireworks:
            firework.update()
            if firework.stage == 2:
                self.fireworks.remove(firework)
        
        self.root.after(20, self.animate)

    def play_music(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("birthday.mp3")
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Error playing music: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CelebrationApp(root)
    root.mainloop()
