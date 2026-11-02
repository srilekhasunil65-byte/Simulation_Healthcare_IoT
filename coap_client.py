import asyncio
from aiocoap import Context, Message, GET

async def main():
    protocol = await Context.create_client_context()

    request = Message(
        code=GET,
        uri="coap://127.0.0.1:5683/patient/vitals"
    )

    try:
        response = await protocol.request(request).response
        print("\n===== COAP PATIENT DATA =====")
        print(response.payload.decode("utf-8"))
        print("=============================")

    except Exception as error:
        print("CoAP Client Error:", error)

    finally:
        await protocol.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
