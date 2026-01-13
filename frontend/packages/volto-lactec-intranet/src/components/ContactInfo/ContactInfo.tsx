import React from 'react';
import { Container } from '@plone/components';
import type { Area } from 'volto-lactec-intranet/types/content';

interface ContactInfoProps {
  content: Area;
}

const ContactInfo: React.FC<ContactInfoProps> = ({ content }) => {
  const { telefone, email } = content;

  return (
    <Container narrow className="contato">
      <Container className="telefone">
        <span className="label">Telefone</span>:{' '}
        <span className="value">{telefone}</span>
      </Container>
      <Container className="email">
        <span className="label">E-mail</span>:{' '}
        <span className="value">
          <a href={`mailto:${email}`}>{email}</a>
        </span>
      </Container>
    </Container>
  );
};

export default ContactInfo;
