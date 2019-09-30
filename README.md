# 实验室信息管理系统(LIMS)

Laboratory Information Management System

## 服务启动
```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_apps.py
```

## 服务依赖
- MariaDB
- Redis


## 项目依赖
```bash
pip install Flask-RESTful
pip install Flask-HTTPAuth
pip install Flask-SQLAlchemy
pip install sqlacodegen==1.1.6
pip install gunicorn
pip install eventlet
pip install mysqlclient
pip install redis
pip install requests
pip install future
pip install supervisor
```

## 接口定义

注意调试模式影响缩进
1. DEBUG = True     indent=2
2. DEBUG = False    indent=4

动作 - 成功
```
# 创建
{
    "id": 8,
    "message": "创建成功",
    "result": true
}

# 更新
{
    "message": "更新成功",
    "result": true
}

# 删除
{
    "message": "删除成功",
    "result": true
}
```

动作 - 失败
```
{
    "message": "更新失败",
    "result": false
}
```

查询 - 成功
```
# 详情
{
    "customer": {
        "company_address": "company address",
        "company_email": "",
        "company_fax": "021-62345678",
        "company_name": "company name put",
        "company_site": "http://www.baidu.com",
        "company_tel": "021-62345678",
        "company_type": 1,
        "create_time": "2019-09-27T06:21:33",
        "id": "1",
        "update_time": "2019-09-27T16:48:30"
    }
}

# 列表
{
    "customers": [
        {
            "company_address": "company address",
            "company_email": "",
            "company_fax": "021-62345678",
            "company_name": "company name 2",
            "company_site": "http://www.baidu.com",
            "company_tel": "021-62345678",
            "company_type": 1,
            "create_time": "2019-09-27T07:30:10",
            "id": "7",
            "update_time": "2019-09-27T07:30:10"
        },
        {
            "company_address": "company address",
            "company_email": "",
            "company_fax": "021-62345678",
            "company_name": "company name 1",
            "company_site": "http://www.baidu.com",
            "company_tel": "021-62345678",
            "company_type": 1,
            "create_time": "2019-09-27T06:41:30",
            "id": "6",
            "update_time": "2019-09-27T06:41:30"
        }
    ],
    "total": 7
}
```

查询 - 失败
```
{
    "message": "Resource not found.",
    "result": false,
    "status": 404
}
```

请求 - 失败
```
{
    "message": "Bad request.",
    "result": false,
    "status": 400
}
```

路由错误
```
{
    "message": "URL not found.",
    "result": false,
    "status": 404
}
```

权限拒绝
```
{
    "message": "Token required.",
    "result": false,
    "status": 403
}
```

服务错误
```
{
    "message": "Internal server error.",
    "result": false,
    "status": 500
}
```
