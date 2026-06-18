def format_message(ticker, market, fund, score):

    return f"""
📊 {ticker} — ANÁLISE PROFISSIONAL

💰 Preço: R$ {market['price']}
📈 Variação: {market['change']}%

📉 FUNDAMENTOS:
P/L: {fund['pl']}
P/VP: {fund['pvp']}
ROE: {fund['roe']}
ROIC: {fund['roic']}
DY: {fund['dy']}
EV/EBITDA: {fund['ev_ebitda']}

🧠 SCORE: {score}/100

📌 INTERPRETAÇÃO:
{"🟢 FORTE COMPRA" if score > 75 else "🟡 NEUTRO" if score > 50 else "🔴 EVITAR"}

⚠️ Dados podem ter atraso
"""
