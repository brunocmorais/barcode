# Barcode Generator

API REST para geração de códigos de barras em Python. Um serviço Flask que gera imagens de códigos de barras em formato BMP ou base64, com suporte a múltiplos tipos de código de barras.

## Funcionalidades

- **Múltiplos tipos**: Code 25, Code 39, EAN-13, EAN-8, UPC-A, Code 128C
- **Formatos de saída**: BMP binário ou base64
- **Compressão**: Suporta PackBits (apenas com base64)
- **Opções configuráveis**: escala, altura, zona silenciosa, dígito de verificação

## Tipos Suportados

- Code 25
- Code 39
- EAN-13
- EAN-8
- UPC-A
- Code 128C

## Uso

### GET

```bash
# Retorna imagem BMP
GET /image/{type}/{string}

# Retorna base64
GET /base64/{type}/{string}
```

### POST

```bash
POST /
Content-Type: application/json

{
  "string": "5901234123457",
  "type": "ean13",
  "base64": false,
  "compress": false,
  "verification_digit": false,
  "scale_factor": 3,
  "height": 80,
  "quiet_zone_size": 10
}
```

## Parâmetros

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|------------|
| string | string | obrigatório | Dados a codificar |
| type | string | obrigatório | Tipo de código de barras |
| base64 | boolean | false | Retornar base64 ao invés de BMP |
| compress | boolean | false | Comprimir com PackBits (requer base64) |
| verification_digit | boolean | false | Adicionar dígito de verificação |
| scale_factor | integer | 3 | Fator de escala |
| height | integer | 80 | Altura da imagem |
| quiet_zone_size | integer | 10 | Tamanho da zona silenciosa |

## Executar

```bash
python main.py
```

O servidor inicia em `http://localhost:8080`.

## Docker

```bash
docker-compose up
```
