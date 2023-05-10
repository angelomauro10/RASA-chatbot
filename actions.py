# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions




from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import pymssql


ddbb = pd.read_excel('ddbb.xls')

iterador = ddbb.iterrows()

class ActionSetSlot(Action):
   def name(self) -> Text:
       return "action_set_slot_from_xls"

   def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       for index, row in iterador:
           
           nombre = str(row['nombre'])
           idcliente = str(row['idcliente']).replace('BSR_TARDIA', 'Banco Santander Rio').replace(
               'FRANCES_2012', 'Banco BBVA Francés').replace('AFM_HSBC', 'Banco HSBC')
           saldo_total = str(row['saldo_total'])


           return [SlotSet('nombre', nombre),
                   SlotSet('idcliente', idcliente),
                   SlotSet('saldo_total', saldo_total)]


#   def run(self, dispatcher: CollectingDispatcher,
#           tracker: Tracker,
#           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#       conn = pymssql.connect(server='111.111.111.111', user='abcdef', password='1234567', database='ddbb')
#
#       cursor = conn.cursor()
#
#       #sql = 'SELECT  * FROM dbo.database_name'
#
#       cursor.execute('SELECT * FROM dbo.database_name')
#
#       row = cursor.fetchall()
#
#       while row:
#
#
#           nombre = str(row[0][1])
#           idcliente = str(row[0][2]).replace('BSR_TARDIA', 'Banco Santander Rio').replace(
#               'FRANCES_2012', 'Banco BBVA Francés').replace('AFM_HSBC', 'Banco HSBC')
#           saldo_total = str(row[0][0])
#
#           row = cursor.fetchall()
#
#           return [SlotSet('nombre', nombre),
#                   SlotSet('idcliente', idcliente),
#                   SlotSet('saldo_total', saldo_total)]





#
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
