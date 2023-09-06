from dash.dependencies import Input, Output

def get_callbacks(app):
    @app.callback(Output("my-output", "children"),Input("my-input", "value"))
    def callback1(input_value) :
        return f'Output: {input_value}'