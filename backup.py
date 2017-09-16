import os
import time
import zipfile

source = ['source']

target_dir = 'dest'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Created dir', today)

zip_command = 'zip -r {} {}'.format(target, ' '.join(source))
print(zip_command)

if os.system(zip_command) == 0:
    print('Backed up to [{}]'.format(target))
else:
    print('Backup failed')
