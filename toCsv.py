def toCsv():

    import glob
    import pathlib as Path
    import pandas as pd
    import tabula
    import datetime
    pdfName = Path.Path('download').glob('*.pdf')
    print(pdfName)

    file = glob.glob("download/*")

    gb = ['Go', 'Back']

    dtn = datetime.datetime.now()
    dtn = dtn.strftime('%Y-%m-%d')

    dfs = tabula.read_pdf(f"{file[0]}", lattice=True, pages='all')
    
    for i in range(2):

        dfs[i] = dfs[i].dropna(axis = 1)
        dfs[i].to_csv(f"csv/timeTable{gb[i]}_{dtn}.csv", index=None)

