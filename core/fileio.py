import aiofiles


class FileIo:
    @staticmethod
    async def read_file(path: str):
        async with aiofiles.open(path, mode='r') as f:
            data = await f.read()

        return data

    @staticmethod
    async def write_file(path: str, txt: str):
        async with aiofiles.open(path, mode='w') as f:
            await f.write(txt)

        return txt
