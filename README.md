# alerta-rest-plugin


1. Install plugin inside docker container or by adding above command in dockerfile.
```python
pip install git+https://github.com/lemondemon/alerta-rest-plugin/archive/1.00.zip
```
2. Enable plugin in `/etc/alertad.conf`.

```python
PLUGINS = ['rest']
```
3. Set plugin-specific variables either in the server configuration file or as environment variables.
```
POSTBACK_URL=
POSTBACK_AUTH_CODE=
```
