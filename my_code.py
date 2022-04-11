import sys

sys.path.append("src")
from loguru import logger

from src.services.collector import devil_king_armed

logger.level("DEBUG")

register_url = ""  # https://www.XXX.com/auth/register  https://www.XXX.com/#/register
nest = "v2board"  # sspanel / v2board
hyper_params = {
    # 注册阶段
    "usr_email": True,  # 🔄 是否需要邮箱注册
    "synergy": False,  # ❓ 是否需要同伴; 邀请码?
    "tos": True,  # 🔄 是否需要同意服务条款
    # 对抗阶段
    "skip": False,  # ❓ 是否需要跳过对抗阶段
    "anti_email": False,  # 🔄 是否需要处理 邮箱验证码
    "anti_recaptcha": True,  # 🔄 是否需要处理 Google reCAPTCHA 人机验证。
    "anti_slider": False,  # 🔄 是否需要处理 滑块验证
    "anti_cloudflare": False,  # 是否需要处理 cloudflare 验证
    # 延拓阶段
    "prism": False,  # 是否 prism模式, 默认malio模式
    "aff": 0,  # ❓ 是否需要aff延拓
    "plan_index": 0,  # ❓ 是否需要plan延拓; 免费套餐ID?
    # 缓存阶段
    "threshold": 3,  # ❓ 是否需要缓存阶段; 用于计算订阅链接生命周期?
}
testCloud = {
    "name": "testCloud",
    "register_url": register_url,
    "nest": nest,
    "hyper_params": {"anti_recaptcha": True, "usr_email": True},
}
ATOMIC = testCloud

SILENCE = False


@logger.catch()
def demo():
    devil_king_armed(ATOMIC, silence=SILENCE).assault()


if __name__ == "__main__":
    demo()
