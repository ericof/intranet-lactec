import React from 'react';
import Icon from '@plone/volto/components/theme/Icon/Icon';
import houseSVG from '@plone/volto/icons/home.svg';
import type { RelatedItem } from '@plone/types';
import { Container } from '@plone/components';

interface AreaInfoProps {
  content: RelatedItem;
  icon: boolean;
}
const AreaInfo: React.FC<AreaInfoProps> = (props) => {
  const { content, icon } = props;

  return (
    <Container className="areaInfo" narrow>
      {icon && <Icon name={houseSVG} size="64px" className={'icon listitem'} />}
      <Container className="info" narrow>
        <h2 className="title">{content.title}</h2>
        <p className="description">{content.description}</p>
      </Container>
    </Container>
  );
};

export default AreaInfo;
