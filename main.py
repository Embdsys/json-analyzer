import sweetviz as sv
import pandas as pd
import glob, os, json

def gather_json():
    json_dir = r'C:\Users\Juan\PycharmProjects\JoinJsonFiles\data'
    json_pattern = os.path.join(json_dir, '*.json')
    file_list = glob.glob(json_pattern)

    dfs = []
    for file in file_list:
        with open(file) as f:
            json_data = pd.json_normalize(json.loads(f.read()))
            json_data['site'] = file.rsplit("/", 1)[-1]
        dfs.append(json_data)
    df = pd.concat(dfs)

    print(df)
    #Build sweetviz frontend htlm
    my_report = sv.analyze(df)
    my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"

#Call
gather_json()