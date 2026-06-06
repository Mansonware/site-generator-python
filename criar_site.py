#!/usr/bin/env python3
"""
Gerador de Sites Profissional com Python
Com suporte total para Termux (Android) e todos os sistemas
"""

import os
import sys
import subprocess
import platform
from datetime import datetime

def detectar_ambiente():
    """Detecta se está rodando no Termux (Android) ou outro sistema."""
    sistema = platform.system().lower()
    is_termux = "com.termux" in os.environ.get("PREFIX", "") or "ANDROID_ROOT" in os.environ
    is_android = is_termux or "android" in sistema.lower()
    
    return {
        "sistema": sistema,
        "is_termux": is_termux,
        "is_android": is_android,
        "is_linux": sistema == "linux" and not is_termux,
        "is_mac": sistema == "darwin",
        "is_windows": sistema == "windows"
    }

def abrir_navegador(caminho_html):
    """Abre o navegador de forma compatível com Termux e outros sistemas."""
    caminho_absoluto = os.path.abspath(caminho_html)
    ambiente = detectar_ambiente()
    
    print(f"\n🌐 Tentando abrir: {caminho_absoluto}")
    
    if ambiente["is_termux"]:
        print("📱 Detectado Termux (Android)")
        
        try:
            subprocess.run(["xdg-open", caminho_absoluto], timeout=3)
            print("✅ Site aberto no navegador Android!")
            return True
        except:
            pass
        
        print("\n⚠️ Não foi possível abrir automaticamente.")
        print("📌 Para visualizar o site:")
        print(f"   1. Acesse pelo gerenciador de arquivos: {caminho_absoluto}")
        print("   2. Ou use um servidor HTTP:")
        print(f"      cd {os.path.dirname(caminho_absoluto)}")
        print("      python -m http.server 8000")
        print("      Então abra no navegador: http://localhost:8000")
        
        resposta = input("\n🔧 Iniciar servidor HTTP local para visualizar? (s/N): ").strip().lower()
        if resposta in ('s', 'sim'):
            print("\n🚀 Iniciando servidor...")
            print("📱 Abra no navegador: http://localhost:8000")
            print("⚠️ Pressione Ctrl+C para parar o servidor\n")
            os.chdir(os.path.dirname(caminho_absoluto))
            try:
                subprocess.run([sys.executable, "-m", "http.server", "8000"])
            except KeyboardInterrupt:
                print("\n✅ Servidor encerrado.")
            return True
        return False
    
    if ambiente["is_linux"]:
        try:
            subprocess.run(["xdg-open", caminho_absoluto])
            print("✅ Site aberto no navegador padrão!")
            return True
        except:
            pass
    
    if ambiente["is_mac"]:
        try:
            subprocess.run(["open", caminho_absoluto])
            print("✅ Site aberto no navegador padrão!")
            return True
        except:
            pass
    
    if ambiente["is_windows"]:
        try:
            os.startfile(caminho_absoluto)
            print("✅ Site aberto no navegador padrão!")
            return True
        except:
            pass
    
    print(f"\n📁 Abra manualmente o arquivo: {caminho_absoluto}")
    return False

def perguntar_config():
    """Coleta configurações do site interativamente."""
    print("\n" + "="*50)
    print("🚀 GERADOR DE SITES PROFISSIONAL")
    print("="*50)
    
    config = {}
    config['nome'] = input("\n📁 Nome do projeto: ").strip()
    if not config['nome']:
        config['nome'] = "meu-site"
    
    config['titulo'] = input("🏷️  Título do site: ").strip()
    if not config['titulo']:
        config['titulo'] = "Meu Site Profissional"
    
    config['subtitulo'] = input("📝 Subtítulo (opcional): ").strip()
    
    print("\n🎨 Escolha um tema:")
    print("1. 🌙 Escuro (Dark) - Moderno")
    print("2. ☀️ Claro (Light) - Clean")
    print("3. 💜 Roxo (Purple) - Criativo")
    print("4. 💚 Verde (Green) - Natureza")
    tema_opcao = input("Digite o número (1-4): ").strip()
    
    temas = {
        "1": "dark",
        "2": "light", 
        "3": "purple",
        "4": "green"
    }
    config['tema'] = temas.get(tema_opcao, "dark")
    
    print("\n📱 Quais seções incluir?")
    print("1. 📖 Sobre")
    print("2. 🛠️ Serviços/Produtos")
    print("3. 📞 Contato")
    print("4. 📧 Newsletter")
    print("5. 💬 Depoimentos")
    print("6. 🎯 Todas")
    secoes = input("Digite os números separados por vírgula (ex: 1,2,3): ").strip()
    config['secoes'] = [s.strip() for s in secoes.split(",")] if secoes else ["1", "2", "3"]
    
    config['ano'] = datetime.now().year
    
    print("\n" + "="*50)
    print("📋 RESUMO DO SITE:")
    print(f"   Nome: {config['nome']}")
    print(f"   Título: {config['titulo']}")
    print(f"   Tema: {config['tema']}")
    print(f"   Seções: {', '.join(config['secoes'])}")
    print("="*50)
    
    confirmar = input("\n✅ Confirmar criação? (s/N): ").strip().lower()
    if confirmar not in ('s', 'sim'):
        print("❌ Criação cancelada.")
        sys.exit(0)
    
    return config

