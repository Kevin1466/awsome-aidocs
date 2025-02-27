import os
import sys

# 添加项目路径
sys.path.insert(0, os.path.abspath(".."))

# 项目基本信息
project = "opensource LLM learning materials"
author = "credits to original authors"
copyright = f"2025, {author}"

# 配置文档格式
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# 主文档入口
master_doc = "index"

# 添加 Markdown 支持
extensions = ["myst_parser"]

# 配置 HTML 输出
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": -1,  # 显示所有层级的导航
}