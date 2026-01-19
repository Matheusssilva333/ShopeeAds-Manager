import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-[#030712] text-white selection:bg-orange-500/30">
      {/* Navbar */}
      <nav className="fixed w-full z-50 border-b border-white/10 bg-[#030712]/80 backdrop-blur-md">
        <div className="container mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-br from-orange-500 to-red-600 rounded-lg flex items-center justify-center font-bold text-white shadow-lg shadow-orange-500/20">
              S
            </div>
            <span className="text-xl font-bold tracking-tight">ShopeeAds Manager</span>
          </div>
          <div className="flex items-center gap-4">
            <Link href="/login" className="text-sm font-medium text-gray-400 hover:text-white transition-colors">
              Entrar
            </Link>
            <Link href="/register" className="px-4 py-2 bg-gradient-to-r from-orange-500 to-red-500 text-white text-sm font-bold rounded-full hover:shadow-lg hover:shadow-orange-500/20 transition-all">
              Acesso Afiliado
            </Link>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="pt-32 pb-16 px-6 relative overflow-hidden">
        {/* Background Gradients */}
        <div className="absolute top-0 right-0 -translate-y-1/4 translate-x-1/4 w-[500px] h-[500px] bg-orange-600/20 rounded-full blur-[100px]"></div>
        <div className="absolute bottom-0 left-0 translate-y-1/4 -translate-x-1/4 w-[500px] h-[500px] bg-red-600/10 rounded-full blur-[100px]"></div>

        <div className="container mx-auto max-w-5xl text-center relative z-10">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-500/10 border border-orange-500/20 text-orange-400 text-sm font-medium mb-8">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-orange-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-orange-500"></span>
            </span>
            Plataforma #1 para Afiliados Shopee
          </div>

          <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-8">
            Maximize suas Comissões na <br />
            <span className="bg-gradient-to-r from-orange-400 via-orange-500 to-red-500 bg-clip-text text-transparent">
              Shopee
            </span>
          </h1>

          <p className="text-lg md:text-xl text-gray-400 mb-12 max-w-2xl mx-auto leading-relaxed">
            Gerencie seus links de afiliado, rastreie conversões em tempo real e descubra os produtos virais que mais pagam comissão.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-20">
            <button className="px-8 py-4 bg-white text-black rounded-full font-bold text-lg hover:bg-gray-100 transition-all transform hover:-translate-y-1 shadow-[0_0_20px_rgba(255,255,255,0.3)]">
              Começar Grátis
            </button>
            <button className="px-8 py-4 bg-white/5 border border-white/10 rounded-full text-white font-medium hover:bg-white/10 transition-all flex items-center gap-2">
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              Ver Lucros Reais
            </button>
          </div>

          {/* Dashboard Preview - Shopee Style */}
          <div className="relative mx-auto max-w-4xl">
            <div className="absolute -inset-1 bg-gradient-to-r from-orange-500 to-red-600 rounded-2xl blur opacity-20"></div>
            <div className="relative bg-[#0a0a0a] border border-white/10 rounded-xl overflow-hidden shadow-2xl">
              <div className="h-8 bg-white/5 border-b border-white/10 flex items-center px-4 gap-2">
                <div className="w-3 h-3 rounded-full bg-red-500/20"></div>
                <div className="w-3 h-3 rounded-full bg-yellow-500/20"></div>
                <div className="w-3 h-3 rounded-full bg-green-500/20"></div>
              </div>
              <div className="p-8 grid grid-cols-1 md:grid-cols-3 gap-6">
                {/* Metric Card 1 */}
                <div className="bg-white/5 p-6 rounded-lg border border-white/5">
                  <div className="text-gray-400 text-sm mb-2">Comissões Hoje</div>
                  <div className="text-3xl font-bold text-white">R$ 482,90</div>
                  <div className="text-orange-400 text-sm mt-2 flex items-center gap-1">
                    ▲ 45% vs ontem
                  </div>
                </div>
                {/* Metric Card 2 */}
                <div className="bg-white/5 p-6 rounded-lg border border-white/5">
                  <div className="text-gray-400 text-sm mb-2">Cliques no Link</div>
                  <div className="text-3xl font-bold text-white">1.240</div>
                  <div className="text-green-400 text-sm mt-2 flex items-center gap-1">
                    ▲ CTR 3.2%
                  </div>
                </div>
                {/* Metric Card 3 */}
                <div className="bg-white/5 p-6 rounded-lg border border-white/5">
                  <div className="text-gray-400 text-sm mb-2">Conversão</div>
                  <div className="text-3xl font-bold text-white">8.5%</div>
                  <div className="text-green-400 text-sm mt-2 flex items-center gap-1">
                    Excelente
                  </div>
                </div>
                {/* Chart Area */}
                <div className="md:col-span-3 bg-white/5 h-48 rounded-lg border border-white/5 p-6 relative">
                  <div className="absolute top-4 left-6 text-sm text-gray-400">Performance da Semana</div>
                  <div className="flex items-end justify-between h-full pt-6 gap-2">
                    {[30, 45, 35, 60, 55, 80, 65, 90, 75, 85, 95, 100].map((h, i) => (
                      <div key={i} className="w-full bg-orange-500/10 rounded-t-sm relative hover:bg-orange-500/30 transition-colors group">
                        <div style={{ height: `${h}%` }} className="absolute bottom-0 w-full bg-gradient-to-t from-orange-600 to-orange-400 rounded-t-sm group-hover:from-orange-500 group-hover:to-orange-300 transition-all"></div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Features Grid */}
      <section className="py-24 px-6 bg-[#030712]">
        <div className="container mx-auto max-w-5xl">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold mb-4">Tudo para o Afiliado Profissional</h2>
            <p className="text-gray-400">Deixe de ser amador. Tenha dados para escalar suas campanhas.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              { title: "Gerador de Links", desc: "Crie Deep Links oficiais da Shopee em segundos e organize por campanha.", color: "from-orange-500 to-red-500" },
              { title: "Achados Virais", desc: "Descubra produtos que estão vendendo muito no TikTok e Instagram.", color: "from-purple-500 to-pink-500" },
              { title: "Relatório Financeiro", desc: "Centralize seus ganhos e saiba exatamente quando vai receber.", color: "from-green-500 to-emerald-500" }
            ].map((feature, i) => (
              <div key={i} className="group p-1 rounded-2xl bg-gradient-to-b from-white/10 to-transparent hover:from-orange-500/50 transition-all">
                <div className="bg-[#0a0a0a] p-8 rounded-xl h-full relative overflow-hidden">
                  <div className={`absolute top-0 right-0 w-32 h-32 bg-gradient-to-br ${feature.color} blur-[60px] opacity-20 group-hover:opacity-40 transition-opacity`}></div>
                  <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
                  <p className="text-gray-400 leading-relaxed">{feature.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 border-t border-white/10 text-center text-gray-500 text-sm">
        <p>&copy; 2024 ShopeeAds Manager. Não afiliado oficialmente à Shopee.</p>
      </footer>
    </div>
  );
}
