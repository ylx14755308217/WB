import os
from hashlib import sha256

def make_password(password):
    # 将密码进行处理
    # 确保password是一个bytes类型
    if not isinstance(password,bytes):
        password = str(password).encode('utf-8')
#产生一个安全密码：包含32个字符的随机数和sha256的哈希值
    safe_password = os.urandom(16).hex()+sha256(password).hexdigest()
    return safe_password

def check_password(password,safe_password):
    '''检查用户输入的密码'''
    # 确保 password 是一个bytes类型
    if not isinstance(password,bytes):
        password =str(password).encode('utf-8')
    password_hash = sha256(password).hexdigest()
    return password_hash == safe_password[32:]

def save_avatar(nickname,avatar):
    '''将用户头像保存到硬盘'''
    base_dir = os.path.dirname(os.path.abspath(__name__)) # 项目文件夹绝对路径
    filepath = os.path.join(base_dir,'static','upload',nickname) # 头像绝对路径
    avatar.save(filepath) # 保存文件
    avatar_url = f'/static/upload/{nickname}'
    return avatar_url