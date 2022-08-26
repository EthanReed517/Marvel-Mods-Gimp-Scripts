@ECHO OFF

cd %~dp0

for /r %%x in (*.scm) do (
	copy %%x "C:\Program Files\GIMP 2\share\gimp\2.0\scripts"
)