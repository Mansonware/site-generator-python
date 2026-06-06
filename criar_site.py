#!/usr/bin/env python3
"""
Gerador de site estático com HTML, CSS e JS.
Cria uma estrutura completa com um clique.
"""

import os
import sys

def criar_site(nome_projeto):
    """Cria a estrutura de pastas e arquivos do site."""
    # Pasta do projeto
    if not os.path.exists(nome_projeto):
        os.makedirs(nome_projeto)
    else:
        print(f"A pasta '{nome_projeto}' já existe. Abortando.")
        return False

    # Conteúdo do index.html
    html_content = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>Meu Site</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Bem-vindo ao seu novo site</h1>
        <p>Este site foi gerado automaticamente com Python.</p>
        <button id="btnClique">Clique aqui</button>
        <p id="mensagem"></p>
    </div>
    <script src="script.js"></script>
</body>
</html>'''

    # Conteúdo do style.css
    css_content = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.container {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    max-width: 500px;
    width: 100%;
    text-align: center;
}

h1 {
    color: #333;
    margin-bottom: 1rem;
}

p {
    color: #666;
    margin-bottom: 1.5rem;
    line-height: 1.5;
}

button {
    background: #764ba2;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 1rem;
    border-radius: 30px;
    cursor: pointer;
    transition: transform 0.2s, background 0.2s;
}

button:hover {
    background: #5a3780;
    transform: scale(1.02);
}

button:active {
    transform: scale(0.98);
}

#mensagem {
    margin-top: 1rem;
    font-weight: bold;
    color: #764ba2;
}'''

    # Conteúdo do script.js
    js_content = '''document.getElementById('btnClique').addEventListener('click', function() {
    const mensagem = document.getElementById('mensagem');
    mensagem.textContent = 'Botão clicado! JavaScript funcionando perfeitamente. 🎉';
    mensagem.style.opacity = '0';
    setTimeout(() => { mensagem.style.opacity = '1'; }, 10);
});'''

    # Conteúdo do README do site (opcional)
    site_readme = f'''# {nome_projeto}

Site gerado automaticamente pelo **site-generator-python**.

## Como visualizar

Abra o arquivo `index.html` no seu navegador.

## Estrutura

- `index.html` - estrutura HTML
- `style.css` - estilos CSS responsivos
- `script.js` - interatividade em JavaScript
'''

    # Escrever arquivos
    with open(os.path.join(nome_projeto, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open(os.path.join(nome_projeto, 'style.css'), 'w', encoding='utf-8') as f:
        f.write(css_content)
    with open(os.path.join(nome_projeto, 'script.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    with open(os.path.join(nome_projeto, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(site_readme)

    print(f"✅ Site criado com sucesso na pasta '{nome_projeto}'")
    return True

def main():
    print("===== GERADOR DE SITE EM PYTHON =====")
    if len(sys.argv) > 1:
        nome = sys.argv[1]
    else:
        nome = input("Digite o nome do seu projeto/site: ").strip()
        if not nome:
            print("Nome inválido.")
            return

    if criar_site(nome):
        # Perguntar se quer abrir no navegador
        resposta = input("Abrir o site no navegador agora? (s/N): ").strip().lower()
        if resposta in ('s', 'sim'):
            import webbrowser
            webbrowser.open(f"file://{os.path.abspath(nome)}/index.html")
        print("\n✨ Para personalizar, edite os arquivos dentro da pasta.")

if __name__ == "__main__":
    main()