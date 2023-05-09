# Pi Snapshot

Um projeto para capturar imagens usando uma Raspberry Pi e a câmera Picamera2 com resoluções e caminhos de arquivos personalizados.

## Índice

1. [Introdução](#introdução)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação](#instalação)
4. [Uso](#uso)
5. [Contribuição](#contribuição)
6. [Licença](#licença)
7. [Contato](#contato)

## Introdução

Este projeto foi desenvolvido para facilitar a captura de imagens com uma Raspberry Pi e a câmera Picamera2. Ele permite que você personalize a resolução das imagens capturadas e especifique o caminho do arquivo onde as imagens serão salvas.

## Pré-requisitos

- **Raspberry Pi**: Uma placa Raspberry Pi para executar o script e controlar a câmera. Qualquer modelo compatível com a câmera deve funcionar, como o Raspberry Pi 3 ou Raspberry Pi 4;
- **Sistema Operacional**: Raspbian OS (ou Raspberry Pi OS) instalado na Raspberry Pi. Outros sistemas operacionais compatíveis com Raspberry Pi e a câmera Picamera2 também podem funcionar;
- **Câmera**: Uma câmera compatível com a Raspberry Pi, como a câmera Picamera2. Certifique-se de que esteja corretamente conectada à Raspberry Pi;
- **Python 3**: O script foi escrito em Python 3, portanto, você precisará do Python 3 instalado na Raspberry Pi;
- **Dependências do Python**: picamera2.
- 
## Instalação

1. Clone este repositório em sua Raspberry Pi:

```bash
git clone https://github.com/username/piSnapshot.git
```
2. Acesse a pasta do projeto:

```bash
cd piSnapshot
```

## Uso

Você pode executar o script `snap.py` para capturar uma imagem. O script aceita até três argumentos:

1. Caminho do arquivo (opcional, o padrão é ~/imagens/foto_YYYYMMDD_HHMMSS.bmp)
2. Largura da resolução (opcional, o padrão é 256)
3. Altura da resolução (opcional, o padrão é 256)

Exemplo de uso:

```bash
python3 snap.py /caminho/para/a/imagem.bmp 640 480
```
Isso capturará uma imagem com resolução de 640x480 pixels e salvará no caminho especificado.

## Contribuição

Sinta-se à vontade para contribuir com este projeto abrindo problemas, enviando pull requests ou entrando em contato com o mantenedor.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.

## Contato

Se você tiver dúvidas ou quiser discutir mais sobre este projeto, entre em contato com:

- [fpfrimer](https://github.com/fpfrimer)
