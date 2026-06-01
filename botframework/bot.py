"""Bot framework."""
import re
from typing import Callable, Dict, List
from dataclasses import dataclass

@dataclass
class Message:
    chat_id: int
    user_id: int
    text: str
    message_id: int

class Bot:
    def __init__(self, token):
        self.token = token
        self.handlers = []
    def command(self, pattern):
        def dec(func):
            self.handlers.append((re.compile(f"^{pattern}$"), func))
            return func
        return dec
    def reply(self, msg, text):
        print(f"[Reply]: {text}")
    def handle(self, cid, uid, text, mid):
        for pat, func in self.handlers:
            if pat.match(text.strip()):
                func(Message(cid,uid,text,mid))
                return
        print("Unknown command")
    def run(self):
        print(f"Bot started with {len(self.handlers)} handlers")
