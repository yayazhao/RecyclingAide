import os
import pandas as pd
from utils.utils import haversine


class SolidWasteFacilityDao:
    def __init__(self):
        self.cwd = os.getcwd()
        if self.cwd.endswith('data'):
            self.sw_facility_file = 'mycsv/SW_FacilityList_LatLng.csv'
        elif self.cwd.endswith('RecyclingAide'):
            self.sw_facility_file = 'data/mycsv/SW_FacilityList_LatLng.csv'
        else:
            self.sw_facility_file = 'data/mycsv/SW_FacilityList_LatLng.csv'
        self.sw_facility_path = os.path.join(self.cwd, self.sw_facility_file)
        self.fields = ['ID','County','Waste','Activity','Permit','Name','Status','Address','City','Contact','Phone','lat','lng']
        self._load_data()

    def _load_data(self):
        self.df = pd.read_csv(self.sw_facility_path, index_col=0)
        self.df['County'].astype(str)
        self.df['Waste'].astype(str)
        self.df['Activity'].astype(str)
        self.df['Permit'].astype(str)
        self.df['Name'].astype(str)
        self.df['Status'].astype(str)
        self.df['Address'].astype(str)
        self.df['City'].astype(str)
        self.df['Contact'].astype(str)
        self.df['Phone'].astype(str)
        self.df['Haversine'] = 1000000.0

    @staticmethod
    def get_waste_types():
        return {'All': 'All',
                'CCR': 'Coal Combustion Residuals',
                'CD': 'Construction and Demolition (C&D)',
                'HHW': 'Household Hazardous Wastes',
                'Indus': 'Industrial Waste',
                'LCID': 'Land Clearing and Inert Debris',
                'MatRecovery': 'Material Recovery',
                'Medical': 'Medical Waste',
                'MSW': 'Municipal Solid Waste',
                'Tire': 'Tire',
                'TypeI': 'Type I Waste',
                'TypeII': 'Type II Waste',
                'TypeIII': 'Type III Waste',
                'TypeIV': 'Type IV Waste',
                'YW': 'Yard Waste'}

    @staticmethod
    def get_activities():
        return {'All': 'All',
                'Incin': 'Incineration',
                'LF': 'Land Fill',
                'TP': 'Treatment and Processing',
                'Trans': 'Transfer Stations',
                'Compost': 'Compost Facilities',
                'Collection': 'Collection Sites',
                'SF': 'Structural Fills',
                'MatRecovery': 'Material Recovery'}

    def get_nearest_facilities(self, lat, lng, top_n=5, waste_type='All', activity='All'):
        _df = self.df
        _df['Haversine'] = 1000000.0
        if waste_type != 'All':
            _df = _df[_df.Waste == waste_type]
        if activity != 'All':
            _df = _df[_df.Activity == activity]

        for inx, row in _df.iterrows():
            lat2, lng2 = row['lat'], row['lng']
            ans = haversine(lat, lng, lat2, lng2)
            _df.loc[inx, 'Haversine'] = ans

        _df = _df.sort_values(by=['Haversine']) # don't use inplace=True, it will generate NaN error
        print('*'*100)
        print(_df)

        _df = _df.head(top_n)
        res = []
        r = 0
        for _, row in _df.iterrows():
            res.append({
                'Rank': r+1,
                'County': row['County'],
                'Waste': row['Waste'],
                'Activity': row['Activity'],
                'Permit': row['Permit'],
                'Name': row['Name'],
                'Address': row['Address'],
                'City': row['City'],
                'Contact': row['Contact'],
                'Phone': row['Phone'],
                'lat': row['lat'],
                'lng': row['lng'],
                'Haversine': round(row['Haversine'], 2),
            })
            r += 1
        return res

    def get_all_facilities(self):
        _df = self.df
        res = []
        for _, row in _df.iterrows():
            res.append({
                'County': row['County'],
                'Waste': row['Waste'],
                'Activity': row['Activity'],
                'Permit': row['Permit'],
                'Name': row['Name'],
                'Address': row['Address'],
                'City': row['City'],
                'Contact': row['Contact'],
                'Phone': row['Phone'],
                'lat': row['lat'],
                'lng': row['lng'],
            })
        return res


# dao = SolidWasteFacilityDao()
# print(dao.df.dtypes)
# print(dao.df.shape)
# res = dao.get_nearest_facilities(35.95954153292285, -79.06147683764769)
# print(res)
# print('Done!')
