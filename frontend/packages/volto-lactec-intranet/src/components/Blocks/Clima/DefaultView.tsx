import React from 'react';

interface ClimaViewProps {
  weather: string;
  temperature: number;
  location: string;
  measure: string;
  measureValue: string;
}

const ClimaView: React.FC<ClimaViewProps> = ({
  weather,
  temperature,
  location,
  measure,
  measureValue,
}) => {
  return (
    <div className={'clima-wrapper'}>
      <div className={'clima-card'}>
        <div className={`clima-icon ${weather}`}></div>
        <p className={'temperature'}>{temperature}º</p>
        <p className={'local'}>{location}</p>
        <p className={`evento ${measure}`}>
          <span>{measureValue}</span>
        </p>
      </div>
    </div>
  );
};

export default ClimaView;
