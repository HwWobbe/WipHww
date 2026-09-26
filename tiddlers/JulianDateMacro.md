# Julian Date macro for TiddlyWiki (Python-generated)

Use the Python script below to generate a macro tiddler that stores the current
Julian Date (`<<julianDate>>`) and Modified Julian Date (`<<modifiedJulianDate>>`).

```bash
python3 JulianDateMacro.py > tiddlers/$__macros_JulianDate.tid
```

Then reload TiddlyWiki and transclude it where needed:

```tid
{{||$:/macros/JulianDate}}
```

You can also generate for a specific UTC time:

```bash
python3 JulianDateMacro.py --iso-utc 2026-04-25T12:00:00
```
