from os import path, getcwd, makedirs
from json import loads

from requests import Session

class Downloader:
    def __init__(self):
        self.modrinth_api = 'https://api.modrinth.com/v2'
        self.session = Session()

        self.session.headers.update({'User-Agent':
            'PixelAmethyst/ModrinthDownloader (trollskull.contact@gmail.com)'})

    @staticmethod
    def __convert_bytes(mod_bytes):
        units, byte = ['bytes', 'KB', 'MB', 'GB'], 0

        while mod_bytes >= 1024 and byte < len(units)-1:
            mod_bytes /= 1024
            byte += 1

        return f"{bytes:.2f} {units[byte]}"

    def download_mod(self, mod_slug, version, loader, output):
        raw_response = self.session.get(
            f'{self.modrinth_api}/project/{mod_slug}/version', timeout = 10)

        mod_request = loads(raw_response.content)
        raw_response.raise_for_status()

        mod_version_to_download = None

        for mod in mod_request:
            if version in mod['game_versions'] and loader in mod['loaders']:

                mod_version_to_download = mod
                break

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

    def search_mod(self, query, loader, version):
        raw_query_response = self.session.get(
            f'{self.modrinth_api}/search?query={query}', timeout = 10)

        mod_request = loads(raw_query_response.content)
        projects = mod_request['hits']

        #for project in projects:
        #    print(f'Name: {project["title"]}')
        #    print(f'Author: {project["author"]}')
        #    print(f'Description: {project["description"]}\n')

        return projects

class ManageMod:
    def __init__(self):
        mods_folder = path.join(getcwd(), 'downloaded')

        directories = [mods_folder]

        for directory in directories:
            makedirs(directory, exist_ok = True)
