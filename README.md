# Telegram Bot Framework

Lightweight bot framework with command routing.

```python
from botframework import Bot
bot = Bot(token="TOKEN")
@bot.command("start")
def start(msg): bot.reply(msg, "Hi!")
bot.run()
```
