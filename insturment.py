import pandas as pd
import utils 

class Instrument():
    def __init__(self, ob):
        self.name = ob['name'],
        self.type = ob['type'],
        self.displayName = ob['displayName'],
        self.pipLocation = pow(10, ob['pipLocation']),
        self.marginRate = ob['marginRate']

    def __repr__(self) -> str:
        return str(vars(self))
    
    @classmethod
    def get_intsrument_df(cls):
        return pd.read_pickle(utils.get_instrument_data_filename())


    @classmethod 


if __name__ == "__main__":
    df = Instrument.get_intsrument_df()

    print(df.to_dict(orient='record'))