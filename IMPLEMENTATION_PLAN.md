# DataVenda - SaaS de Gestão para Afiliados Shopee
## Plano de Implementação

O objetivo é construir o maior SaaS de gestão de vendas focada exclusivamente em **Afiliados da Shopee**. O sistema permitirá que afiliados rastreiem comissões, gerenciem links de produtos e analisem a performance de suas campanhas em tempo real.

### 1. Arquitetura do Sistema (Mantida & Adaptada)
- **Frontend**: Next.js 14 + Tailwind CSS (Foco em Dashboards de Performance).
- **Backend**: FastAPI (Python) (Processamento de planilhas de comissão e integração via API se disponível).
- **Banco de Dados**: SQLite -> PostgreSQL.

### 2. Roadmap

#### Fase 1: Fundação & Rebranding (Atual)
- [x] Estrutura do Projeto (Monorepo)
- [x] Design System Base
- [ ] Rebranding para identidade Shopee (Laranja/Moderno)
- [ ] Adaptação dos modelos de dados para "Comissões" e "Links"

#### Fase 2: Integração Shopee
- [ ] Autenticação (Shopee Open Platform ou Login Social)
- [ ] Importação de Relatórios (Upload de CSV/Excel da Shopee)
- [ ] Gerador de Links de Afiliado (Deep linking)

#### Fase 3: Dashboard do Afiliado
- [ ] Gráfico de Comissões Diárias
- [ ] Top Produtos Mais Vendidos
- [ ] Calculadora de ROI (Gasto em Ads vs Comissão)

#### Fase 4: Automação
- [ ] Alertas de produtos em alta
- [ ] Disparador de ofertas para Telegram/WhatsApp

### 3. Estrutura de Dados (Conceitual)
- **AffiliateSale**: data, produto, valor_venda, comissao, status (pendente/pago).
- **Campaign**: nome_link, cliques, conversoes.
