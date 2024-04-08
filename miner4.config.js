module.exports = {
  apps: [
    {
      name: 'WL1_sn28_hk4',
      script: 'python3',
      args: './neurons/miner.py --netuid 28 --logging.debug --logging.trace --subtensor.network finney --wallet.name wl1 --wallet.hotkey hk4 --axon.port 28114 --model base_lstm.h5 --blacklist.force_validator_permit'
    },
  ],
};
