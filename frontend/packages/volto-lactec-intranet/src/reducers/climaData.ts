import { GET_CLIMA_DATA } from 'volto-lactec-intranet/constants/ActionTypes';
import type { ClimaData } from 'volto-lactec-intranet/types/clima';

interface ClimaState {
  data: ClimaData | null;
  loaded: boolean;
  loading: boolean;
  error: string | null;
}

interface ClimaAction {
  type: string;
  result?: ClimaData;
  error?: {
    response: {
      error: string;
    };
  };
}

const initialState: ClimaState = {
  data: null,
  loaded: false,
  loading: false,
  error: null,
};

export default function climaData(
  state: ClimaState = initialState,
  action: ClimaAction,
): ClimaState {
  switch (action?.type) {
    case `${GET_CLIMA_DATA}_PENDING`:
      return {
        ...state,
        loaded: false,
        loading: true,
        error: null,
        data: null,
      };
    case `${GET_CLIMA_DATA}_FAIL`:
      return {
        ...state,
        loaded: false,
        loading: false,
        error: action.error?.response?.error || 'Unknown error',
        data: null,
      };
    case `${GET_CLIMA_DATA}_SUCCESS`:
      return {
        ...state,
        loaded: true,
        loading: false,
        error: null,
        data: action.result,
      };
    default:
      return state;
  }
}
