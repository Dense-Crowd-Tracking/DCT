import dash
from dash import html, dcc, dash_table
import base64

app = dash.Dash(__name__)

# Example data: Algorithms, Metrics, Video file paths
data = [
    {"Algorithm": "Kalman Filter", "Precision": 0.85, "Recall": 0.80, "Video": "videos/kalman.mp4"},
    {"Algorithm": "SORT", "Precision": 0.90, "Recall": 0.85, "Video": "videos/sort.mp4"},
    {"Algorithm": "Deep SORT", "Precision": 0.92, "Recall": 0.88, "Video": "videos/deepsort.mp4"}
]

# Function to generate HTML video tag for embedding
def generate_video_html(video_path):
    return html.Video(src=video_path, controls=True, width="250")

# Create Dash DataTable
table = dash_table.DataTable(
    columns=[
        {"name": "Algorithm", "id": "Algorithm"},
        {"name": "Precision", "id": "Precision"},
        {"name": "Recall", "id": "Recall"},
        {"name": "Video", "id": "Video", "presentation": "markdown"}
    ],
    data=[{**row, "Video": generate_video_html(row["Video"])} for row in data],
    style_cell={'textAlign': 'left'},
    style_table={'overflowX': 'auto'}
)

app.layout = html.Div(children=[
    html.H1(children='Tracking Algorithm Comparison'),
    table
])

if __name__ == '__main__':
    app.run_server(debug=True)
