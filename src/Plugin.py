__copyright__ = """
    This file is part of the TouchPortal-API project.
    Copyright (c) TouchPortal-API Developers/Contributors
    Copyright (C) 2023 DamienS
    All rights reserved.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from concurrent.futures import Executor
import sys
from typing import TextIO
from TouchPortalAPI import Client
import TouchPortalAPI as TP
from inspect import signature
import inspect
from TouchPortalAPI import sdk_tools
import json


class __TPPluginMeta:
    __TP_SETTINGS = {}


class Plugin(Client):
    __TP_REGISTER_CALLCOUNT = 0

    def __init__(self, pluginId: str,
                 sleepPeriod: float = 0.01,
                 autoClose: bool = False,
                 checkPluginId: bool = True,
                 updateStatesOnBroadcast: bool = False,
                 maxWorkers: int = None,
                 executor: Executor = None,
                 useNamespaceCallbacks: bool = False,
                 loggerName: str = None,
                 logLevel: str = "INFO",
                 logStream: TextIO = sys.stderr,
                 logFileName: str = None):
        super().__init__(pluginId, sleepPeriod, autoClose, checkPluginId,
                         updateStatesOnBroadcast, maxWorkers, executor,
                         useNamespaceCallbacks, loggerName, logLevel,
                         logStream, logFileName)

        self.wrappedMethods = []
        self.add_listener(TP.TYPES.onAction, self._actionHandler)
        self.add_listener(TP.TYPES.onConnect, self._onConnect)
        self.add_listener(TP.TYPES.onSettingUpdate, self._onSettings)
        self.add_listener(TP.TYPES.onError, self._onError)
        self.settings = {}

        self.registeredAction = {}
        self.registeredSetting = {}
        self.registeredConnector = {}
        self.callback = {"onConnect": None}

    def getArgs(self, frame):
        args_dict = {}
        args, _, _, values = inspect.getargvalues(frame)
        for arg in args:
            args_dict[arg] = values[arg]
        return args_dict

    def runErrorCheck(self, argsValue, annotation):
        isvaild = True
        for parm in annotation.keys():
            if not isinstance(argsValue.get(parm), annotation[parm].annotation) and annotation[parm].annotation != inspect._empty:
                print(
                    f"{parm} arg needs to be type {annotation[parm].annotation} not {type(argsValue[parm])}")
                isvaild = False
        return isvaild
    
    def getDoc(self, func):
        if hasattr(func, '__doc__'):
            return func.__doc__
        
        return ""

    def _actionHandler(self, data):
        if not (actionid := data.get('actionId')):
            return
        
        action_data = data.get('data')
        action_data = {data["id"].split(".")[-1]: data["value"] for data in action_data}

        if actionid in self.registeredAction.keys():
            self.registeredAction[actionid](self, action_data)

    def settingsRegister(name: str, type: str, default: str = "", maxLength: int = -1, isPassword: bool = False, minValue: int = -2147483647, maxValue: int = 2147483647, readOnly: bool = False):
        frame = inspect.currentframe()

        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if name in self.registeredSetting:
                    raise Exception("Same settings exist already.")
                self.registeredSetting[name] = func

                setting = {}
                argValue = self.getArgs(frame)
                annotation = dict(signature(self.settingsRegister).parameters)
                isVaildEntry = self.runErrorCheck(argValue, annotation)

                if isVaildEntry:
                    setting = {
                        "name": argValue['name'],
                        "type": argValue['type'],
                        "default": argValue['default']
                    }

                    if argValue['type'] == "number":
                        setting["minValue"] = argValue['minValue']
                        setting["maxValue"] = argValue['maxValue']

                    if argValue['maxLength'] != -1:
                        setting["maxLength"] = argValue['maxLength']
                    
                    if argValue['isPassword']:
                        setting["isPassword"] = argValue['isPassword']
                    
                    if argValue['readOnly']:
                        setting["readOnly"] = argValue['readOnly']

                    if (doc := self.getDoc(func)) != "":
                        setting["doc"] = doc
                else:
                    raise TypeError("Please check the error above.")
                self.TP_PLUGIN_SETTINGS[name] = setting
            
            Plugin.__TP_REGISTER_CALLCOUNT += 1
            wrapper.wrapped = Plugin.__TP_REGISTER_CALLCOUNT
            return wrapper

        return decorator

    def actionRegister(category:str, id:str, name:str, prefix:str, type:str="communicate", executionType:str="", execution_cmd:str="", description:str="", tryInline:bool=True, format:str="", hasHoldFunctionality:bool=False):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                new_id = self.PLUGIN_ID + ".act." + id
                if new_id in self.registeredAction:
                    raise Exception("Action ID cannot be same")
                self.registeredAction[new_id] = func

                action = {
                    'id': new_id,
                    'name': name,
                    'prefix': prefix,
                    'type': type
                }

                if hasattr(func, 'data'):
                    action_data = func.data
                else:
                    action_data = []

                if action_data and format is not None:
                    formats = format
                    for data in action_data:
                        old_id = data["id"]
                        data["id"] = new_id + ".data." + old_id
                        formats = formats.replace("$[" + old_id + "]", f"$[{action_data.index(data) + 1}]")
                    action['format'] = formats
                    action['data'] = action_data
                else:
                    action['format'] = format
                
                if isinstance(category, str) and category != "":
                    action['category'] = category

                if isinstance(tryInline, bool):
                    action['tryInline'] = tryInline
                
                if isinstance(hasHoldFunctionality, bool):
                    action['hasHoldFunctionality'] = hasHoldFunctionality

                if isinstance(executionType, str) and executionType != "":
                    action['executionType'] = executionType

                if isinstance(execution_cmd, str) and execution_cmd != "":
                    action['execution_cmd'] = execution_cmd

                if isinstance(description, str) and description != "":
                    action['description'] = description

                self.TP_PLUGIN_ACTIONS[id] = action

                if (doc := self.getDoc(func)) != "":
                        action["doc"] = doc

            Plugin.__TP_REGISTER_CALLCOUNT += 1
            wrapper.wrapped = Plugin.__TP_REGISTER_CALLCOUNT
            return wrapper

        return decorator
    
    def addDoc(doc:str):
        def decorator(func):
            func.__doc__ = doc
            return func
        return decorator
    
    def connectorRegister(id:str, name:str, format:str):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                new_id = self.PLUGIN_ID + ".con." + id
                if new_id in self.registeredConnector:
                    raise Exception("Connector ID cannot be same")
                self.registeredConnector[new_id] = func
                if not hasattr(func, 'data'):
                    func.data = {}

                if 'data' not in func.data:
                    func.data['data'] = []

                data_entry = {
                    'id': id,
                    'name': name,
                    'format': format
                }

                func.data['data'].append(data_entry)

        return decorator
    
    def data(id:str, type:str, label:str, default:str, valueChoices:list=None, extensions:list=None, allowDecimals:bool=None, minValue:int=None, maxValue:int=None):
        def decorator(func):
            if not hasattr(func, 'data'):
                func.data = []

            if any([id, type, label, default]) is None:
                raise Exception("id, type, label, default is required")
            if not (type.lower() in ["text", "number", "switch", "choice"]):
                raise Exception("type must be text, number, switch, choice")
            
            data_entry = {
                'id': id,
                'type': type.lower(),
                'label': label,
                'default': default
            }

            if isinstance(label, str) and label != "":
                data_entry['label'] = label

            if isinstance(default, str) and default != "":
                data_entry['default'] = default

            if isinstance(valueChoices, list) and type == "choice":
                data_entry['valueChoices'] = valueChoices

            if isinstance(extensions, list):
                data_entry['extensions'] = extensions

            if type == "number":
                if isinstance(allowDecimals, bool):
                    data_entry['allowDecimals'] = allowDecimals

                if isinstance(minValue, int):
                    data_entry['minValue'] = minValue

                if isinstance(maxValue, int):
                    data_entry['maxValue'] = maxValue
            else:
                if (allowDecimals or minValue or maxValue) is not None:
                    raise Exception("allowDecimals, minValue, maxValue is only for number type")

            func.data.append(data_entry)
            return func

        return decorator

    def handleSettings(self, settings):
        for setting in settings:
            key = list(setting.keys())[0]
            if self.settings.get(key) != setting.get(key):
                self.registeredSetting.get(key)(self, setting.get(key))

        settings = {list(settings[i])[0]: list(settings[i].values())[
            0] for i in range(len(settings))}

        self.settings = settings

    def _onSettings(self, data):
        self.handleSettings(data['values'])

    def _onConnect(self, data):
        self.handleSettings(data.get("settings"))

        if self.callback['onConnect']:
            self.callback['onConnect'](self, data)

    def onStart():
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                self.callback['onConnect'] = func

            wrapper.wrapped = True
            return wrapper
        return decorator
    
    def getRegisteredMethod(self):
        wrapped_methods = []
        for method_name in dir(self):
            attr = getattr(self, method_name)
            if callable(attr) and hasattr(attr, "wrapped"):
                wrapped_methods.append(attr)

        # write a sort function that sorts by the wrapped attribute
        wrapped_methods.sort(key=lambda x: x.wrapped)
        return wrapped_methods

    def startRegister(self):
        for action in self.getRegisteredMethod():
            action()

    def start(self):
        self.startRegister()
        self.connect()

    def _onError(self, error):
        print(error)