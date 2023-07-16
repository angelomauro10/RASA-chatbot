This a BOT project applying a Python framework named RASA and this is used to create virtual assistants. 

The RASA's chatbot is working with a banks database considering that this bot will contact the customer notifying a 
specific deubt in a customized sense mentioning: the name, bank's name and money quantity to pay with the finallity to
redirect the user with a telephonically operator.

Every RASA's response as bot states a logical action depending the user's decission (if the person wants being comunicated
with a operator or not, or if the contacted is a family member or known person) and the bot will understand wich action 
must has to do. Beside that this bot has the fallback identiffication if user try to make a chit-chat action and fallback action will be activated explaining that does not understand the action and also will repeat the last message.

For last, when the bot finish the interaction, will continues with the next row (person) restarting it as a 
new historical event.

The following archives in this repository and their functions are:

ddbb.xls  : The file where the bot will manipulates the data.

actions.py : Where the bot is connected to the ddbb (.xls) and extracts a specific columns as Slots making the 
customization messages.

domain.yml : This file contains the programmed bot's responses, intents and actions archives linked and slots.

endpoints.yml : Contains the server and endpoints actions but this is configurated as default.

nlu.yml : Here we have the user's lists responses for each given event.

rules.yml : The bot reply's when the user is trying to do some action out of the specific bot's function.

config.yml : configure of fallback restrictions.

stories.yml : In this file are every situational event that this bot will have always persuading the user for being redirected
with a bank's representative. 

Best wishes.

//////////////////     -     /////////////////////

Este es un proyecto de un BOT que aplica un framework de Python llamado RASA y se usa para crear asistentes virtuales.
     
El chatbot de RASA está trabajando con una base de datos de bancos considerando que este bot contactará al cliente notificando un
deuda específica en un sentido personalizado mencionando: el nombre, el nombre del banco y la cantidad de dinero a pagar con la finalidad de
redirigir al usuario con un operador telefónico.

Cada respuesta de RASA como bot establece una acción lógica dependiendo de la decisión del usuario (si la persona quiere ser comunicada
con un operador o no, o si el contactado es un miembro de la familia o una persona conocida) y el bot entenderá qué acción
debe tomar. Aparte de eso, el bot tiene la identificacion de fallback en caso que el usario intente hacer alguna trampa al bot y cuando el fallback se active dará un mensaje de que no entiende la accion e incluso repetirá el mensaje.

Por último, cuando el bot termine la interacción, continuará con la siguiente fila (persona) reiniciándolo como un
nuevo acontecimiento histórico.

Los siguientes archivos en este repositorio y sus funciones son:

ddbb.xls: El archivo donde el bot manipulará los datos.

actions.py : Donde el bot está conectado al ddbb (.xls) y extrae columnas específicas como Slots haciendo el
mensajes de personalización.

domain.yml: Este archivo contiene las respuestas, las uniones entre los archivos de intenciones y las acciones del bot 
programado, y los Slots.

endpoints.yml: contiene las acciones del servidor y los endpoints pero está configurado de forma predeterminada.

nlu.yml: Aquí tenemos las respuestas de las listas de usuarios para cada evento dado.

rules.yml: La respuesta del bot cuando el usuario intenta realizar alguna acción fuera de la función específica del bot.

stories.yml: En este archivo se encuentran todos los eventos situacionales que este bot tendrá siempre 
persuadiendo al usuario para que sea redirigido con un representante del banco.

config.yml: configuracion de las politicas para el fallback.


Saludos cordiales.

