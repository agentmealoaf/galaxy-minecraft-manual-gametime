import sys
from typing import Any

from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform
from galaxy.api.types import Authentication, Game, LicenseInfo, LicenseType
from galaxy.api.plugin import GameTime
from version import __version__
from parse_config import config
import yaml

class PluginMinecraftGametime(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(Platform.Minecraft, __version__, reader, writer, token
        )

    # required
    async def authenticate(self, stored_credentials=None):
       self.store_credentials({'dummy': 'dummy'})
       return Authentication(user_id='Minecraft_ID', user_name='Minecraft Player')
    
    # required
    async def get_owned_games(self):
        return [
            Game('1', 'Minecraft: Java Edition', None, LicenseInfo(LicenseType.SinglePurchase))
        ]
    
    async def get_game_time(self, game_id: str, context: Any) -> GameTime:
        time_played = config.get("minutes")
        last_played = 1514768400
        return GameTime(game_id, time_played, last_played)


def main():
    create_and_run_plugin(PluginMinecraftGametime, sys.argv)

# run plugin event loop
if __name__ == "__main__":
    main()
