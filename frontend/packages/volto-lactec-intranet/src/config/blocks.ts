import type { ConfigType } from '@plone/registry';
import type { BlockConfigBase } from '@plone/types';
import AreaGridItem from 'volto-lactec-intranet/components/Blocks/Grid/AreaGridItem';
import ClimaBlockInfo from 'volto-lactec-intranet/components/Blocks/Clima';

declare module '@plone/types' {
  // Altera a interface BlocksConfigData para incluir o bloco de Clima
  export interface BlocksConfigData {
    climaBlock: BlockConfigBase;
  }
}

function installLocalBlocks(config: ConfigType) {
  // Instala o bloco de Clima
  config.blocks.blocksConfig.climaBlock = ClimaBlockInfo;
  return config;
}

export default function install(config: ConfigType) {
  // Registra todos os blocos criados nesse pacote
  installLocalBlocks(config);
  // Registra Componente para exibir uma Área quando a listagem for de Grade
  // ref: frontend/packages/volto-lactec-intranet/node_modules/@kitconcept/volto-light-theme/src/components/Blocks/Listing/GridTemplate.jsx
  config.registerComponent({
    name: 'GridListingItemTemplate',
    component: AreaGridItem,
    dependencies: 'Area',
  });
  return config;
}
