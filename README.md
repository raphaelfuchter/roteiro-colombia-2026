# Roteiro gastronômico · Cartagena + San Andrés (nov/2026)

Site: https://raphaelfuchter.github.io/roteiro-colombia-2026/

## Editar
- Refeições: `src/data_M.py` (dia, hora, tipo, nome, cozinha, nota, nº avaliações, fonte, preço 1–4, pratos, dica, foto do local, fotos dos pratos).
- Passeios, dias, extras e Instagram: `src/build_app.py`.
- Layout: `src/app_template.html`.
- Fotos: `src/img/` (nome do arquivo sem `.jpg` nos dados).

Gerar o site: `python3 src/build_app.py` (precisa de Pillow), gerando o `index.html`. Depois faça commit e push.
Se mudar só o conteúdo, troque também `C='roteiro-vN'` em `sw.js`, para limpar o cache antigo do app instalado.
