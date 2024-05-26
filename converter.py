import csv

def read_preferences(pref_file_path):
    preferences = {}
    with open(pref_file_path, 'r', encoding='utf-8') as pref_file:
        mode = None
        for line in pref_file:
            stripped_line = line.strip()
            if stripped_line.startswith('default:{'):
                mode = 'default'
                continue
            elif stripped_line.startswith('user:{'):
                mode = 'user'
                continue
            elif stripped_line == '}':
                mode = None
                continue
            if mode and stripped_line and not stripped_line.startswith('//'):
                key, value = stripped_line.split(':')
                preferences[key.strip()] = value.strip().rstrip(';')
    return preferences

def csv_to_html(csv_file_path, html_file_path, preferences):
    default_preferences = {
        "top_row_color": "#F8D566",
        "top_column_color": "#E4E2DF",
        "alt_color_1": "#FFFBF0",
        "alt_color_2": "#EFEBE3",
        "background_color": "#FFFBF0",
        "cell_font_name": "Avenir Next",
        "cell_text_color": "black",
        "anti_alternating": "false",
        "border_thickness": "1px",
        "border_color": "black",
        "title": "true",
        "title_text": "CSV Data",
        "title_color": "black"
    }
    
    color_themes = {
    "dracula": {
        "top_row_color": "#282A36",
        "top_column_color": "#282A36",
        "alt_color_1": "#6272A4",
        "alt_color_2": "#44475A",
        "background_color": "#282A36",
        "border_color": "#8BE9FD",
        "title_color": "#F8F8F2",
        "cell_text_color": "#F8F8F2"
    },
    "light": {
        "top_row_color": "#E0E0E0",
        "top_column_color": "#FFFFFF",
        "alt_color_1": "#F0F0F0",
        "alt_color_2": "#FFFFFF",
        "background_color": "#FFFFFF",
        "border_color": "#CCCCCC",
        "title_color": "#000000",
        "cell_text_color": "#000000"
    },
    "solarized": {
        "top_row_color": "#002B36",
        "top_column_color": "#073642",
        "alt_color_1": "#586e75",
        "alt_color_2": "#657b83",
        "background_color": "#FDF6E3",
        "border_color": "#93A1A1",
        "title_color": "#657B83",
        "cell_text_color": "#FDF6E3"
    },
    "gruvbox": {
        "top_row_color": "#282828",
        "top_column_color": "#282828",
        "alt_color_1": "#3C3836",
        "alt_color_2": "#504945",
        "background_color": "#282828",
        "border_color": "#EBDBB2",
        "title_color": "#EBDBB2",
        "cell_text_color": "#EBDBB2"
    },
    "monokai": {
        "top_row_color": "#272822",
        "top_column_color": "#272822",
        "alt_color_1": "#49483E",
        "alt_color_2": "#3E3D32",
        "background_color": "#272822",
        "border_color": "#F8F8F0",
        "title_color": "#F8F8F0",
        "cell_text_color": "#F8F8F0"
    },
    "nord": {
        "top_row_color": "#2E3440",
        "top_column_color": "#2E3440",
        "alt_color_1": "#3B4252",
        "alt_color_2": "#434C5E",
        "background_color": "#2E3440",
        "border_color": "#D8DEE9",
        "title_color": "#D8DEE9",
        "cell_text_color": "#D8DEE9"
    },
    "tokyo-night": {
        "top_row_color": "#1A1B26",
        "top_column_color": "#1A1B26",
        "alt_color_1": "#24283B",
        "alt_color_2": "#1F2335",
        "background_color": "#1A1B26",
        "border_color": "#C0CAF5",
        "title_color": "#C0CAF5",
        "cell_text_color": "#C0CAF5"
    },
    "oceanic-next": {
        "top_row_color": "#1B2B34",
        "top_column_color": "#343D46",
        "alt_color_1": "#4F5B66",
        "alt_color_2": "#65737E",
        "background_color": "#1B2B34",
        "border_color": "#A7ADBA",
        "title_color": "#C0C5CE",
        "cell_text_color": "#C0C5CE"
    },
    "palenight": {
        "top_row_color": "#292D3E",
        "top_column_color": "#444267",
        "alt_color_1": "#32374D",
        "alt_color_2": "#464B5D",
        "background_color": "#292D3E",
        "border_color": "#959DCB",
        "title_color": "#959DCB",
        "cell_text_color": "#959DCB"
    },
    "ayu-mirage": {
        "top_row_color": "#17191E",
        "top_column_color": "#242B38",
        "alt_color_1": "#1F2430",
        "alt_color_2": "#343D46",
        "background_color": "#17191E",
        "border_color": "#6C7680",
        "title_color": "#D9D7CE",
        "cell_text_color": "#D9D7CE"
    },
    "material": {
        "top_row_color": "#263238",
        "top_column_color": "#37474F",
        "alt_color_1": "#455A64",
        "alt_color_2": "#546E7A",
        "background_color": "#263238",
        "border_color": "#B0BEC5",
        "title_color": "#ECEFF1",
        "cell_text_color": "#ECEFF1"
    },
    "tomorrow-night": {
        "top_row_color": "#1D1F21",
        "top_column_color": "#282A2E",
        "alt_color_1": "#373B41",
        "alt_color_2": "#4D4D4C",
        "background_color": "#1D1F21",
        "border_color": "#C5C8C6",
        "title_color": "#C5C8C6",
        "cell_text_color": "#C5C8C6"
    }
}



    settings = {**default_preferences, **preferences}

    selected_theme = settings.get("colortheme")
    if selected_theme and selected_theme in color_themes:
        theme_settings = color_themes[selected_theme]
        settings = {**settings, **theme_settings}

    top_row_color = settings["top_row_color"]
    top_column_color = settings["top_column_color"]
    alt_color_1 = settings["alt_color_1"]
    alt_color_2 = settings["alt_color_2"]
    background_color = settings["background_color"]
    cell_font_name = settings["cell_font_name"]
    cell_text_color = settings["cell_text_color"]
    border_color = settings["border_color"]
    border_thickness = settings["border_thickness"]
    anti_alternating = settings["anti_alternating"].lower() == "true"
    title_flag = settings["title"].lower() == "true"
    title_text = settings["title_text"]
    title_color = settings["title_color"]

    if title_text == "":
        title_text = "CSV Data"

    if anti_alternating:
        alt_color_1, alt_color_2 = alt_color_2, alt_color_1

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        html_content = f'''
        <html lang="en">
        <head>
            <title>CSV to HTML</title>
            <style>
                h1 {{
                    text-align: center;
                    color: {title_color};
                }}
                body {{
                    background-color: {background_color};
                    font-family: '{cell_font_name}', sans-serif;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    color: {cell_text_color};
                    border: {border_thickness} solid {border_color};
                    padding: 8px;
                    text-align: left;
                }}
                tr:first-child {{
                    background-color: {top_row_color};
                }}
                td:first-child {{
                    background-color: {top_column_color};
                }}
                tr:nth-child(2n+1) td {{
                    background-color: {alt_color_1};
                }}
                tr:nth-child(2n+2) td {{
                    background-color: {alt_color_2};
                }}
            </style>
        </head>
        <body>'''

        if title_flag:
            html_content += f'<h1>{title_text}</h1>'

        html_content += '''
            <table>
                <thead>
                    <tr>'''
        for header in headers:
            html_content += f'<th>{header}</th>'
        
        html_content += '''
                    </tr>
                </thead>
                <tbody>
        '''
        row_index = 0
        for row in reader:
            row_index += 1
            html_content += '<tr>'
            for column_index, column in enumerate(row):
                if column_index == 0:
                    html_content += f'<td style="background-color:{top_column_color}">{column}</td>'
                else:
                    html_content += f'<td>{column}</td>'
            html_content += '</tr>'
        html_content += '''
                </tbody>
            </table>
        </body>
        </html>
        '''
    with open(html_file_path, mode='w', encoding='utf-8') as htmlfile:
        htmlfile.write(html_content)

pref_file_path = 'pref.txt'
csv_file_path = 'example.csv'
html_file_path = 'output.html'
preferences = read_preferences(pref_file_path)
csv_to_html(csv_file_path, html_file_path, preferences)
