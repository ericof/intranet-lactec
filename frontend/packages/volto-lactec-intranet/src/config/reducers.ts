import type { ConfigType } from '@plone/registry';

import climaData from 'volto-lactec-intranet/reducers/climaData';

export default function install(config: ConfigType) {
  config.addonReducers = {
    ...config.addonReducers,
    climaData,
  };
  return config;
}
