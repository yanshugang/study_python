"""
只有try块不抛异常，才会执行after_call()
"""


def dangerous_call():
    pass


def after_call():
    pass


def log(t):
    pass


try:
    dangerous_call()
except OSError:
    log("OSerror")
else:
    after_call()