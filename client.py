import asyncio

from asyncua import Client, Node
from asyncua.common.subscription import DataChangeNotif, SubHandler

ENDPOINT = 'opc.tcp://localhost:4840'
NAMESPACE = 'http://examples.freeopcua.github.io'


class MyHandler(SubHandler):
    def __init__(self):
        self._queue = asyncio.Queue()

    def datachange_notification(self, node: Node, value, data: DataChangeNotif) -> None:
        self._queue.put_nowait([node, value, data])
        print(f'Data change notification was received and queued.')

    async def process(self) -> None:
        try:
            while True:
                # Get data in a queue.
                [node, value, data] = self._queue.get_nowait()
                path = await node.get_path(as_string=True)

                # *** Write your processing code ***

                print(f'New value {value} of "{path}" was processed.')

        except asyncio.QueueEmpty:
            pass


async def main() -> None:
    async with Client(url=ENDPOINT) as client:
        # Get a variable node.
        idx = await client.get_namespace_index(NAMESPACE)
        node = await client.get_objects_node().get_child([f'{idx}:MyObject', f'{idx}:MyVariable'])

        # Subscribe data change.
        handler = MyHandler()
        subscription = await client.create_subscription(period=0, handler=handler)
        await subscription.subscribe_data_change(node)

        # Process data change every 100ms
        while True:
            await handler.process()
            await asyncio.sleep(0.1)


if __name__ == '__main__':
    asyncio.run(main())
