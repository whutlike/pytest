from PIL import Image
import os

# 你的图片目录
input_dir = r'C:\Users\whutl\Desktop\pic'
output_dir = os.path.join(input_dir, 'cropped')
os.makedirs(output_dir, exist_ok=True)

# ✅ 修改这里：你想要的固定裁剪区域（左上角x, 左上角y, 右下角x, 右下角y）
crop_box = (400, 200, 1500, 2150)

# 支持的图片格式
valid_ext = ('.png', '.jpg', '.jpeg', '.bmp')

for filename in os.listdir(input_dir):
    if filename.lower().endswith(valid_ext):
        img_path = os.path.join(input_dir, filename)
        try:
            with Image.open(img_path) as img:
                cropped = img.crop(crop_box)
                cropped.save(os.path.join(output_dir, f'cropped_{filename}'))
                print(f"✅ 已裁剪：{filename}")
        except Exception as e:
            print(f"❌ 失败：{filename} -> {e}")

print("🎉 全部处理完成！裁剪后的图在：", output_dir)