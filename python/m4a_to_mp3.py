import subprocess
import pathlib
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('You must provide a src and destiantion directory')
        sys.exit(-1)

    src = pathlib.Path(sys.argv[1])
    dest = pathlib.Path(sys.argv[2])

    if not src.exists():
        print('The src directory does not exists')
        sys.exit(-1)

    if not src.is_dir():
        print('The src is not directory')
        sys.exit(-1)

    if not dest.exists():
        print('Dest directory does not exists it will be created')
        dest.mkdir(parents=True, exists_ok=True)
    elif dest.is_file():
      print('Dest path is a file')
      sys.exit(-1)

    for f in src.iterdir():
        print(f)
        if f.name.endswith('.m4a'):
            mp3_name = f'{f.name[:-len('.m4a')]}.mp3'
            print(mp3_name)
            subprocess.run(['ffmpeg' , '-i', str(f), '-codec:a', 'libmp3lame', '-qscale:a', '0', '-map_metadata', '0', mp3_name])
            os.rename(mp3_name, f'{dest}/{mp3_name}')
