@ECHO OFF
REM **************************
REM * Section 0 - User Input *
REM **************************
REM enter the path to your plugins folder in AppData:
set appDataPluginFolder="C:\users\ethan\AppData\Roaming\GIMP\2.10\plug-ins"
REM enter the path to your scripts folder in your GIMP installation folder:
set installScriptsFolder="C:\Program Files\GIMP 2\share\gimp\2.0\scripts"


REM ******************************
REM * Section 1 - Main Execution *
REM ******************************
REM Do not modify anything below this line!
REM move to the folder of the script
cd %~dp0

REM copy scheme scripts to the "scripts" folder in GIMP's installation
echo Copying Scheme plugins . . .
for /r %%x in (*.scm) do (
	copy >nul "%%x" %installScriptsFolder%
)

REM copy python plugins to the "plugins" folder in GIMP's AppData folder
echo Copying Python plugins . . .
for /r %%x in (*.py) do (
	copy >nul "%%x" %appDataPluginFolder%
)

REM pause to show completion
echo.
echo Installation of plugins is complete.
pause