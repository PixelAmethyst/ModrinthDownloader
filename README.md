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

This function will be looking for a match for our loader, version and our mod slug that we are looking for.

The "`__init__`" of the class will store the Modrinth API url on a variable and start a requests session to handle an user-agent.
```python
    def __init__(self):
        self.modrinth_api = 'https://api.modrinth.com/v2'
        self.session = Session()

        self.session.headers.update({'User-Agent':
            'TrollSkull/PixelAmethyst (trollskull.contact@gmail.com)'})
```
