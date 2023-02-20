import pandas as pd

def clean(input_file1,input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df = pd.merge(df1, df2, left_on="respondent_id", right_on="id").drop('id', axis=1)
    df = df.dropna()
    df = df[~df['job'].str.contains('insurance')]
    df = df[~df['job'].str.contains('Insurance')]
    return df

data = clean("respondent_contact.csv","respondent_other.csv")
print(data.shape)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file (CSV1)')
    parser.add_argument('input2', help='Data file (CSV2)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1,args.input2)
    cleaned.to_csv(args.output, index=False)
