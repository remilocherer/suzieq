import dash
import dash_table
import pandas as pd
from suzieq.sqobjects.routes import RoutesObj
from suzieq.sqobjects.lldp import LldpObj

#df = RoutesObj().get(namespace='ibgp-evpn')

df = pd.read_parquet('parquet/routes/')

app = dash.Dash('suzieq')
app.layout = dash_table.DataTable(
    id='Routes',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    editable=True,
    column_selectable="multi",
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    page_action="native")

if __name__ == '__main__':
    app.run_server(debug=True)
