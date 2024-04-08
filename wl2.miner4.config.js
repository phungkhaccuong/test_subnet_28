module.exports = {
  apps: [
    {
      name: 'WL2_sn28_hk4',
      script: 'python3',
      args: './neurons/miner.py --netuid 28 --logging.debug --subtensor.network finney --wallet.name wl2 --wallet.hotkey hk4 --axon.port 28214 --model base_lstm.h5 --blacklist.force_validator_permit'
    },
  ],
};
