import plotly.express as px
import pandas as pd

# Simple function to plot on plotly mapbox library
# Of course we can add support to more frameworks/libraries to plot and map different stuff with different file formats
# For now the function scope is only with COVID info 

def plotly_map_csv(path_to_csv):
    mex_states=pd.read_csv(path_to_csv)
    fig = px.scatter_mapbox(mex_states, lat="lat", lon="long", hover_name="state", hover_data=["confirmed", "recovered", "deaths", "updated"],
                        color_discrete_sequence=["red"], zoom=5, size="confirmed")
    fig.update_layout(mapbox_style="stamen-terrain")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()