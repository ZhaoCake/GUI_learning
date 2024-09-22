import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import scrolledtext
from ttkthemes import ThemedTk
import requests
from PIL import Image, ImageTk
import io

def fetchImage(image_type="iw233"):
    request_url = f"https://api.iw233.cn/api.php?sort={image_type}"
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            return response.content  # 返回图像的二进制数据
        else:
            print(f"获取图像失败。状态码: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"发生错误: {e}")
        return None

def saveImage(image, filename="image.jpg"):
    with open(filename, "wb") as f:
        f.write(image)
        print("图像保存成功。")

def fetchWeiboHot():
    url = "https://api.andeer.top/API/hot_wb.php"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["data"][:50]  # 只获取前50条数据
        else:
            print(f"获取微博热搜失败。状态码: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"发生错误: {e}")
        return []

def translate(text):
    url = f"https://api.andeer.top/API/fanyi2.php?msg={text}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"翻译失败。状态码: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"发生错误: {e}")
        return None

class ImageFetcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("岛风酱我是你的粉丝啊")
        self.root.geometry("800x600")  # 设置窗口大小为800x600
        self.root.resizable(False, False)  # 不可变窗口大小

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="抓取图像")
        self.create_image_fetcher_tab()

        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="微博热搜")
        self.create_weibo_hot_tab()

        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="英译中")
        self.create_translation_tab()

    def create_image_fetcher_tab(self):
        self.left_frame = ttk.Frame(self.tab1)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.image_type_var = tk.StringVar(value="top")  # 默认值修改为中文类型
        self.image_types = {
            "random": "随机全部图像",
            "iw233": "随机无色图像",
            "top": "精选图像",
            "yin": "银发",
            "cat": "兽耳",
            "xing": "星空",
            "mp": "竖屏",
            "pc": "横屏"
        }

        self.type_label = ttk.Label(self.left_frame, text="选择图像类型：")
        self.type_label.pack(pady=5)

        self.type_menu = ttk.OptionMenu(
            self.left_frame, 
            self.image_type_var, 
            "精选图像",  # 修改为中文类型
            *self.image_types.values()
        )
        self.type_menu.pack(pady=5)

        self.fetch_button = ttk.Button(self.left_frame, text="抓取图像", command=self.fetch_image)
        self.fetch_button.pack(pady=5)

        self.use_default_path = tk.BooleanVar(value=True)
        self.default_path_check = ttk.Checkbutton(self.left_frame, text="使用默认文件路径", variable=self.use_default_path)
        self.default_path_check.pack(pady=5)

        self.save_button = ttk.Button(self.left_frame, text="保存图像", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.image_frame = ttk.Frame(self.tab1)
        self.image_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.image_label = ttk.Label(self.image_frame, text="没有图像")
        self.image_label.pack(pady=10)

        self.image_data = None
        self.default_filename = "抓取的图像.jpg"

    def create_weibo_hot_tab(self):
        self.weibo_text = scrolledtext.ScrolledText(self.tab2, wrap=tk.WORD, width=70, height=20)
        self.weibo_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.fetch_weibo_button = ttk.Button(self.tab2, text="获取微博热搜", command=self.display_weibo_hot)
        self.fetch_weibo_button.pack(pady=10)

    def create_translation_tab(self):
        self.translate_frame = ttk.Frame(self.tab3)
        self.translate_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_label = ttk.Label(self.translate_frame, text="请输入英文：")
        self.input_label.pack(pady=5)

        self.input_text = tk.Text(self.translate_frame, height=10, width=70)  # 增大文本框
        self.input_text.pack(pady=5)

        self.translate_button = ttk.Button(self.translate_frame, text="翻译", command=self.perform_translation)
        self.translate_button.pack(pady=10)

        self.output_label = ttk.Label(self.translate_frame, text="翻译结果：")
        self.output_label.pack(pady=5)

        self.output_text = tk.Text(self.translate_frame, height=10, width=70)  # 增大文本框
        self.output_text.pack(pady=5)
        self.output_text.config(state=tk.DISABLED)

    def fetch_image(self):
        image_type_key = list(self.image_types.keys())[list(self.image_types.values()).index(self.image_type_var.get())]
        self.image_data = fetchImage(image_type_key)

        if self.image_data:
            image = Image.open(io.BytesIO(self.image_data))
            self.resize_and_display_image(image)
            self.save_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("错误", "抓取图像失败。")
            self.save_button.config(state=tk.DISABLED)

    def resize_and_display_image(self, image):
        window_width = 800 - 200  # 减去左侧框架的宽度
        window_height = 600

        aspect_ratio = image.width / image.height
        if image.width > window_width or image.height > window_height:
            if aspect_ratio > 1:  # 宽图
                new_width = window_width
                new_height = int(window_width / aspect_ratio)
            else:  # 长图
                new_height = window_height
                new_width = int(window_height * aspect_ratio)
        else:
            new_width, new_height = image.width, image.height  # 使用原始大小

        image = image.resize((new_width, new_height), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.tk_image, text="")
        self.image_label.image = self.tk_image  # 保持对图像的引用

    def save_image(self):
        if self.image_data:
            if self.use_default_path.get():
                filename = self.default_filename  # 使用默认文件名
            else:
                filename = simpledialog.askstring("保存图像", "输入文件名：", initialvalue=self.default_filename)
                if not filename:  # 如果用户没有输入文件名，使用默认值
                    filename = self.default_filename
            
            saveImage(self.image_data, filename)
            messagebox.showinfo("成功", "图像保存成功！")

    def display_weibo_hot(self):
        weibo_data = fetchWeiboHot()

        if weibo_data:
            self.weibo_text.delete(1.0, tk.END)  # 清空文本框内容
            for item in weibo_data:
                self.weibo_text.insert(tk.END, f"热搜 #{item['num']}: {item['title']} - 热度: {item['hot']}\n\n")
        else:
            messagebox.showerror("错误", "获取微博热搜失败。")

    def perform_translation(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("警告", "请输入文本进行翻译。")
            return

        translation_result = translate(input_text)
        if translation_result and translation_result["code"] == 200:
            translated_text = translation_result["data"]["翻译后"]
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated_text)
            self.output_text.config(state=tk.DISABLED)
        else:
            messagebox.showerror("错误", "翻译失败。")

if __name__ == "__main__":
    root = ThemedTk(theme="radiance")
    style = ttk.Style()
    # 更改默认字体和颜色
    style.configure(".", font=("Arial", 14), foreground="#333", background="#fff")
    app = ImageFetcherApp(root)
    root.mainloop()
