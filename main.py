from core import LongPoll
import os, handler

LP = LongPoll(os.getenv("VK_TOKEN"))
LP.addListener('message_new', handler.new_message)
LP.run()