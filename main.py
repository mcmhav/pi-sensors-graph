import pandas as pd
import plot
import config

def get_df(tempratures_location):
	df = pd.read_csv(tempratures_location)
	df['epoch'] = pd.to_datetime(df['epoch'], unit='ms')
	df = df.set_index('epoch')
	df.columns = df.columns.str.strip()
	df = df.fillna(method='ffill')
	df = df.replace(to_replace=0, method='ffill')

	return df

config = config.get_yaml('config.yaml')

df = get_df(config['tempratures_path'])

plot.plotly_df(df, dir=config['plot_location'])
