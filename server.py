import asyncio
import random

from asyncua import Server

ENDPOINT = 'opc.tcp://localhost:4840'
NAMESPACE = 'http://examples.freeopcua.github.io'


async def main() -> None:
    # Start a server.
    server = Server()
    await server.init()
    server.set_endpoint(ENDPOINT)
    idx = await server.register_namespace(NAMESPACE)
    await server.start()
    print(f'Server started: {server}')

    # Create a node.
    myobj = await server.get_objects_node().add_object(idx, 'MyObject')
    myvar = await myobj.add_variable(idx, 'MyVariable', 1)
    await myvar.set_writable()

    # Write a new value every second.
    while True:
        await myvar.write_value(random.randint(1, 100))
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
