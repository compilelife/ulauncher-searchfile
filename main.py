from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.event import PreferencesEvent
from ulauncher.api.shared.event import PreferencesUpdateEvent
from locator import Locator


locator = Locator()

class SearchFileExtension(Extension):
    def __init__(self):
        super(SearchFileExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesUpdateEventListener())


class PreferencesUpdateEventListener(EventListener):
    def on_event(self, event, extension):
        if event.id == 'limit':
            locator.set_limit(event.new_value)


class PreferencesEventListener(EventListener):
    def on_event(self, event, extension):
        locator.set_limit(event.preferences['limit'])


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        arg = event.get_argument()
        items = []

        if arg is None:
            examples=['s 2018', 's r -r']
            desc = ['search file or directory 2018', 'search use regex']
            for i in range(len(examples)):
                items.append(ExtensionSmallResultItem(icon='images/info.png',
                name = examples[i]+' : '+desc[i],
                on_enter = SetUserQueryAction(examples[i])
                ))
        else:
            try:
                results = locator.run(arg)
                for file in results:
                    items.append(ExtensionSmallResultItem(icon='images/ok.png',
                        name = file, 
                        on_enter = OpenAction(file),
                        on_alt_enter = CopyToClipboardAction(file)))
            except Exception, e:
                error_info = str(e)
                items = [ExtensionSmallResultItem(icon='images/error.png',
                                                name = error_info,
                                                on_enter = CopyToClipboardAction(error_info))]
        
        return RenderResultListAction(items)


if __name__ == '__main__':
    SearchFileExtension().run()