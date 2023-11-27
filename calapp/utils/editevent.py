from datetime import date
from dateutil.relativedelta import relativedelta
from .gapi import Gapi
from ..config.id_dic import id_dic

class EditEvent:
    def __init__(self) -> None:
        self.event = Gapi()
    
    def create_event(self, year: int, month: int, day: int, continue_month: int) -> None:
        start_day = date(year, month, day)
        for month in range(1, continue_month + 1):
            title = f'{month // 12}年記念日' if month % 12 == 0 else f'{month}ヶ月記念日' if month < 12 else f'{month // 12}年{month % 12}ヶ月記念日'
            aniv_day = (start_day + relativedelta(months=month)).strftime('%Y-%m-%d')
            self.event.create_event(title, f'{aniv_day}', f'{aniv_day}', True)
            
    def delete_event(self, index) -> None:
        index = str(index)
        event_id = id_dic[index]
        self.event.delete_event(event_id)
        del id_dic[index]
        with open('calapp/config/id_dic.py', 'w') as f:
            f.write(f'{id_dic = }')

    def delete_all_event(self) -> None:
        for index in list(id_dic):
            event_id = id_dic[index]
            self.event.delete_event(index, event_id)
            del id_dic[index]
        with open('calapp/config/id_dic.py', 'w') as f:
            f.write(f'{id_dic = }')