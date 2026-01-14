import type { ConfigType } from '@plone/registry';
import AreaGridItem from 'volto-lactec-intranet/components/Blocks/Grid/AreaGridItem';

export default function install(config: ConfigType) {
  // Registra Componente para exibir uma Área quando a listagem for de Grade
  // ref: frontend/packages/volto-lactec-intranet/node_modules/@kitconcept/volto-light-theme/src/components/Blocks/Listing/GridTemplate.jsx
  config.registerComponent({
    name: 'GridListingItemTemplate',
    component: AreaGridItem,
    dependencies: 'Area',
  });
  return config;
}
