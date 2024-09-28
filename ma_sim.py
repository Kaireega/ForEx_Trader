import pandas as pd
import utils 
import insturment

pd.set_option('display.max_columns',None)

def is_trade(row):
    if row.DIFF >= 0 and row.DIFF_PREV < 0:
        return 1
    if row.DIFF <= 0 and row.DIFF_PREV > 0:
        return -1
    return 0


def get_ma_col(ma):
    return  f"MA_{ma}"


def evaluate_pair(i_pair, mashort, malong ,price_data):
    
    price_data['DIFF'] = price_data[get_ma_col(mashort)] - price_data[get_ma_col(malong)] 
    price_data['DIFF_PREV'] = price.DIFF.shift(1)
    price_data['IS_TRADE'] = price_data.apply(is_trade,axis=1)

    df_trades = price_data[price_data.IS_TRADE != 0].copy()
    df_trades = ["DELTA"] = (df_trades.mid_c.diff() / i_pair.pipLocation).shift(-1)
    df_trades = ["GAIN"] = df_trades["DELTA"]* df_trades["IS_TRADE"]

    print(f"{i.pair.name} {mashort} {malong} trades:{df_trades.shape[0]} gain:{df_trades['GAIN'].sum():of}")
    return 

def get_price_data(pairame, granularity):
    df = pd.read_pickle(utils.get_his_data_filename(pairame, granularity))
    none_columns = ['time', 'volume']
    mod_columns = [x for x in df.columns if x not in none_columns ]
    df[mod_columns] = df[mod_columns].apply(pd.to_numeric)
    return df[['time','mid_c']]


def process_data(ma_short, ma_long, price_data):
    ma_list = set(ma_short + ma_long)

    for ma in ma_list:
        price_data[get_ma_col(ma)] = price_data.mid_c.rolling(window=ma).mean()
    
    return price_data

def run():
    pairname = "GBP_JPY"
    granularity = "H1"
    ma_short =[8,16,32,64]
    ma_long =[16,64,96,128,256]
    i_pair = insturment.Instrument.get_instruments_dict()[pairname]
    
    price_data = get_price_data(pairname,granularity)
    price_data = process_data(ma_short,ma_long,price_data)
    print(price_data.tail())

    best = -1000000.0
    b_maShort = 0
    b_maLong = 0

    for _maLong in ma_long:
        for _maShort in ma_short:

            #####

if __name__ == "__main__":
    run()