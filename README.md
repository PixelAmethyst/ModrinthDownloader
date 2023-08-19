<h1>
  <a href='https://modrinth.com/'>
    <img src='https://docs.modrinth.com/img/logo.svg'
         alt='Modrinth icon'
         width='40'
         height='40'
         align='Absbottom'>
  </a> Modrinth base downloader </h1>

### A simple downloader for mods hosted on the modrinth platform.

You can download mods from Modrinth by calling the function "`download_mod_from_modrinth`" from the class "`Downloader`".

This function will be looking for a match for our loader, version and our mod slug that we are looking for, if it finds a match it will break the loop.

```python
    def download_mod_from_modrinth(self, mod_slug, version, loader, output):
        """ Download a mod using Modrinth API. """

        raw_response = self.session.get(
            f'{self.modrinth_api}/project/{mod_slug}/version', timeout = 60)

        mod_request = loads(raw_response.content)
        raw_response.raise_for_status()

        mod_version_to_download = None

        for mod in mod_request:
            if version in mod['game_versions'] and loader in mod['loaders']:

                mod_version_to_download = mod
                break
```

The "`__init__`" of the class will store the Modrinth API url on a variable and start a requests session to handle an user-agent.
```python
    def __init__(self):
        self.modrinth_api = 'https://api.modrinth.com/v2'
        self.session = Session()

        self.session.headers.update({'User-Agent':
            'TrollSkull/PixelAmethyst (trollskull.contact@gmail.com)'})
```
