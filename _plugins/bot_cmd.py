import os

from EAbotoy import Action, GroupMsg

master = 550991679  # 只允许自己用


def receive_group_msg(ctx: GroupMsg):
    if ctx.FromUserId == master and ctx.Content.startswith('cmd'):
        try:
            msg = str(os.popen(ctx.Content
                               .replace('sudo', '')
                               .replace('rm', '')
                               .replace('cmd', '')
                               .strip()).read())
        except Exception:
            msg = 'error'
        finally:
            Action(ctx.CurrentWxid).sendGroupText(ctx.FromGroupId, content=msg)
