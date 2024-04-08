module.exports = {
  apps: [
    {
      name: 'WL1_sn28_hk1',
      script: 'python3',
      args: './neurons/miner.py --netuid 28 --logging.debug --logging.trace --subtensor.network finney --wallet.name wl1 --wallet.hotkey hk1 --axon.port 28111 --model base_lstm.h5 --blacklist.force_validator_permit'
    },
  ],
};
