import asyncio
from fastapi import FastAPI, Depends

from auth.validate_token_header import validate_token
from router import outfit
from config import db_config

app = FastAPI(dependencies=[Depends(validate_token)])

app.include_router(outfit.router)


async def start():
    await db_config.get()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(start())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
