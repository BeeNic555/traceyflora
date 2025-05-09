#!/usr/bin/env bash

# 安装依赖
pip install -r requirements.txt

# 执行数据库迁移
python manage.py migrate

# 收集静态文件
python manage.py collectstatic --noinput
