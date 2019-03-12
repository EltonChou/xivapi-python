[![Pypi](https://img.shields.io/pypi/v/xivapi.svg?style=flat-square)](https://pypi.org/project/xivapi/)
[![Pypi](https://img.shields.io/pypi/pyversions/xivapi.svg?style=flat-square)](https://pypi.org/project/xivapi/)
# xivapi-python
[xivapi](https://xivapi.com) wrapper in python

Feel free to contact me at [xivapi discord](https://discord.gg/MFFVHWC) @iIKAze

## Installation
```shell
pip install xivapi
```

## Usage
```py
import xivapi as XIVAPI

xivapi = XIVAPI.Client('YOUR_API_KEY')
```

### Example

Find item information:
```py
import asyncio

async def weapon_info(name):
    result = await xivapi.search(name)
    weapon_id = result['Results'][0]['ID']
    info = await xivapi.content('item', weapon_id)
    print(info)

loop = asyncio.get_event_loop()
loop.run_until_complete(weapon_info('Omega Torquetum'))
```