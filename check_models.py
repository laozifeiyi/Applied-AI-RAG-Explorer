import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. 加载环境变量
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. 配置并列出可用模型
genai.configure(api_key=api_key)

print("🔍 正在获取你的 API Key 可调用的模型列表...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ 可用模型名称: {m.name}")
except Exception as e:
    print(f"❌ 获取失败: {e}")