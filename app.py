# FUNCIONALIDADE: Importa o Flask, framework usado para criar o site em Python
from flask import Flask

# FUNCIONALIDADE: Cria a aplicação Flask
app = Flask(__name__)

# FUNCIONALIDADE: Define a rota principal do site
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">

    <head>
        <!-- CONFIGURAÇÃO: Permite usar acentos e caracteres especiais -->
        <meta charset="UTF-8">

        <!-- CONFIGURAÇÃO: Deixa o site responsivo em celular, tablet e computador -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <!-- SEO: Título que aparece na aba do navegador e no Google -->
        <title>Nathana Bernardes | Desenvolvedora</title>

        <style>
            /* ESTILO GERAL: Configuração visual do corpo do site */
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #ffffff;
            }

            /* SEÇÃO: Topo do site */
            header {
                padding: 80px 20px;
                text-align: center;
                background: linear-gradient(135deg, #111827, #1e3a8a);
            }

            /* ESTILO: Logo */
            .logo {
                width: 120px;
                margin-bottom: 20px;
            }

            /* ESTILO: Título principal */
            header h1 {
                font-size: 42px;
                margin-bottom: 20px;
            }

            /* ESTILO: Texto do topo */
            header p {
                font-size: 20px;
                max-width: 800px;
                margin: 0 auto 30px;
                color: #dbeafe;
            }

            /* FUNCIONALIDADE VISUAL: Botões de chamada para ação */
            .botao {
                display: inline-block;
                background: #22c55e;
                color: #ffffff;
                padding: 15px 30px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
            }

            /* ESTILO: Espaçamento padrão das seções */
            section {
                padding: 60px 20px;
                max-width: 1100px;
                margin: auto;
            }

            /* ESTILO: Títulos das seções */
            h2 {
                text-align: center;
                font-size: 32px;
                margin-bottom: 40px;
            }

            /* SEÇÃO: Cards dos serviços */
            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 20px;
            }

            /* ESTILO: Card individual */
            .card {
                background: #1e293b;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            }

            .card h3 {
                color: #93c5fd;
            }

            /* SEÇÃO: Diferenciais */
            .diferenciais {
                text-align: center;
            }

            .diferenciais span {
                display: inline-block;
                background: #1e40af;
                padding: 12px 18px;
                margin: 8px;
                border-radius: 20px;
            }

            /* SEÇÃO: Chamada final */
            .final {
                text-align: center;
                line-height: 1.7;
                font-size: 18px;
            }

            /* SEÇÃO: Portfólio */
            .portfolio {
                padding: 60px 20px;
                max-width: 1100px;
                margin: auto;
            }

            .portfolio h2 {
                text-align: center;
                font-size: 34px;
                margin-bottom: 10px;
            }

            .portfolio-subtitulo {
                text-align: center;
                color: #cbd5e1;
                font-size: 17px;
                margin-bottom: 35px;
            }

            /* FUNCIONALIDADE: Carrossel horizontal */
            .carousel {
                width: 100%;
                overflow: hidden;
            }

            /* FUNCIONALIDADE: Linha que movimenta os cards do carrossel */
            .carousel-track {
                display: flex;
                gap: 16px;
                width: max-content;
                animation: scroll 25s linear infinite;
            }

            /* ESTILO: Card do carrossel */
            .carousel-card {
                flex: 0 0 auto;
                width: 180px;
                background: #1e293b;
                border-radius: 14px;
                overflow: hidden;
                box-shadow: 0 8px 20px rgba(0,0,0,0.30);
                transition: transform 0.3s ease;
            }

            .carousel-card:hover {
                transform: translateY(-6px);
            }

            .carousel-card img {
                width: 100%;
                height: 120px;
                object-fit: cover;
            }

            .carousel-card h3 {
                text-align: center;
                padding: 10px;
                color: #93c5fd;
                font-size: 14px;
            }

            /* FUNCIONALIDADE: Animação automática do carrossel */
            @keyframes scroll {
                0% {
                    transform: translateX(0);
                }
                100% {
                    transform: translateX(-50%);
                }
            }

            /* SEÇÃO: Rodapé */
            footer {
                text-align: center;
                padding: 25px;
                background: #020617;
                color: #94a3b8;

            }
            
            /* ===== SERVIÇOS ===== */
.servicos {
    padding: 60px 20px;
    max-width: 1100px;
    margin: auto;
}

.servicos h2 {
    text-align: center;
    font-size: 34px;
    margin-bottom: 10px;
}

.servicos-subtitulo {
    text-align: center;
    color: #cbd5e1;
    font-size: 17px;
    margin-bottom: 35px;
}

/* GRID IGUAL AO PORTFÓLIO */
.servicos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

/* CARD MODERNO */
.servico-card {
    background: #1e293b;
    border-radius: 14px;
    padding: 25px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.30);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.servico-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 28px rgba(0,0,0,0.40);
}

