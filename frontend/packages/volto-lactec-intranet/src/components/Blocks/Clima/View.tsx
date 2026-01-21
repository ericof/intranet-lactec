import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import withBlockExtensions from '@plone/volto/helpers/Extensions/withBlockExtensions';
import { getClimaData } from 'volto-lactec-intranet/actions/Clima/Clima';
import ClimaView from 'volto-lactec-intranet/components/Blocks/Clima/DefaultView';
import type { ClimaBlockData } from 'volto-lactec-intranet/components/Blocks/Clima/Data';
import cx from 'classnames';

interface ClimaBlockViewProps {
  data: ClimaBlockData;
  className?: string;
  isEditMode?: boolean;
  style?: React.CSSProperties;
}

const ClimaBlockView: React.FC<ClimaBlockViewProps> = ({
  data,
  className,
  style,
  isEditMode,
}) => {
  const dispatch = useDispatch();
  const loaded = useSelector((state: any) => state.climaData?.loaded || false);
  const previsao = useSelector((state: any) => state.climaData?.data || {});
  const events = previsao?.events;
  const sunrise = events?.sunrise ? events.sunrise : '';
  const sunset = events?.sunset ? events.sunset : '';
  const temperature = previsao?.temperature ? previsao.temperature.now : '';
  const weather = previsao?.weather ? previsao.weather : 'cloud';
  const measure = data?.measure ? data.measure : '';
  const location = data?.location ? data.location : 'Terra';

  // Busca os dados quando o bloco é renderizado
  // ou quando a localização é alterada
  useEffect(() => {
    dispatch(getClimaData(location));
  }, [dispatch, location]);

  return (
    <div
      className={cx(
        'block climaBlock',
        `${className}`,
        isEditMode ? 'edit' : '',
      )}
      style={style}
    >
      {loaded ? (
        <ClimaView
          weather={weather}
          temperature={temperature}
          location={location}
          measure={measure}
          measureValue={measure === 'sunrise' ? sunrise : sunset}
        />
      ) : (
        <div className={'loading'}>{'Please wait'}</div>
      )}
    </div>
  );
};

export default withBlockExtensions(ClimaBlockView);
