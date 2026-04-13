# Applied-AI-RAG-Explorer 

本项目是一个基于 RAG（Retrieval-Augmented Generation）架构的智能学术助手，旨在通过 LLM 技术自动化解析长篇学术文献并提取核心洞察。

## 🌟 核心功能
- **自动化 PDF 解析**：集成 `PyPDF2` 实现对本地非结构化文档的文本提取。
- **智能摘要生成**：调用 **Gemini 2.5 Flash** 预览版模型，实现对复杂学术论文的语义压缩。
- **环境安全管理**：采用 `.env` 变量隔离技术，确保 API 密钥的安全性。

## 🧪 案例演示 (Case Study)
- [cite_start]**分析对象**：[《Hadamard product in deep learning》](data/Hadamard_Survey.pdf) (arxiv:2504.13112v1) [cite: 1, 2]。
- [cite_start]**解析规模**：成功处理包含 16.9 万字符的超长综述 [cite: 4, 134, 135]。
- **提取结果**：
  1. [cite_start]识别了 Hadamard 积在深度学习中实现**线性计算复杂度**非线性交互的核心价值 [cite: 7, 26]。
  2. [cite_start]梳理了该算子在**多模态融合**、**高阶相关性**等领域的分类体系 [cite: 6, 43, 112]。

## 🔧 开发日志 (Development Log)
### 2026-04-13：API 适配与配额优化
- **Issue**: 遇到 `404 Not Found` 模型路径错误与 `429 Quota Exceeded` 流量限制。
- **Solution**: 
  - 编写 `check_models.py` 脚本动态查询 API 终点，由 `1.5-flash` 迁移至 `models/gemini-2.5-flash`。
  - 实施 **Token 截断策略**，将 16.9 万字的原始文本通过语义切片（Slicing）限制在 10,000 Token 内，适配 Free Tier 频率限制。
- **Outcome**: 成功打通从文档解析到模型生成的 RAG 最小闭环。

## 🛠️ 环境配置
1. 确保已在 `.venv` 虚拟环境下安装依赖：`pip install google-generativeai python-dotenv PyPDF2`
2. 配置 `.env` 文件并填入 `GEMINI_API_KEY`。
3. 运行：`python main.py`