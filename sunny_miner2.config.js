module.exports = {
  apps: [
    {
      name: 'sn28_hk2',
      script: 'python3',
      args: './neurons/miner.py --netuid 28 --logging.debug --logging.trace --subtensor.network finney --wallet.name sunny --wallet.hotkey hk2 --axon.port 28002 --model base_lstm.h5 --blacklist.force_validator_permit --neuron.device cuda:1'
    },
  ],
};
