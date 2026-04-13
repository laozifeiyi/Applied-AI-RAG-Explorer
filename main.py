import os
import PyPDF2
from dotenv import load_dotenv
import google.generativeai as genai

# 1. 配置环境：读取 .env 里的私密密钥
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ 错误：未在 .env 中找到 GEMINI_API_KEY，请检查配置。")
else:
    # 2. 初始化 Gemini 大脑
    genai.configure(api_key=api_key)
    # 建议使用稳定且支持文本处理的模型，例如 gemini-2.5-flash
    # 加上 models/ 前缀是解决 404 的关键
    model = genai.GenerativeModel('models/gemini-2.5-flash')

    # 3. 定义 PDF 解析工具函数
    def extract_text_from_pdf(pdf_path):
        """读取 PDF 并提取文字内容"""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                full_text = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text
                return full_text
        except FileNotFoundError:
            return None

    # 4. 执行流程
    # 【请确保 data 文件夹里有文件，并修改下面的文件名】
    file_name = "Hadamard_Survey.pdf" 
    target_path = os.path.join("data", file_name)
    
    print(f"🚀 正在处理文件: {target_path}...")
    content = extract_text_from_pdf(target_path)

    if content is not None:
        if not content.strip():
            print("⚠️ 警告：成功打开了 PDF，但未能提取到任何文字内容（可能是纯图片扫描版 PDF）。")
        else:
            print("✅ PDF 读取成功，字数：", len(content))
            print("🤖 正在请求 Gemini 生成学术摘要...")
            
            # 这里的 Prompt（提示词）设计是 Applied AI 的关键能力
            prompt = f"""
            你是一个专业的 AI 学术助理。请根据以下提供的文档内容，
            提取出 3 个核心关键点，并用简洁的中文总结。
            
            文档内容：
            {content[:10000]}  # 截取前10000字防止超出长度限制
            """
            
            try:
                response = model.generate_content(prompt)
                print("\n" + "="*30)
                print("🌟 Gemini 总结结果：")
                print(response.text)
                print("="*30)
            except Exception as e:
                print(f"❌ 调用 Gemini 失败: {e}")
    else:
        print(f"❌ 找不到文件: {target_path}，请检查 data 文件夹。")