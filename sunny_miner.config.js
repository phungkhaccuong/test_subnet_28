module.exports = {
  apps: [
    {
      name: 'sn28_hk1',
      script: 'python3',
      args: './neurons/miner.py --netuid 28 --logging.debug --logging.trace --subtensor.network finney --wallet.name sunny --wallet.hotkey hk1 --axon.port 28001 --model base_lstm.h5 --blacklist.force_validator_permit'
    }
  ],
};
