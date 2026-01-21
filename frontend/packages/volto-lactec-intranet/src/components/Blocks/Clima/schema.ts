import { defineMessages } from 'react-intl';
import type { BlockSchemaProps } from '@plone/types';

const messages = defineMessages({
  climaBlock: {
    id: 'Previsão do Tempo',
    defaultMessage: 'Previsão do Tempo',
  },
  sunrise: {
    id: 'Nascer do Sol',
    defaultMessage: 'Nascer do Sol',
  },
  sunset: {
    id: 'Por do Sol',
    defaultMessage: 'Por do Sol',
  },
  location: {
    id: 'Local',
    defaultMessage: 'Local',
  },
  locationHelp: {
    id: 'Nome do local a ser exibido',
    defaultMessage: 'Nome do local a ser exibido',
  },
  measure: {
    id: 'Medida',
    defaultMessage: 'Medida',
  },
  measureHelp: {
    id: 'O que será exibido no bloco',
    defaultMessage: 'O que será exibido no bloco',
  },
});

export const ClimaSchema = (props: BlockSchemaProps): any => {
  const { intl } = props;

  const availableMeasures = [
    ['sunrise', intl.formatMessage(messages.sunrise)],
    ['sunset', intl.formatMessage(messages.sunset)],
  ];

  const defaultMeasure = 'sunset';

  return {
    title: intl.formatMessage(messages.climaBlock),
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['location', 'measure'],
      },
    ],
    properties: {
      location: {
        title: intl.formatMessage(messages.location),
        description: intl.formatMessage(messages.locationHelp),
        widget: 'text',
      },
      measure: {
        title: intl.formatMessage(messages.measure),
        description: intl.formatMessage(messages.measureHelp),
        choices: availableMeasures,
        default: defaultMeasure,
      },
    },
    required: ['location', 'measure'],
  };
};
