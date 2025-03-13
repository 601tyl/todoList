# Todo List API

基于Flask和SQLite构建的RESTful API，提供完整的待办事项管理功能，支持增删改查操作和错误处理。

## 功能特性

- RESTful接口设计
- 统一JSON响应格式
- 完整的错误处理机制
- SQLite数据库存储
- 自动API文档生成支持

## 快速开始

### 环境要求
- Python 3.8+
- pip包管理工具

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/601tyl/todoList.git
cd todoList 
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 初始化数据库
```bash
python database/init_db.py
```
4. 启动服务

```bash
python app.py
```


## API文档
### 基础路径
`http://localhost:5000/todos`

### 接口概览

| 方法    | 路径            | 描述                | 请求体示例                            | 成功响应码 |
|---------|-----------------|---------------------|-------------------------------------|------------|
| `GET`   | `/`             | 获取所有待办事项    | 不需要                              | 200        |
| `GET`   | `/<int:todo_id>`| 获取单个待办事项    | 不需要                              | 200        |
| `POST`  | `/`             | 创建新待办事项      | `{"title": "任务名称"}`            | 201        |
| `PUT`   | `/<int:todo_id>`| 更新现有待办事项    | `{"title": "新标题", "completed": true}` | 200    |
| `DELETE`| `/<int:todo_id>`| 删除待办事项        | 不需要                              | 200        |


### 相应格式介绍
```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "id": 1,
    "title": "示例任务",
    "completed": false
  }
}
```