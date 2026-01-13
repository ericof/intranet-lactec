import type { Content } from '@plone/types';

export interface Area extends Content {
  title: string;
  description: string;
  telefone?: string;
  email: string;
  endereco?: string;
  complemento?: string;
  cidade?: string;
  estado?: string;
  cep?: string;
}
