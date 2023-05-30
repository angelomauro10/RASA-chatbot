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
           idcliente = str(row['idcliente']).replace('BANK1', 'International Bank 1').replace(
               'BANK2', 'National Bank 2').replace('BANK3', 'Banking Society 3')
           saldo_total = str(row['saldo_total'])


           return [SlotSet('nombre', nombre),
                   SlotSet('idcliente', idcliente),
                   SlotSet('saldo_total', saldo_total)]



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
