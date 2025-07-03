
```markdown
# 🧠 AIPPT - AI 驱动的 PPT 生成任务系统

AIPPT 是一个基于 Python 构建的后端工作流系统，自动处理 AI 生成 PPT 的全流程任务，包括任务发起、内容生成、合并导出、状态追踪、异常日志记录与结构化归档。

> ✅ 本项目专注于稳定性、可维护性与结构化设计，适用于企业级自动化 AI 内容生成场景。

---

## 📁 项目结构
AIPPT/
├── app/ # Core application logic
│ ├── core/ # Task scheduler and workflow state machine
│ ├── models/ # Data models (e.g., Task)
│ ├── services/ # Business logic for processing tasks
│ ├── utils/ # Logging, HTTP wrappers, utilities
├── logs/ # Auto-generated logs and CSV snapshots
│ ├── aippt_YYYY-MM-DD.log # Runtime log per day
│ ├── tasks_YYYY-MM-DD.csv # Task status snapshot per day
├── main.py # Entry point to start processing loop
├── requirements.txt # Python dependency list
├── README.md # Project documentation
---

## 🚀 项目功能

- [x] 异步任务读取与调度（定期扫描待处理任务）
- [x] 接入 AI 接口进行大纲/内容生成、PPT 导出
- [x] 多阶段任务状态机：submitted → outlining → content_creating → merging → exporting → success
- [x] 所有状态变化记录并写入 CSV 表
- [x] 全局异常捕捉与结构化日志输出（终端 + 日志文件）
- [x] 可适配数据库、文件系统、云存储等扩展

---

## ⚙️ 安装与运行

### 1. 克隆项目

```bash
git clone git@github.com:yanyunfei123/AIPPT.git
cd AIPPT
````

### 2. 创建虚拟环境（建议）

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 启动主循环（任务轮询）

```bash
python main.py
```

---

## 📝 日志与记录说明

所有运行信息与任务状态均被记录：

### ✅ 控制台日志（实时可见）

* 处理进度、错误信息、状态变更

### ✅ 日志文件（logs/aippt\_YYYY-MM-DD.log）

* 每天一个文件，保留最近 14 天
* 包含任务上下文、异常 traceback、系统级日志

### ✅ 任务记录 CSV（logs/tasks\_YYYY-MM-DD.csv）

* 每次运行后自动追加任务状态行
* 可用于后续分析、归档或人工检查

---

## 📦 依赖模块

主要使用以下库：

* `requests`：HTTP 调用
* `logging`：日志系统
* `csv/json`：任务数据读写
* `dataclasses`：数据建模

---

## 🛡️ 安全性与可维护性设计

* 使用 `@dataclass` 进行类型安全建模
* 所有异常均带堆栈追踪、任务上下文输出
* 所有处理逻辑支持模块化扩展，便于拆解与测试
* `.venv/` 环境已默认被 Git 忽略（.gitignore）

---

## 🤝 贡献指南

1. Fork 本项目
2. 新建分支：`git checkout -b feature/my-feature`
3. 提交修改：`git commit -am 'Add my feature'`
4. 推送分支：`git push origin feature/my-feature`
5. 提交 PR 请求合并

---

## 📮 联系作者

如有任何问题、建议或合作意向，欢迎联系作者：

* GitHub: [@yanyunfei123](https://github.com/yanyunfei123)
* 邮箱: 2286604334@qq.com

---
