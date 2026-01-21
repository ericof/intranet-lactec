import { GET_CLIMA_DATA } from 'volto-lactec-intranet/constants/ActionTypes';

export function getClimaData(location: string) {
  const path = `/@clima?location=${location}`;
  return {
    type: GET_CLIMA_DATA,
    request: {
      op: 'get',
      path: path,
    },
  };
}
