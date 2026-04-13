# Applied-AI-RAG-Explorer

本项目是一个基于 RAG (Retrieval-Augmented Generation) 架构的学术辅助工具，旨在利用大语言模型技术自动化解析长篇学术文献并提炼核心研究洞察。

## 核心功能
- **自动化解析**：集成 PyPDF2 实现对本地非结构化 PDF 文档的文本提取。
- **智能语义压缩**：调用 Gemini 2.5 Flash 预览版模型，实现对学术数据的高维总结。
- **工程化管理**：通过 Python 虚拟环境 (.venv) 与环境变量 (.env) 确保依赖隔离与 API 安全。

## 案例分析：Hadamard Product 综述解析
本项目对学术论文《Hadamard product in deep learning》进行了深度解析：
- **处理规模**：成功处理超过 16.9 万字符的原始文本数据。
- **提取结论**：
  1. 识别了 Hadamard 积以线性计算复杂度实现非线性交互的核心算法价值。
  2. 系统梳理了该算子在多模态融合、高阶相关性等领域的分类体系与应用现状。

## 开发日志 (Development Log)
### 2026-04-13：API 架构适配与 Token 策略优化
- **问题诊断**: 修复了 API 接口下的模型路径匹配错误。
- **解决方案**: 
  - 通过动态查询 API Endpoint，完成从 1.5 到 2.5 系列模型的平滑迁移。
  - 针对免费层级配额限制，实施了 Input Slicing 策略，将单次处理上限优化至 10,000 Token。
- **项目状态**: 成功构建了从文档解析到模型生成的闭环链路。

## 环境配置
1. 确保已在 .venv 虚拟环境下安装依赖：
   pip install google-generativeai python-dotenv PyPDF2
2. 在 .env 文件中配置 GEMINI_API_KEY。
3. 执行主程序：
   python main.py