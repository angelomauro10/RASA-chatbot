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
import os



class ActionSetSlot(Action):
   def name(self) -> Text:
       return "action_set_slot_from_xls"

   def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       conn = pymssql.connect(server='192.168.120.120', user='jsoulez', password='Mopc2022*', database='master')

       cursor = conn.cursor()

       #sql = 'SELECT  ID_MOPC, IDMOROSO, IDCLIENTE, OPERADOR, CAMPAÑA, FECHA, ID, IDLLAMADA FROM Active.dbo.NEOTEL_AUDIOS_ACTIVE'

       cursor.execute('SELECT top 10 ID_MOPC, IDMOROSO, IDCLIENTE, OPERADOR, CAMPAÑA, FECHA, ID, IDLLAMADA FROM Active.dbo.NEOTEL_AUDIOS_ACTIVE')

       row = cursor.fetchall()

       while row:

           # while sin condicion itera infinitamente. Buscar reemplazo de while
           nombre = str(row[0][1])
           idcliente = str(row[0][2]).replace('BSR_TARDIA', 'Banco Santander Rio').replace(
               'FRANCES_2012', 'Banco BBVA Francés').replace('AFM_HSBC', 'Banco HSBC')
           saldo_total = str(row[0][0])

           row = cursor.fetchall()

           return [SlotSet('nombre', nombre),
                   SlotSet('idcliente', idcliente),
                   SlotSet('saldo_total', saldo_total)]

class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation=tracker.events
        print(conversation)
        if not os.path.isfile('chats.csv'):
            with open('chats.csv','w') as file:
                file.write("intent,user_input,entity_name,entity_value,action,bot_reply\n")
        chat_data=''
        for i in conversation:
            if i['event'] == 'user':
                chat_data+=i['parse_data']['intent']['name']+','+i['text']+','
                print('user: {}'.format(i['text']))
                if len(i['parse_data']['entities']) > 0:
                    chat_data+=i['parse_data']['entities'][0]['entity']+','+i['parse_data']['entities'][0]['value']+','
                    print('extra data:', i['parse_data']['entities'][0]['entity'], '=',
                          i['parse_data']['entities'][0]['value'])
                else:
                    chat_data+=",,"
            elif i['event'] == 'bot':
                print('Bot: {}'.format(i['text']))
                try:
                    chat_data+=i['metadata']['utter_action']+','+i['text']+'\n'
                except KeyError:
                    pass
        else:
            with open('chats.csv','a') as file:
                file.write(chat_data)

        dispatcher.utter_message(text="All Chats saved.")

        return []


class ActionSaveEndpoints(Action):

    def name(self) -> Text:
        return "action_save_endpoints"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation=tracker.events
        print(conversation)
        a = pd.read_csv('chats.csv', error_bad_lines=False)
        if 'utter_bot_validacion_oferta_positiva' in str(a.entity_name[-1:]) or 'utter_bot_validacion_oferta_positiva' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '10-Desvio_Operadora'
        elif 'utter_bot_validacion_conocido_positivo' in str(a.entity_name[-1:]) or 'utter_bot_validacion_conocido_positivo' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '10-Desvio_Operadora'
        elif 'utter_bot_saludo' in str(a.entity_name[-1:] or 'utter_bot_saludo' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '02-Sin_Interes_unk'
        elif 'utter_bot_validacion_moroso_positivo' in str(a.entity_name[-1:]) or 'utter_bot_validacion_moroso_positivo' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '02-Reconoce_Identidad'
        elif 'utter_bot_validacion_oferta_negativa' in str(a.entity_name[-1:]) or  'utter_bot_validacion_oferta_negativa' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '03-Interes_en_conocer_detalles_unk'
        elif 'utter_bot_validacion_moroso_negativo' in str(a.entity_name[-1:]) or 'utter_bot_validacion_moroso_negativo' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '07-No_reconoce_identidad'
        elif 'utter_bot_validacion_conocido_negativo' in str(a.entity_name[-1:]) or 'utter_bot_validacion_conocido_negativo' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '08-No_reconoce_identidad'
        elif 'utter_bot_validacion_operador_negativo' in str(a.entity_name[-1:]) or 'utter_bot_validacion_operador_negativo' in str(a.user_input[-1:]):
            a.entity_name[-1:] = '04-Sin_Dudas'

        a.to_csv('chats.csv')

        return []
#class ActionSaludo(Action):
#    def name(self) -> Text:
#        return "action_bot_saludo"
#
#    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#        nombre = tracker.get_slot('nombre')
#        idcliente = tracker.get_slot('idcliente')
#        saldo_total = tracker.get_slot('saldo_total')
#
#        if nombre and idcliente and saldo_total:
#          mensaje = f"Hola, soy el asistente virtual en representacion del {idcliente}, hablo con {nombre}?"
#
#          dispatcher.utter_message(text = mensaje)
#
#        return []


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
