sslexpire
=========

This is a utility for checking how long it is until a host's SSl certificate
expires. Can for example be used in monitoring situations with Zabbix.

## Install

Install with python.

```
$ python setup.py install --user
```

Will install for the given user. If the script doesn't show up in your path you
can specify the `--install-scripts` flag.

```
$ python setup.py install --user --install-scripts /usr/local/bin
```

to install the scripts to `/usr/local/bin` or somewhere in your path.

## Usage

To check a host call with

```
$ sslexpire <host>
```

### Example

```
$ sslexpire uio.no
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Assured ID Root CA
verify return:1
depth=1 C = NL, ST = Noord-Holland, L = Amsterdam, O = TERENA, CN = TERENA SSL CA 3
verify return:1
depth=0 C = NO, ST = Oslo, L = Oslo, O = Universitetet i Oslo, CN = www.apollon.uio.no
verify return:1
DONE
2019-05-02 12:00:00
```

OpenSSL does output some text we're not interested in. You can get rid of it by
routing to `/dev/null`.

```
$ sslexpire uio.no 2>/dev/null
2019-05-02 12:00:00
```

And giving the `--days-until` flag only prints number of days.

```
$ sslexpire uio.no --days-until 2>/dev/null
1057
```
