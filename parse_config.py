import yaml
import os

subpath = "GOG.com/Galaxy/plugins/installed/minecraft_636ca436-f5fb-4e03-be57-76a90699ee0b/config.yml"
with open(os.path.join(os.getenv("LOCALAPPDATA"), subpath)) as config:
    config = yaml.load(config, Loader=yaml.FullLoader)
