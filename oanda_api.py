import requests
import pandas as pd
import defs
import utils

class OandaAPI():

    def __init__(self) -> None:
        self.session = requests.Session()

    def fetch_instruments_data(self):
        url =f"{defs.OANDA_URL}/accounts/{defs.ACCOUNT_ID}/instruments"
        response = self.session.get(url,params=None, headers=defs.SECURE_HEADER)
        return response.status_code , response.json()



    def get_instruments_df(self):
        code , data = self.fetch_instruments_data()
        if code == 200:
             df = pd.DataFrame.from_dict(data['instruments'])
             return df[['name','type','displayName','pipLocation','marginRate']]
        else:
             return None

    def save_instruments(self):
        df = self.get_instruments_df()
        if df is not None:
            df.to_pickle(utils.get_instrument_data_filename())


    def fetch_candles(self,pair_name, count, granularity):
         url =f"{defs.OANDA_URL}/instruments/{pair_name}/candles"

         params = dict(
              count = count,
              granularity = granularity,
              price = "MBA"
         )
         response = self.session.get(url, params=params, headers=defs.SECURE_HEADER)
         return response.status_code , response.json()

    
        
if __name__ == "__main__":
        api = OandaAPI()
        # print(api.fetch_candles("EUR_USD",400,"H1"))
        # print(api.fetch_instruments_data())
        # print(api.get_instruments_df())
        api.save_instruments()