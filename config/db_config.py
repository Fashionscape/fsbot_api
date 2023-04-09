import yaml


async def get():
    with open("./db_config.yml", "r") as file:
        config = yaml.safe_load(file)

        return config
