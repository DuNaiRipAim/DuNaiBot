from nonebot.adapters.onebot.v11 import Message,MessageSegment
from nonebot import on_command, on_message
from src.lib.maimaidx.image import *

help = on_command("help")

#获取帮助列表
@help.handle()
async def get_help():
    help_str = """
    DuNaiBot帮助列表
    欢迎使用DuNaiBot
    本Bot还在开发过程中
    现只开放LeetCode与MaiMaiDX功能
    ---MaiMaiDX功能---
    /mai b40(b50) 查询自己的b40以及b50
    其他功能还在修改中
    ---LeetCode功能---
    /lc每日，/lc，/leetcode回复，发送今天的每日一题。
    可搜索leetcode题目，指令/lc搜索 XXXXX，/lc查找 XXXXX，/leetcode搜索 XXXXX，将以关键词“XXXXX”进行leetcode搜索，发送搜索到的第一道题。
    随机一题，指令/lc随机，/lc随机一题，/leetcode随机将请求leetcode随机一题，发送请求到的任意题目。
    查询用户信息/lc查询 XXXXX，/lc查询用户 XXXXX，/leetcode查询 XXXXX，可查询用户基本信息，XXXXX为用户ID（不能用用户名）。
    对应QQ号绑定LeetCodeID待开发（其实就是CRUD而已x）
    """
    
    await help.send(Message(MessageSegment(
        type="image",
        data={
            "file": f"base64://{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
        },
    )))
    

