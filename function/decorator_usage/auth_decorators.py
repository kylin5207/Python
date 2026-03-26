current_user = {"name": "zhangsan", "role": "user"}  # 模拟当前用户

def admin_required(func):
    def wrapper(*args, **kwargs):
        if current_user["role"] != "admin":
            print(f"权限不足：{current_user['name']} 不是管理员")
            return None                    # 不执行原函数，直接返回
        return func(*args, **kwargs)       # 是管理员，正常执行
    return wrapper

@admin_required
def delete_user(user_id):
    print(f"已删除用户{user_id}")
    return True

# 当前用户是普通用户
delete_user("123")
# 权限不足：zhangsan 不是管理员

# 换成管理员
current_user = {"name": "admin", "role": "admin"}
delete_user(123)
# 已删除用户 123