def gerar_html(config):
    """Gera o HTML completo com todas as seções."""
    
    temas_css = {
        "dark": """
            :root {
                --bg-primary: #0f0f1f;
                --bg-secondary: #1a1a2e;
                --text-primary: #ffffff;
                --text-secondary: #b8b8d0;
                --accent: #7c3aed;
                --accent-hover: #8b5cf6;
                --card-bg: #16213e;
            }""",
        "light": """
            :root {
                --bg-primary: #f8fafc;
                --bg-secondary: #ffffff;
                --text-primary: #0f172a;
                --text-secondary: #475569;
                --accent: #3b82f6;
                --accent-hover: #2563eb;
                --card-bg: #ffffff;
            }""",
        "purple": """
            :root {
                --bg-primary: #1e1b4b;
                --bg-secondary: #2e2b5e;
                --text-primary: #f8fafc;
                --text-secondary: #c4b5fd;
                --accent: #a78bfa;
                --accent-hover: #c4b5fd;
                --card-bg: #312e81;
            }""",
        "green": """
            :root {
                --bg-primary: #064e3b;
                --bg-secondary: #047857;
                --text-primary: #f0fdf4;
                --text-secondary: #bbf7d0;
                --accent: #22c55e;
                --accent-hover: #4ade80;
                --card-bg: #065f46;
            }"""
    }
    
    secoes_html = ""
    
    if "1" in config['secoes'] or "6" in config['secoes']:
        secoes_html += """
        <section id="sobre" class="section">
            <div class="container">
                <h2>Sobre Nós</h2>
                <p>Somos uma equipe apaixonada por criar soluções digitais incríveis. Nosso objetivo é transformar ideias em realidade através da tecnologia e criatividade.</p>
                <p>Trabalhamos com as melhores práticas e tecnologias modernas para entregar produtos de alta qualidade.</p>
            </div>
        </section>"""
    
    if "2" in config['secoes'] or "6" in config['secoes']:
        secoes_html += """
        <section id="servicos" class="section">
            <div class="container">
                <h2>Nossos Serviços</h2>
                <div class="cards">
                    <div class="card">
                        <div class="card-icon">🚀</div>
                        <h3>Desenvolvimento Web</h3>
                        <p>Sites modernos, responsivos e otimizados para SEO.</p>
                    </div>
                    <div class="card">
                        <div class="card-icon">📱</div>
                        <h3>Apps Mobile</h3>
                        <p>Aplicativos nativos e híbridos para iOS e Android.</p>
                    </div>
                    <div class="card">
                        <div class="card-icon">🎨</div>
                        <h3>UI/UX Design</h3>
                        <p>Designs intuitivos e experiências memoráveis.</p>
                    </div>
                </div>
            </div>
        </section>"""
    
    if "3" in config['secoes'] or "6" in config['secoes']:
        secoes_html += """
        <section id="contato" class="section">
            <div class="container">
                <h2>Contato</h2>
                <form id="contactForm" class="contact-form">
                    <input type="text" placeholder="Seu nome" required>
                    <input type="email" placeholder="Seu e-mail" required>
                    <textarea rows="4" placeholder="Sua mensagem" required></textarea>
                    <button type="submit">Enviar Mensagem</button>
                </form>
            </div>
        </section>"""
    
    if "4" in config['secoes'] or "6" in config['secoes']:
        secoes_html += """
        <section class="section" style="background: var(--bg-secondary);">
            <div class="container">
                <h2>Newsletter</h2>
                <p>Receba novidades e conteúdos exclusivos</p>
                <form id="newsletterForm" style="display: flex; gap: 1rem; max-width: 500px; margin: 0 auto; flex-wrap: wrap;">
                    <input type="email" placeholder="Seu melhor e-mail" required style="flex: 1; min-width: 200px;">
                    <button type="submit">Inscrever</button>
                </form>
            </div>
        </section>"""
    
    if "5" in config['secoes'] or "6" in config['secoes']:
        secoes_html += """
        <section class="section">
            <div class="container">
                <h2>Depoimentos</h2>
                <div class="cards">
                    <div class="card">
                        <p>"Excelente trabalho! Superou todas as expectativas."</p>
                        <h3>- João Silva</h3>
                        <span>CEO Empresa X</span>
                    </div>
                    <div class="card">
                        <p>"Time muito profissional e atencioso. Recomendo!"</p>
                        <h3>- Maria Santos</h3>
                        <span>CTO Startup Y</span>
                    </div>
                </div>
            </div>
        </section>"""
    
    html = f'''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>{config['titulo']}</title>
    <style>
        {temas_css[config['tema']]}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            scroll-behavior: smooth;
        }}
        
        .header {{
            background: var(--bg-secondary);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .nav {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }}
        
        .logo {{
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent);
        }}
        
        .nav-links {{
            display: flex;
            gap: 2rem;
            flex-wrap: wrap;
        }}
        
        .nav-links a {{
            color: var(--text-primary);
            text-decoration: none;
            transition: color 0.3s;
        }}
        
        .nav-links a:hover {{
            color: var(--accent);
        }}
        
        .hero {{
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 6rem 2rem 4rem;
            background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
        }}
        
        .hero h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: fadeInUp 1s ease;
        }}
        
        .hero p {{
            font-size: 1.2rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
            animation: fadeInUp 1s ease 0.2s both;
        }}
        
        .btn {{
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 12px 30px;
            border-radius: 30px;
            text-decoration: none;
            transition: transform 0.3s, background 0.3s;
            animation: fadeInUp 1s ease 0.4s both;
        }}
        
        .btn:hover {{
            background: var(--accent-hover);
            transform: translateY(-2px);
        }}
        
        .section {{
            padding: 5rem 2rem;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        h2 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--accent);
        }}
        
        .cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }}
        
        .card {{
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .card-icon {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}
        
        .contact-form {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
            max-width: 600px;
            margin: 0 auto;
        }}
        
        input, textarea {{
            padding: 12px;
            border: 1px solid var(--text-secondary);
            background: var(--bg-primary);
            color: var(--text-primary);
            border-radius: 8px;
            font-size: 1rem;
        }}
        
        button {{
            background: var(--accent);
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.3s;
        }}
        
        button:hover {{
            background: var(--accent-hover);
        }}
        
        .footer {{
            background: var(--bg-secondary);
            text-align: center;
            padding: 2rem;
            margin-top: 2rem;
        }}
        
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}
            
            .nav {{
                flex-direction: column;
                text-align: center;
            }}
            
            .nav-links {{
                justify-content: center;
            }}
            
            h2 {{
                font-size: 1.8rem;
            }}
            
            .section {{
                padding: 3rem 1rem;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <nav class="nav">
            <div class="logo">{config['titulo'][:20]}</div>
            <div class="nav-links">
                <a href="#home">Início</a>
                <a href="#sobre">Sobre</a>
                <a href="#servicos">Serviços</a>
                <a href="#contato">Contato</a>
            </div>
        </nav>
    </header>
    
    <section id="home" class="hero">
        <div class="container">
            <h1>{config['titulo']}</h1>
            {f'<p>{config["subtitulo"]}</p>' if config['subtitulo'] else '<p>Bem-vindo ao nosso site profissional</p>'}
            <a href="#contato" class="btn">Vamos Conversar</a>
        </div>
    </section>
    
    {secoes_html}
    
    <footer class="footer">
        <p>&copy; {config['ano']} {config['titulo']}. Todos os direitos reservados.</p>
        <p>Criado com 🐍 Python Site Generator</p>
    </footer>
    
    <script>
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if(target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
        
        const contactForm = document.getElementById('contactForm');
        if(contactForm) {{
            contactForm.addEventListener('submit', (e) => {{
                e.preventDefault();
                alert('Mensagem enviada! Entraremos em contato em breve.');
                contactForm.reset();
            }});
        }}
        
        const newsletterForm = document.getElementById('newsletterForm');
        if(newsletterForm) {{
            newsletterForm.addEventListener('submit', (e) => {{
                e.preventDefault();
                alert('Inscrição realizada com sucesso!');
                newsletterForm.reset();
            }});
        }}
        
        const observerOptions = {{
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        }};
        
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if(entry.isIntersecting) {{
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }}
            }});
        }}, observerOptions);
        
        document.querySelectorAll('.section, .card').forEach(el => {{
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'all 0.6s ease-out';
            observer.observe(el);
        }});
    </script>
</body>
</html>'''
    
    return html

def criar_site(config):
    """Cria a estrutura completa do site."""
    nome = config['nome']
    
    if os.path.exists(nome):
        print(f"❌ Pasta '{nome}' já existe.")
        return False
    
    os.makedirs(nome)
    
    html_content = gerar_html(config)
    caminho_html = os.path.join(nome, 'index.html')
    
    with open(caminho_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    readme_content = f"""# {config['titulo']}

Site gerado automaticamente com Python Site Generator.

## Como visualizar
Abra o arquivo `index.html` no seu navegador.

## Personalização
Edite os arquivos HTML, CSS e JavaScript conforme sua necessidade.

---
Criado em {datetime.now().strftime('%d/%m/%Y')}
"""
    
    with open(os.path.join(nome, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"\n✅ Site criado com sucesso em: '{nome}/'")
    return caminho_html

def main():
    ambiente = detectar_ambiente()
    
    if ambiente["is_termux"]:
        print("\n📱 === MODO TERMUX (ANDROID) DETECTADO ===")
        print("🎯 Visualização otimizada para celular!")
    
    config = perguntar_config()
    
    print(f"\n🎨 Gerando site com tema: {config['tema']}...")
    
    caminho_html = criar_site(config)
    
    if caminho_html:
  