# -*- coding: utf-8 -*-
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask import Flask, Response
from flask_talisman import Talisman
from werkzeug.middleware.proxy_fix import ProxyFix
from bots import get_bot_metrics

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.DARKLY])
Talisman(server, force_https=False)
server.wsgi_app = ProxyFix(server.wsgi_app, x_for=1, x_proto=1)

app.layout = dbc.Container([
    html.H2("🧠 EagleNet Bot Telemetry Grid", className="text-warning text-center mb-4"),
    dcc.Interval(id="interval", interval=5000, n_intervals=0),
    dbc.Table(id="bot-table", bordered=True, striped=True, hover=True, responsive=True)
], fluid=True)

@app.callback(
    dash.Output("bot-table", "children"),
    dash.Input("interval", "n_intervals")
)
def update_bot_table(n):
    bots = get_bot_metrics()
    header = html.Thead(html.Tr([
        html.Th("Bot ID"), html.Th("Strategy"), html.Th("Profit (ETH)"),
        html.Th("Latency (ms)"), html.Th("Wallet Balance (USDT)"), html.Th("Withdrawal Mode")
    ]))
    rows = [html.Tr([
        html.Td(bot["bot_id"]),
        html.Td(bot["strategy"]),
        html.Td(f'{bot["profit_eth"]}'),
        html.Td(f'{bot["latency_ms"]}'),
        html.Td(f'{bot["wallet_balance"]}'),
        html.Td(bot["withdrawal_mode"])
    ]) for bot in bots]
    body = html.Tbody(rows)
    return [header, body]

@server.route("/health")
def health_check():
    return Response("OPERATIONAL", status=200)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080, debug=True)
