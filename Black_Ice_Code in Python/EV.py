'''
주어진 위경도 좌표에 해당하는 고도를 얻을 수 있음
'''
import requests
import pandas as pd

class EV(object):
    def __init__(self):
        self.ELEVATION_URL = 'https://maps.googleapis.com/maps/api/elevation/json'
        self.API_KEY = 'AIzaSyBUhgmfZrtL90wEBBnJmjVFNtLyEMH3RB0'
        self.RESPONSE = {}
        self.POS_CNT_LIMIT = 300

    @staticmethod
    def conv_coord(coord):
        '''
        :param coord: (x, y)
        :return: API 요청을 할 때에는 '위도,경도'의 형식으로 입력 처리되어야 함.
        '''
        x = coord[1]
        y = coord[0]

        return '%s,%s' % (x, y)

    def fetch(self, params):
        '''
        :param params: list 내부에 위경도 tuple이 저장되어있음 ex) [(127, 36), (127, 36.5)]
        :return:
        '''
        coords = '|'.join(EV.conv_coord(params[i]) for i in range(len(params)))

        requests_url = self.ELEVATION_URL + '?key=' + self.API_KEY + '&locations=' + coords
        self.RESPONSE = requests.get(requests_url)

    def get_elevation(self):
        '''
        :param r: requests result
            {
               "results" : [
                  {
                     "elevation" : 26.43111038208008,
                     "location" : {
                        "lat" : 36,
                        "lng" : 127
                     },
                     "resolution" : 152.7032318115234
                  }
               ],
               "status" : "OK"
            }

        :return: ev_list (경도, 위도, 고도)
        '''
        r_json = self.RESPONSE.json()

        if self.RESPONSE.status_code == 200:
            response = r_json['results'] # list

            ev_list = []
            for res in response:
                x = res['location']['lng']
                y = res['location']['lat']
                ev = res['elevation']

                #ev_list.append((x, y, ev))

            #result = ev_list
            result = ev

        else:
            print('%s, %s' % (r_json['status'], r_json['error_message']))
            result = 0.0

        return result

    @staticmethod
    def test():
        #locs = [(127, 36), (127, 35.5), (126.5, 36)]
        #locs = [(127, 36)]
        data = pd.read_csv('Data/VDS/VDS_VMS_code.csv',encoding='euc-kr')
        dataframe = pd.DataFrame()
        for i in range(len(data)):
            # x = data.iloc[i, 6]
            # y = data.iloc[i, 7]
            x = data.iloc[i,8]
            y = data.iloc[i,9]
            locs = [(y,x)]
            ev.fetch(locs)
            ev_result = ev.get_elevation()

            #print(type(ev_result))
            #data_set = {'index' : i,'czid' : data.iloc[i,0],'s_elevation':ev_result}
            data_set = {'index' : i,'czid' : data.iloc[i,0],'e_elevation':ev_result}
            dataframe = dataframe.append(data_set,ignore_index=True)
            print(i,'번째 좌표 (',x,',',y,')의 고도 :',ev_result)
            # for ev_set in ev_result:
            #    print(ev_set)
        dataframe.to_csv('end.csv',encoding='euc-kr',index=False)
if __name__ == '__main__':
    ev = EV()

    ev.test()
