import pandas as pd
import plot

def get_df():
	df = pd.read_csv('tempratures')
	df['epoch'] = pd.to_datetime(df['epoch'], unit='ms')
	df = df.set_index('epoch')
	df.columns = df.columns.str.strip()
	df = df.fillna(method='ffill')
	df = df.replace(to_replace=0, method='ffill')

	return df

df = get_df()

plot.plotly_df(df)