.servico-card h3 {
    color: #93c5fd;
    margin-bottom: 10px;
}

.servico-card p {
    color: #e2e8f0;
    line-height: 1.6;
}
        </style>
    </head>

    <body>

        <!-- SEÇÃO: Topo do site -->
        <header>
            <!-- LOGO: Imagem da marca -->
            <img src="/static/logo.png" alt="Logo Nathana Bernardes" class="logo">

            <h1>Criação de Sites Profissionais <br> e Desenvolvimento Web</h1>

            <p>
                Transformo idéias em soluções digitais e Funcionais. Ajudo pessoas, negócios e empresas a terem presença digital com
                sites, landing pages, sistemas e aplicações mobile.
            </p>

            <a class="botao" href="https://wa.me/5551981686819" target="_blank">
                Solicitar orçamento pelo WhatsApp
            </a>
        </header>

        <!-- SEÇÃO: Serviços -->
        <section>
            <h2>Serviços</h2>

            <div class="cards">
                <div class="card">
                    <h3>Criação de Sites Profissionais</h3>
                    <p>Sites modernos, rápidos e adaptados para celular, computador e tablet.</p>
                </div>

                <div class="card">
                    <h3>Landing Pages</h3>
                    <p>Páginas estratégicas para divulgação de serviços, captação de clientes e campanhas.</p>
                </div>

                <div class="card">
                    <h3>Aplicações Web</h3>
                    <p>Soluções sob medida para organizar processos, cadastros, informações e rotinas do negócio.</p>
                </div>

                <div class="card">
                    <h3>Desenvolvimento Mobile</h3>
                    <p>Aplicativos funcionais para Android/iOS, conforme a necessidade do projeto.</p>
                </div>
            </div>
        </section>

        <!-- SEÇÃO: Portfólio -->
        <section class="portfolio">
            <h2>Portfólio</h2>

            <p class="portfolio-subtitulo">
                Catálogo de modelos de sites, lojas, plataformas e aplicativos.
            </p>

            <!-- FUNCIONALIDADE: Carrossel de imagens -->
            <div class="carousel">
                <div class="carousel-track">

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80" alt="Site profissional">
                        <h3>Sites</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=600&q=80" alt="Loja virtual">
                        <h3>Lojas</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80" alt="Plataforma web">
                        <h3>Plataformas</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=600&q=80" alt="Aplicativo mobile">
                        <h3>Apps</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=600&q=80" alt="Sistema web">
                        <h3>Sistemas</h3>
                    </div>

                    <!-- Repetição dos cards para o carrossel ficar contínuo -->
                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80" alt="Site profissional">
                        <h3>Sites</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=600&q=80" alt="Loja virtual">
                        <h3>Lojas</h3>
                    </div>

                    <div class="carousel-card">
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80" alt="Plataforma web">
                        <h3>Plataformas</h3>
                    </div>

                </div>
            </div>
        </section>

        <!-- SEÇÃO: Diferenciais -->
        <section class="diferenciais">
            <h2>Diferenciais</h2>

            <span>Design responsivo</span>
            <span>Atendimento personalizado</span>
            <span>Sites com foco em conversão</span>
            <span>Entrega organizada</span>
            <span>Comunicação clara</span>
        </section>

        <!-- SEÇÃO: Chamada final -->
        <section class="final">
            <h2>Quer tirar sua ideia do papel?</h2>

            <p>
                Vamos conversar sobre o seu projeto e encontrar a melhor solução digital para você.
            </p>

            <a class="botao" href="https://wa.me/5551981686819" target="_blank">
                Quero meu site ou aplicação
            </a>
        </section>

        <!-- SEÇÃO: Rodapé -->
        <footer>
            <p>© 2026 Nathana Bernardes | Desenvolvedora Web e Mobile</p>
        </footer>

    </body>
    </html>
    """

# FUNCIONALIDADE: Executa o servidor Flask localmente
if __name__ == "__main__":
    app.run(debug=True)