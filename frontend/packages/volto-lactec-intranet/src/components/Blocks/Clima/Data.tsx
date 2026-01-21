import React from 'react';
import BlockDataForm from '@plone/volto/components/manage/Form/BlockDataForm';
import { useIntl } from 'react-intl';
import { ClimaSchema } from 'volto-lactec-intranet/components/Blocks/Clima/schema';

export interface ClimaBlockData {
  location?: string;
  measure?: string;
}

interface ClimaBlockDataProps {
  data: ClimaBlockData;
  block: string;
  onChangeBlock: (id: string, data: ClimaBlockData) => void;
  [key: string]: any;
}

const ClimaBlockDataForm: React.FC<ClimaBlockDataProps> = (props) => {
  const { data, block, onChangeBlock } = props;
  const intl = useIntl();
  const schema = ClimaSchema({ ...props, intl });

  const handleFieldChange = (id: string, value: any) => {
    onChangeBlock(block, {
      ...data,
      [id]: value,
    });
  };

  return (
    <BlockDataForm
      schema={schema}
      title={schema.title}
      onChangeField={handleFieldChange}
      formData={data}
      block={block}
    />
  );
};

export default ClimaBlockDataForm;
