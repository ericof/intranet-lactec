import React from 'react';
import AreaInfo from 'volto-lactec-intranet/components/AreaInfo/AreaInfo';
import type { RelatedItem } from '@plone/types';

interface AreaGridItemProps {
  item: RelatedItem;
}

const AreaGridItem: React.FC<AreaGridItemProps> = (props) => {
  const { item } = props;
  return (
    <div className={`card-summary`}>
      <AreaInfo content={item} icon />
    </div>
  );
};

export default AreaGridItem;
