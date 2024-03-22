import bittensor as bt
from predictionnet.api.prediction import PredictionAPI
from predictionnet.api.get_query_axons import get_query_api_axons

from datetime import datetime, timedelta
import time
from pytz import timezone

bt.debug()

# Example usage
async def test_prediction():

    wallet = bt.wallet()

    # Fetch the axons of the available API nodes, or specify UIDs directly
    metagraph = bt.subtensor("finney").metagraph(netuid=28)
    axons = await get_query_api_axons(wallet=wallet, metagraph=metagraph, uids=[89, 96, 97])

    # Store some data!
    ny_timezone = timezone('America/New_York')
    current_time_ny = datetime.now(ny_timezone)
    timestamp = current_time_ny.isoformat()

    bt.logging.info(f"Sending {timestamp} to predict a price.")
    retrieve_handler = PredictionAPI(wallet)
    retrieve_response = await retrieve_handler(
        axons=axons,
        # Arugmnts for the proper synapse
        timestamp=timestamp, 
        timeout=60
    )
    print(retrieve_response)


if __name__ == "__main__":
    import asyncio
    asyncio.run(test_prediction())