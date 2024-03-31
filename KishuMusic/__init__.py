from KishuMusic.core.bot import Jarvis
from KishuMusic.core.dir import dirr
from KishuMusic.core.git import git
from KishuMusic.core.userbot import Userbot
from KishuMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Jarvis()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
