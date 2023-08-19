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

Once it finds the match "`mod_version_to_download`" will no longer be "`None`", that means a compatible version of the mod was found.

Make a get request to download the mod file using the url provided in the "`mod_version_to_download`" dictionary. The binary content of the file is stored in the "`mod_file`" variable.

```python
    mod_file = self.session.get(mod_version_to_download['files'][0]['url'], timeout=60).content
```

Then extracts the mod's filename from the information provided in the dictionary.

```python
    file_name = mod_version_to_download['files'][0]['filename']
```

The binary content of the file is stored in the "mod_file" variable, and then download the mod by open a new file in your output directory.

Then gets the file size and name and print it. (The funtcion `__convert_bytes()` will convert the bytes into a slightly more readable number, for example: `1000000b > 1mb`)

```python
        if mod_version_to_download is not None:
            mod_file = self.session.get(
                mod_version_to_download['files'][0]['url'], timeout = 60).content

            file_name = mod_version_to_download['files'][0]['filename']
            downloaded_file = path.join(output, file_name)

            with open(downloaded_file, 'wb') as file:
                file.write(mod_file)

            get_size = path.getsize(downloaded_file)
            file_size = self.__convert_bytes(get_size)

            print(f'Downloaded {file_size} - {file_name}')

        else:
            print(f'Cannot find "{mod_slug}" for version {version} or loader {loader}!')
```

The "`__init__`" of the class will store the Modrinth API url on a variable and start a requests session to handle an user-agent.

```python
    def __init__(self):
        self.modrinth_api = 'https://api.modrinth.com/v2'
        self.session = Session()

        self.session.headers.update({'User-Agent':
            'TrollSkull/PixelAmethyst (trollskull.contact@gmail.com)'})
```
