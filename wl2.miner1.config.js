
module.exports = {
  apps: [
    {
      name: 'WL2_sn28_hk1',
      script: 'python3',
      args: './neurons/miner.py --netuid 28 --logging.debug --logging.trace --subtensor.network finney --wallet.name wl2 --wallet.hotkey hk1 --axon.port 28211 --model base_lstm.h5 --blacklist.force_validator_permit'
    },
  ],
};
