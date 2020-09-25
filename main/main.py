from main.libs.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/myyyxa/sshemp.git')
    ota_updater.download_and_install_update_if_available('qq', '1982Qt6e9findiglo19820912')

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    from main.house import House
    house=House()
    return house
    
def boot():
    download_and_install_update_if_available()
    start()


boot()