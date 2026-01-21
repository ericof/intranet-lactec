import type { ConfigType } from '@plone/registry';
import installSettings from './config/settings';
import installViews from './config/views';
import installBlocks from './config/blocks';
import installReducers from './config/reducers';

function applyConfig(config: ConfigType) {
  installSettings(config);
  installViews(config);
  installBlocks(config);
  installReducers(config);

  return config;
}

export default applyConfig;
