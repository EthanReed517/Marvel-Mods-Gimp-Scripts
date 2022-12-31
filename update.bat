@ECHO OFF

cd %~dp0

for /r %%x in (*.scm) do (
	copy "%%x" "C:\Program Files\GIMP 2\share\gimp\2.0\scripts"
)

for /r %%x in (*.py) do (
	copy "%%x" "C:\users\ethan\AppData\Roaming\GIMP\2.10\plug-ins"
)

pause