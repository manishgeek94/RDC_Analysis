import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
import pandas as pd
import numpy as np
from threading import Thread

plt.xkcd()

app = Flask(__name__)


@app.route("/erdate")
def RDC():
    erdat = pd.read_csv('erdate.csv')
    df = pd.DataFrame(erdat)
    # df.plot(kind='bar', x='ERDAT', y='NO_OF_RECORDS')
    plt.barh(df['ERDAT'], df['NO_OF_RECORDS'], color='g')
    plt.ylabel('Create_Date')
    plt.xlabel('Records_Count')
    plt.title("RDC Create Date")
    plt.savefig('static/images/createR.png', bbox_inches='tight', dpi=1000)
    plt.tight_layout()
    create_img = True
    return render_template('data.html', create_img=create_img)


@app.route("/cov_effective")
def RDC_Coverage():
    cov_eff = pd.read_csv('Coverage_March.csv')
    cf = pd.DataFrame(cov_eff)
    plt.barh(cf['COV_EFFDATE'], cf['NO_OF_RECORDS'], color='r')
    plt.xlabel('Record_Count/day')
    plt.ylabel('Date')
    plt.title("Cov_Record")
    plt.savefig('static/images/CoverageEffective.png', bbox_inches='tight',
                dpi=1000)  # bbox_inches removes extra white spaces.  dpi (The resolution in dots per inch)
    plt.tight_layout()
    return render_template('data.html')


@app.route("/idm")
def IDM():
    idm_sources = pd.read_csv('IDM_March_Sources.csv')
    idm = pd.DataFrame(idm_sources)

    # Record_count = list(range(idm['RECORD_CREATED']))
    Record_count = [2300, 7240, 7600, 8982, 2977, 4101, 9519, 2901]
    add = 0
    for item in Record_count:
        add = add + item
    total_records = add
    # Record_count = [3, 15, 23, 76, 84, 87, 97, 206, 218, 2108, 2317, 2977, 4101, 9519, 35022, 72402, 175821, 245743, 396858, 546193, 898298]
    # Data_sources = list(range(idm['DATA_SOURCE']))
    Data_sources = ['ATLAS', 'CLOUD', 'CSA', 'DM', 'WHI', 'SFDC', 'WH', 'THIRDPARTY']
    # Data_sources = ['TWCB2C', 'INEWS', 'ATLAS', 'CSA', 'Siebel', 'TWCB2B', 'TWCVC', 'LIST ACQUIRED', 'WHI', 'SFDC', 'WH', 'THIRDPARTY', 'Sales Connect', 'DSW SAP', 'DSW SQO', 'CLOUD', 'LIST LEASED', 'Web Identity', 'IWM', 'GRP', 'DM']
    plt.pie(Record_count, labels=Data_sources, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

    # plt.xlabel('Data_Source')
    # plt.ylabel('Count')
    plt.title("Record_Count/Data_Source")
    plt.savefig('static/images/idm_sources.png', bbox_inches='tight', dpi=1000)
    return render_template('data1.html', total_records=total_records)


@app.route("/shad_update")
def shad_update():
    timestamp = pd.read_csv('Update_March_ts.csv')
    tmp = pd.DataFrame(timestamp)
    indexes = np.arange(0, len(tmp['UPDATE_TIME_TODAY']), 1)
    plt.plot(indexes, tmp['RECORD_COUNT'], color='r', linestyle='--', marker='o')
    plt.ylabel('Count')
    plt.xlabel('Date')
    plt.title('Record/Day-MARCH')
    plt.grid(True)
    plt.savefig('static/images/update.png', bbox_inches='tight', dpi=1000)
    return render_template('update.html')


if __name__ == '__main__':
    app.run(port=1000, debug=True)
