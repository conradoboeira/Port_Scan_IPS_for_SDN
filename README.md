# IPS para Port Scans numa rede SDN

Modelo de detector de ataques de port scan numa rede SDN baseado no trabalho Lightweight IPS for port scan in OpenFlow SDN networks. Desenvolvido um programa em Python que faz requisições para um controlador em Ryu usando a api ofctl_rest.

Esse trabalho foi desenvolvido para a disciplina de Integradora 2 do curso de Ciência da Computação da PUCRS.

## Depêndencias:
  - Python 3.5.2
  - Ryu 4.32
  - Mininet 2.2.1
  
## Como executar:
  Dentro do diretório src estão os fontes necessários.
  Em um terminal inicie o ryu-manager com o comando:
  '''bash
  ryu-manager sw3.py ryu.app.ofctl_rest
  '''
