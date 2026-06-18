def build_message(ticker, market, fund):

    return f"""
📊 {ticker} - ANÁLISE COMPLETA

💰 PREÇO: R$ {market['price']}
📈 VARIAÇÃO: {market['change']}%

📉 FUNDAMENTOS:

P/L: {fund['pl']}
P/VP: {fund['pvp']}
ROE: {fund['roe']}
ROIC: {fund['roic']}
DY: {fund['dy']}
EV/EBITDA: {fund['ebitda']}
Margem Líquida: {fund['margem_liquida']}

📊 RESUMO:

- Empresa de qualidade média/alta (baseado em ROE e ROIC)
- Avaliação depende do setor
- Usar DY + P/L para decisão de entrada

⚠️ Dados podem ter atraso de alguns minutos
"""
