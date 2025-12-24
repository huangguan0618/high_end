from amzqr import amzqr
import os

# ================= 配置 =================
# 1. 你的视频链接 (扫码后看企鹅跳舞)
video_url = "https://www.bilibili.com/video/BV19f24BSErY/?spm_id_from=333.1007.tianma.3-3-7.click"

# 2. 你的动态背景图 (必须是 .gif)
gif_bg = "pop.gif"

# 3. 输出文件名 (必须以 .gif 结尾)
output_file = "Dancing_Poop_QR.gif"
# =======================================

print("💩 [Processing Dynamic GIF QR...]")

version, level, qr_name = amzqr.run(
    words=video_url,
    version=1,
    level="H",  # 必须用高容错，因为动图干扰大
    picture=gif_bg,  # 传入 GIF
    colorized=True,  # 彩色
    contrast=1.0,  # 对比度
    brightness=1.0,  # 亮度
    save_name=output_file,
    save_dir=os.getcwd(),
)

print(f"\n✅ 这是一个有味道的动态二维码: {output_file}")
