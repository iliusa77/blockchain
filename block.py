#!venv/bin/python

import json
import os
import stat
import hashlib

blockchain_dir = os.curdir + '/blockchain/'
file_block = blockchain_dir + '1'

def create_genesys_block():
    os.mkdir(blockchain_dir, int('0755')|stat.S_IRUSR)
    gen_block = os.mknod(file_block, int('0644')|stat.S_IRUSR)
    return gen_block

def write_genesys_block():
    data = {
        'name': 'User',
        'amount': 10,
        'to_whom': 'Master',
        'hash': '494ca1672d8f3c519ad1139f6783c997'
    }
    with open(file_block, 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)


def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def get_files():
    files = (os.listdir(blockchain_dir))
    return sorted([int(i) for i in files])

def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()

    prev_file = files[-1]
    filename = str(prev_file + 1)

    prev_hash = get_hash(str(prev_file))

    data = {
        'name': name,
        'amount': amount,
        'to_whom': to_whom,
        'hash': prev_hash
    }

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def check_integrity():
    files = get_files()

    for file in files[1:]:
        h = json.load(open(blockchain_dir + str(file)))['hash']

        prev_file = str(file - 1)

        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'OK'
        else:
            res = 'Corrupted'

        print("bloc {} is {}".format(prev_file, res))

def main():
    print('yes - if fist start, no - if not')
    start = input('Is this initial start blockchain? ')
    if start == "yes":
        create_genesys_block()
        write_genesys_block()
    else:
        write_block(name='Georg', amount=67, to_whom='Tatiana')
        check_integrity()


if __name__ == '__main__':
    main()