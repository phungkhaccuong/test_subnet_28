module.exports = {
  apps: [
    {
      name: 'WL3_sn28_hk1',
      script: 'python3',
      args: './neurons/miner.py --netuid 28 --logging.debug --logging.trace --subtensor.network finney --wallet.name wl3 --wallet.hotkey hk1 --axon.port 28311 --model base_lstm.h5 --blacklist.force_validator_permit --neuron.device cuda:1'
    },
  ],
};
