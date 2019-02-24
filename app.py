import dash
import layout


app = dash.Dash(__name__)

app.layout = layout.create_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
