from .__init__ import *


loop.create_task(bot.run())
try:
    loop.run_forever()
except (KeyboardInterrupt, SystemExit):
    loop.run_until_complete(bot.stop())
    loop.close()