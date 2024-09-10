from flask import Flask, render_template
import plotly.graph_objects as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[10, 11, 12])])
    graph_html = pio.to_html(fig, full_html=False)
    
    return render_template('index.html', graph=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
