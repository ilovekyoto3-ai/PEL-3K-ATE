import tkinter as tk
class OverlayApp:
    def __init__(self, root):
        # 基本設定
        self.root.title("Black Overlay")
        self.root.geometry("500x300")
        self.root.configure(bg="black")

        # 永遠最上層
        self.root.attributes("-topmost", True)

        # 半透明
        self.alpha = 0.65
        self.root.attributes("-alpha", self.alpha)

        # 移除視窗邊框
        self.root.overrideredirect(True)

        # 拖曳功能
        self.offset_x = 0
        self.offset_y = 0

        self.root.bind("<Button-1>", self.click_win)
        self.root.bind("<B1-Motion>", self.drag_win)

        # 快捷鍵
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("<Up>", self.increase_alpha)
        self.root.bind("<Down>", self.decrease_alpha)

        # 提示文字
        label = tk.Label(
            root,
            text=(
                "ESC = 關閉\n"
                "↑ = 增加透明度\n"
                "↓ = 降低透明度\n"
                "滑鼠拖曳移動"
            ),
            fg="white",
            bg="black",
            font=("Arial", 14)
        )

        label.pack(expand=True)

        # 右鍵調整大小
        self.root.bind("<Button-3>", self.start_resize)
        self.root.bind("<B3-Motion>", self.do_resize)

    def click_win(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def drag_win(self, event):
        x = event.x_root - self.offset_x
        y = event.y_root - self.offset_y
        self.root.geometry(f"+{x}+{y}")

    def increase_alpha(self, event):
        self.alpha = min(1.0, self.alpha + 0.05)
        self.root.attributes("-alpha", self.alpha)

    def decrease_alpha(self, event):
        self.alpha = max(0.1, self.alpha - 0.05)
        self.root.attributes("-alpha", self.alpha)

    def start_resize(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.start_width = self.root.winfo_width()
        self.start_height = self.root.winfo_height()

    def do_resize(self, event):
        new_width = self.start_width + (event.x - self.start_x)
        new_height = self.start_height + (event.y - self.start_y)

        self.root.geometry(f"{new_width}x{new_height}")


if __name__ == "__main__":
    root = tk.Tk()
    app = OverlayApp(root)
    root.mainloop()