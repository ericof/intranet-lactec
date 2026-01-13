import type { ConfigType } from '@plone/registry';

export default function install(config: ConfigType) {
  // Language settings
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['pt-br'];
  config.settings.defaultLanguage = 'pt-br';

  return config;
}
