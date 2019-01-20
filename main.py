import pandas as pd
import plot
import config
import sys
import getopt

def make_plot(config_path):
    def get_df(tempratures_location, from_url=False):
        if from_url:
            s = requests.get(tempratures_location).content
            df = pd.read_csv(io.StringIO(s.decode('utf-8')))
        else:
            df = pd.read_csv(tempratures_location)

        df['epoch'] = pd.to_datetime(df['epoch'], unit='ms')
        df = df.set_index('epoch')
        df.columns = df.columns.str.strip()
        df = df.fillna(method='ffill')
        df = df.replace(to_replace=0, method='ffill')

        return df

    configs = config.get_yaml(config_path)
    
    from_url = False
    if from_url in configs:
        from_url = configs['from_url']

    df = get_df(configs['tempratures_path'])

    plot.plotly_df(df, dir=configs['plot_location'], auto_open=False)

def help():
   print('heeeelp')

def main(argv):
    config_path = 'local.yaml'
    debug = False
    
    try:
        opts, _ = getopt.getopt(argv, 'hdc:', ['help', 'debug', 'config='])
    except getopt.GetoptError:
        print('something wrong with inputz')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-d', '--debug'):
            DEBUG = True
        if opt in ('-c', '--config'):
            config_path = arg
        if opt in ('-h', '--help'):
            help()
            sys.exit(0)
        # elif opt in ('-g', '--GETresponse'):
        #     GET_RESPONSE = arg
        # elif opt in ('-s', '--responseStatus'):
        #     STATUS_CODE = arg

    make_plot(config_path)

if __name__ == '__main__':
    """ Parse arguments """
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
