import type { Meta, StoryObj } from '@storybook/react';
import ClimaView from './DefaultView';

/**
 * Componente de Previsão do Tempo
 *
 */
const meta = {
  title: 'Componentes/Clima',
  component: ClimaView,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
    location: {
      description: 'Localização',
    },
    weather: {
      description: 'Clima atual (ex: sun, rain, cloud)',
    },
    temperature: {
      control: 'text',
      description: 'Temperatura atual',
    },
    measure: {
      control: 'text',
      description: 'Medida do evento (ex: sunrise, sunset)',
    },
    measureValue: {
      control: 'text',
      description:
        'Valor da medida do evento (ex: horário do nascer ou pôr do sol)',
    },
  },
} satisfies Meta<typeof ClimaView>;

export default meta;
type Story = StoryObj<typeof meta>;

/**
 * Exemplo básico mostrando temperatura e pôr do sol em Curitiba
 */
export const Default: Story = {
  args: {
    location: 'Curitiba',
    weather: 'sun',
    temperature: 29.1,
    measure: 'sunset',
    measureValue: '18:00',
  },
};

/**
 * Exemplo mostrando o nascer do sol
 */
export const Sunrise: Story = {
  args: {
    location: 'Curitiba',
    weather: 'sun',
    temperature: 29.1,
    measure: 'sunrise',
    measureValue: '06:00',
  },
};

/**
 * Exemplo com localização diferente
 */
export const OutraLocalizacao: Story = {
  args: {
    location: 'Picos',
    weather: 'sun',
    temperature: 29.1,
    measure: 'sunset',
    measureValue: '18:00',
  },
};

/**
 * Exemplo mostrando o clima nublado
 */
export const ClimaNublado: Story = {
  args: {
    location: 'Curitiba',
    weather: 'cloud',
    temperature: 29.1,
    measure: 'sunset',
    measureValue: '18:00',
  },
};
