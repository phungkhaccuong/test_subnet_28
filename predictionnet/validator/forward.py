# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
import bittensor as bt
# Import Validator Template
import predictionnet
from predictionnet.protocol import Challenge
from predictionnet.validator.reward import get_rewards
from predictionnet.utils.uids import get_random_uids

from datetime import datetime, timedelta
import time
from pytz import timezone


async def forward(self):
    """
    The forward function is called by the validator every time step.
    It is responsible for querying the network and scoring the responses.
    Args:
        self (:obj:`bittensor.neuron.Neuron`): The neuron object which contains all the necessary state for the validator.
    """
    # TODO(developer): Define how the validator selects a miner to query, how often, etc.
    # get_random_uids is an example method, but you can replace it with your own.
    
    # wait for market to be open
    ny_timezone = timezone('America/New_York')
    current_time_ny = datetime.now(ny_timezone)
    bt.logging.info("Current time: ", current_time_ny)
    
    while True:
        current_time = datetime.now(ny_timezone)
        if await self.is_market_open(current_time):
            bt.logging.info("Market is open. Begin processes requests")
            break  # Exit the loop if market is open
        else:
            bt.logging.info("Market is closed. Sleeping for 5 minutes...")
            time.sleep(300)  # Sleep for 5 minutes before checking again

            if datetime.now(ny_timezone) - current_time_ny >= timedelta(hours=1):
                self.set_weights()
                current_time_ny = datetime.now(ny_timezone)
    

    miner_uids = get_random_uids(self, k=min(self.config.neuron.sample_size, self.metagraph.n.item()))

    # Here input data should be gathered to send to the miners
    # TODO(create get_input_data())
    
    current_time_ny = datetime.now(ny_timezone)
    timestamp = current_time_ny.isoformat()

    # Build synapse for request
    # Replace dummy_input with actually defined variables in protocol.py
    # This can be combined with line 49
    synapse = predictionnet.protocol.Challenge(
        timestamp=timestamp,
    )

    # The dendrite client queries the network.
    responses = self.dendrite.query(
        # Send the query to selected miner axons in the network.
        axons=[self.metagraph.axons[uid] for uid in miner_uids],
        # Construct a dummy query. This simply contains a single integer.
        # This can be simplified later to all build from here
        synapse=synapse,
        #synapse=Dummy(dummy_input=self.step),
        # All responses have the deserialize function called on them before returning.
        # You are encouraged to define your own deserialization function.
        
        # Other subnets have this turned to false, I am unsure of whether this should be set to true
        deserialize=False,
    )
    # Log the results for monitoring purposes.
    bt.logging.info(f"Received responses: {responses}")
    # TODO(developer): Define how the validator scores responses.
    # Adjust the scores based on responses from miners.
    
    # query = synapse most likely?
    #rewards = get_rewards(self, query=self.step, responses=responses)
    rewards = get_rewards(self, query=synapse, responses=responses)
    # Potentially will need some  
    bt.logging.info(f"Scored responses: {rewards}")
    # Update the scores based on the rewards. You may want to define your own update_scores function for custom behavior.
    
    # Check base validator file
    self.update_scores(rewards, miner_uids)
