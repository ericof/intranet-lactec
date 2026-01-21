export type ClimaData = {
  '@id': string;
  events: {
    sunrise: string; // format "HH:MM"
    sunset: string; // format "HH:MM"
  };
  temperature: {
    hourly: Record<string, number>; // keys like "00:00", "01:00", etc.
    now: number;
  };
  weather: string; // e.g. "sun"
};
