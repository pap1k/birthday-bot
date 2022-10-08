from core import LongPoll
import os, handler, sys, importlib

importlib.reload(sys)
sys.setdefaultencoding('utf8')

LP = LongPoll(os.getenv("VK_TOKEN"))
LP.addListener('message_new', handler.new_message)
LP.run()