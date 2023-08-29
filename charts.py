''' Draws temperature charts for each day of a specific month '''
from constants import BLUE, RED, WHITE


class Charts:
    '''Class to draw temperature charts'''

    def __init__(self, data_of_month) -> None:
        self.data_of_month = data_of_month

    def draw_graph(self):
        '''Draw charts of highest and lowest temperature of each day'''
        month = self.data_of_month[0].pkt
        formated_date = month.strftime("%B %Y")
        single_graph_string = ""
        seperate_graph_string = ""
        for day in self.data_of_month:
            date = day.pkt.strftime("%d")
            max_temp = day.max_temperature_celcius
            min_temp = day.min_temperature_celcius
            seperate_graph_string += f'''{date} {RED}{max_temp * '+'} {WHITE}{max_temp}C\n{
                date} {BLUE}{min_temp * '+'} {WHITE}{min_temp}C\n'''
            single_graph_string += f'''{date} {BLUE}{min_temp * '+'}{RED}{max_temp * '+'} {
                WHITE}{min_temp}C-{max_temp}C\n'''
        print(formated_date)
        print(single_graph_string)
        print(formated_date)
        print(seperate_graph_string)
