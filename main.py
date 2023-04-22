import asyncio
import msal
from fastapi import FastAPI, Depends

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

from auth.validate_token_header import validate_token
from router import outfit
from config import db_config

app = FastAPI(dependencies=[Depends(validate_token)])

app.include_router(outfit.router)


async def azure():
    cred = DefaultAzureCredential()
    client = SecretClient(vault_url="https://fashionscape.vault.azure.net/", credential=cred)

    secret_name = "fsbot-discord-token-dev"
    s = client.get_secret(secret_name)

    print(s.value)


async def start():
    await db_config.get()

    await azure()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(start())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
