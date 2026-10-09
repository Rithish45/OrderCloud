import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("OrderCloud order processor started")

    order_id = event.get("order_id", "ORD-1001")

    logger.info("Processing order: %s", order_id)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Order processed successfully",
            "order_id": order_id
        })
    }
