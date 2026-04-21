import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convert_to_pdf():
    file_paths = filedialog.askopenfilenames(
        title="請選擇要轉換的圖片",
        filetypes=[("圖片檔案", "*.jpg *.jpeg *.png")]
    )
    
    if not file_paths:
        return

    save_path = filedialog.asksaveasfilename(
        title="儲存 PDF 為",
        defaultextension=".pdf",
        filetypes=[("PDF 檔案", "*.pdf")]
    )

    if not save_path:
        return

    try:
        image_list = []
        for path in file_paths:
            img = Image.open(path).convert('RGB')
            image_list.append(img)
        
        if image_list:
            first_img = image_list.pop(0)
            first_img.save(save_path, save_all=True, append_images=image_list)
            messagebox.showinfo("成功", f"PDF 已成功儲存至：\n{save_path}")
            
    except Exception as e:
        messagebox.showerror("錯誤", f"轉換失敗：{str(e)}")

root = tk.Tk()
root.title("JPG 轉 PDF 工具")
root.geometry("300x150")

label = tk.Label(root, text="圖片轉 PDF 工具", font=("Arial", 12))
label.pack(pady=10)

btn = tk.Button(root, text="選擇圖片並開始轉換", command=convert_to_pdf, 
                bg="#4CAF50", fg="white", padx=10, pady=5)
btn.pack(pady=10)

root.mainloop()