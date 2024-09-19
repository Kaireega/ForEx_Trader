def get_his_data_filename(pair,grannularity):
    return f"his_data/{pair}_{grannularity}.pkl"

def get_instrument_data_filename():
    return "instrument.pkl"


if __name__ == "__main__":
    print(get_his_data_filename('EUR_USD',"H1"))
    get_instrument_data_filename()