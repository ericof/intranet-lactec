import React from 'react';
import { getBaseUrl } from '@plone/volto/helpers/Url/Url';
import { Container } from '@plone/components';
import RenderBlocks from '@plone/volto/components/theme/View/RenderBlocks';
import type { Area } from 'volto-lactec-intranet/types/content';
import ContactInfo from 'volto-lactec-intranet/components/ContactInfo/ContactInfo';
import EnderecoInfo from 'volto-lactec-intranet/components/EnderecoInfo/EnderecoInfo';

interface AreaViewProps {
  content: Area;
  location?: {
    pathname: string;
  };
  [key: string]: any;
}

const AreaView: React.FC<AreaViewProps> = (props) => {
  const { content, location } = props;
  const path = getBaseUrl(location?.pathname || '');

  return (
    <Container id="page-document" className="view-wrapper area-view">
      <RenderBlocks {...props} path={path} />
      <ContactInfo content={content} />
      <EnderecoInfo content={content} />
    </Container>
  );
};

export default AreaView;
