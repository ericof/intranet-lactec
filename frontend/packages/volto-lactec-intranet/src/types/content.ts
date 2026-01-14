import type { Content } from '@plone/types';

export interface Endereco {
  endereco?: string;
  complemento?: string;
  cidade?: string;
  estado?: {
    token: string;
    title: string;
  };
  cep?: string;
}

export interface Contato {
  telefone?: string;
  email?: string;
}

export interface Area extends Content, Endereco, Contato {}

export interface Pessoa extends Content, Endereco, Contato {
  cargo?: {
    token: string;
    title: string;
  };
}
