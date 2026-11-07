from config import SMM_SERVICE_ID

async def add_order(link, quantity):
    result = await api_request({
        "action": "add",
        "service": SMM_SERVICE_ID,
        "link": link,
        "quantity": int(quantity)
    })

    return result
