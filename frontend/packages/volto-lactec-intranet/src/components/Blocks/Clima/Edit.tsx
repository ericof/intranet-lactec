import React from 'react';
import withBlockExtensions from '@plone/volto/helpers/Extensions/withBlockExtensions';
import ClimaBlockDataForm from 'volto-lactec-intranet/components/Blocks/Clima/Data';
import SidebarPortal from '@plone/volto/components/manage/Sidebar/SidebarPortal';
import type { ClimaBlockData } from 'volto-lactec-intranet/components/Blocks/Clima/Data';
import ClimaBlockView from 'volto-lactec-intranet/components/Blocks/Clima/View';

interface ClimaBlockEditProps {
  data: ClimaBlockData;
  onChangeBlock: (id: string, data: ClimaBlockData) => void;
  block: string;
  selected: boolean;
  [key: string]: any;
}

const ClimaBlockEdit: React.FC<ClimaBlockEditProps> = (props) => {
  const { data, onChangeBlock, block, selected } = props;

  return (
    <>
      <ClimaBlockView {...props} isEditMode={true} />
      <SidebarPortal selected={selected}>
        <ClimaBlockDataForm
          data={data}
          block={block}
          onChangeBlock={onChangeBlock}
        />
      </SidebarPortal>
    </>
  );
};

export default withBlockExtensions(ClimaBlockEdit);
