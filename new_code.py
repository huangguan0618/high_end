from amzqr import amzqr
import os

# ================= 配置中心 =================

video_url = "https://www.bilibili.com/video/BV19f24BSErY/?spm_id_from=333.1007.tianma.3-3-7.click"

# 2. 这里填你下载的【圣诞树背景图】文件名
# (必须放在当前目录下)
bg_image = "final.jpg"

# 3. 生成的文件名
output_file = "F.png"

# ===========================================

print("🎄 [Compiling Cyber Christmas Tree...]")

# 核心生成函数
version, level, qr_name = amzqr.run(
    words=video_url,  # 扫码跳转的链接（那个视频）
    version=1,  # 自动控制大小
    level="L",  # 纠错等级 H (High)，背景花哨也能扫
    picture=bg_image,  # 你的圣诞树图片
    colorized=True,  # 彩色二维码 (True=保留圣诞树原色)
    contrast=1.0,  # 对比度 (默认1.0，如果扫不出可适当调高)
    brightness=1.0,  # 亮度 (默认1.0，如果背景太深，调成 1.2 变亮)
    save_name=output_file,  # 输出文件名
    save_dir=os.getcwd(),  # 保存到当前目录
)

print(f"🎁 文件已生成: {output_file}")
