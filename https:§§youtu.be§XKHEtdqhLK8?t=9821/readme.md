
# <https:§§youtu.be§XKHEtdqhLK8?t=9821>
> <https://youtu.be/XKHEtdqhLK8?t=9821>


## init

```py
touch tmp.py
python -m venv .venv
echo '.venv/' >> .gitignore
echo 'tmp.py' >> .gitignore

touch 'test' >> .gitignore
```

## file detection 

```py
import os

path = './'+'test'

if os.path.exists(path):
    print('exists')
    if os.path.isfile(path):
        print('isfile')


exists
isfile
```

https://docs.python.org/3/library/os.html?highlight=os#module-os


## read file contents

```py
import os

path = './'+'some_text'

with open(path) as file:
    print(file.read())
try:
    with open('abc') as file:
        print(file.read())
except FileNotFoundError:
    print('no file')


omg you can read this!
have a nice day...
pythonista :P 
no file

```
https://docs.python.org/3/library/os.html?highlight=open#os.open


## write file

you have to pass a file_mode

```py
import os

path = './'+'some_other_text'
text = "Yoooooooo!\nDude"

try:
    with open(path, 'a') as file:
        for i in range(2):
            file.write(text)
except Exception as e:
    print(e)

```

## copy file

```py
import shutil

path = './'+'some_other_text'
text = "Yoooooooo!\nDude"

try:
    shutil.copyfile(path,path+".cpf")
    shutil.copy(path,path+".c")
    shutil.copy2(path,path+".c2")
except Exception as e:
    print(e)

```

https://docs.python.org/3/library/shutil.html?highlight=copy%20file#shutil.copy


## modules

module a py code file with func class etc
used to separate programs into parts and reuse/mod

[messages](./messages.py)

```py
import messages

print(messages.hello('mario'))


hello mario!
```

or

```py
import messages as msg

print(msg.hello('mario'))
```

or  import what you need

```py
from messages import hello

print(hello('mario'))
```

> avoid using import *

use help to list all the built in modules
```py
help("modules")



Please wait a moment while I gather a list of all available modules...

CommandNotFound     _yaml               heapq               runpy
DistUpgrade         _zoneinfo           hmac                sched
HweSupportStatus    abc                 html                secrets
UpdateManager       aifc                html5lib            secretstorage
__future__          antigravity         http                select
_abc                apport              httplib2            selectors
_aix_support        apport_python_hook  idna                setuptools
_ast                apt                 imaplib             shellingham
_asyncio            apt_inst            imghdr              shelve
_bisect             apt_pkg             imp                 shlex
_blake2             aptsources          importlib           shutil
_bootsubprocess     argparse            importlib_metadata  signal
_bz2                array               inspect             site
_cffi_backend       ast                 io                  sitecustomize
_codecs             asynchat            ipaddress           six
_codecs_cn          asyncio             itertools           smtpd
_codecs_hk          asyncore            janitor             smtplib
_codecs_iso2022     atexit              jeepney             snack
_codecs_jp          audioop             json                sndhdr
_codecs_kr          autopep8            jwt                 socket
_codecs_tw          base64              keyring             socketserver
_collections        bdb                 keyword             softwareproperties
_collections_abc    binascii            launchpadlib        soupsieve
_compat_pickle      binhex              lib2to3             spwd
_compression        bisect              linecache           sqlite3
_contextvars        blinker             locale              sre_compile
_crypt              bs4                 lockfile            sre_constants
_csv                builtins            logging             sre_parse
_ctypes             bz2                 lsb_release         ssl
_ctypes_test        cProfile            lzma                stat
_curses             cachecontrol        mailbox             statistics
_curses_panel       cachy               mailcap             string
_datetime           cairo               marshal             stringprep
_dbm                calendar            math                struct
_dbus_bindings      certifi             messages            subprocess
_dbus_glib_bindings cgi                 mimetypes           sunau
_decimal            cgitb               mmap                symtable
_distutils_hack     chardet             modulefinder        sys
_distutils_system_mod chunk               more_itertools      sysconfig
_elementtree        cleo                msgpack             syslog
_functools          clikit              multiprocessing     systemd
_gdbm               cmath               netifaces           tabnanny
_hashlib            cmd                 netrc               tarfile
_heapq              code                nis                 telnetlib
_imp                codecs              nntplib             tempfile
_io                 codeop              ntpath              termios
_json               collections         nturl2path          test
_locale             colorsys            numbers             textwrap
_lsprof             compileall          oauthlib            this
_lzma               concurrent          opcode              threading
_markupbase         configparser        operator            time
_md5                contextlib          optparse            timeit
_multibytecodec     contextvars         os                  tmp
_multiprocessing    copy                ossaudiodev         token
_opcode             copyreg             packaging           tokenize
_operator           crashtest           pastel              tomli
_osx_support        crypt               pathlib             tomlkit
_pickle             cryptography        pdb                 trace
_posixshmem         csv                 pexpect             traceback
_posixsubprocess    ctypes              pickle              tracemalloc
_py_abc             curses              pickletools         tty
_pydecimal          dataclasses         pip                 turtle
_pyio               datetime            pipes               types
_queue              dbm                 pkg_resources       typing
_random             dbus                pkginfo             uaclient
_sha1               decimal             pkgutil             ufw
_sha256             difflib             platform            unicodedata
_sha3               dis                 platformdirs        unittest
_sha512             distlib             plistlib            urllib
_signal             distro              poplib              urllib3
_sitebuiltins       distro_info         posix               uu
_snack              distutils           posixpath           uuid
_socket             doctest             pprint              venv
_sqlite3            email               problem_report      virtualenv
_sre                encodings           profile             wadllib
_ssl                ensurepip           pstats              warnings
_stat               enum                pty                 wave
_statistics         errno               ptyprocess          weakref
_string             faulthandler        pwd                 webbrowser
_strptime           fcntl               py_compile          webencodings
_struct             filecmp             pyclbr              wheel
_symtable           fileinput           pycodestyle         wsgiref
_sysconfigdata__linux_x86_64-linux-gnu filelock            pydoc               xdrlib
_sysconfigdata__x86_64-linux-gnu fnmatch             pydoc_data          xml
_testbuffer         fractions           pyexpat             xmlrpc
_testcapi           ftplib              pygtkcompat         xxlimited
_testimportmultiple functools           pylev               xxlimited_35
_testinternalcapi   gc                  pyparsing           xxsubtype
_testmultiphase     genericpath         queue               yaml
_thread             getopt              quopri              zipapp
_threading_local    getpass             random              zipfile
_tracemalloc        gettext             re                  zipimport
_uuid               gi                  readline            zipp
_warnings           glob                reprlib             zlib
_weakref            graphlib            requests            zoneinfo
_weakrefset         grp                 requests_toolbelt   
_xxsubinterpreters  gzip                resource            
_xxtestfuzz         hashlib             rlcompleter         

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".
```

or jusy https://docs.python.org/3/py-modindex.html


