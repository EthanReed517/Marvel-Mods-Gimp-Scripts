@ECHO OFF
REM **************************
REM * Section 0 - User Input *
REM **************************
REM enter the path to your plugins folder in AppData:
set appDataPluginFolder="C:\users\your_user\AppData\Roaming\GIMP\2.10\plug-ins"
REM enter the path to the scripts folder in the GIMP installation:
set gimpScriptsFolder="C:\Program Files\GIMP 2\share\gimp\2.0\scripts"


REM ******************************
REM * Section 1 - Main Execution *
REM ******************************
REM Do not modify anything below this line!
REM Verify that a plugins folder was entered
if not %appDataPluginFolder%=="" (
	REM a folder was entered
	REM verify that the folder exists
	if exist %appDataPluginFolder% (
		REM the folder exists
		REM move to the folder of the script
		cd %~dp0

		REM copy python plugins to the "plugins" folder in GIMP's AppData folder
		echo Copying Python plugins . . .
		for /r %%x in (*.py) do (
			copy >nul "%%x" %appDataPluginFolder%
		)
		
		REM announce completion
		echo.
		echo Installation of plugins is complete.
	) else (
		REM the folder does not exist
		REM display the error message
		echo ERROR: The folder %appDataPluginFolder% does not exist. Please enter a valid folder name.
		REM display lack of completion
		echo.
		echo Python plugins were not installed.
	)
) else (
	REM a folder was not entered
	REM display the error message
	echo ERROR: The location of the "plugins" folder was not entered. Please edit line 6 of "update.bat" to add this information.
	REM display lack of completion
	echo.
	echo Python plugins were not installed.
)
REM add a blank line as a spacer
echo.
REM Verify that a scripts folder was entered
if not %gimpScriptsFolder%=="" (
	REM a folder was entered
	REM verify that the folder exists
	if exist %gimpScriptsFolder% (
		REM the folder exists
		REM move to the folder of the script
		cd %~dp0

		REM copy scheme plugins to the "scripts" folder in GIMP's installation
		echo Copying Scheme plugins . . .
		for /r %%x in (*.scm) do (
			copy >nul "%%x" %gimpScriptsFolder%
		)
		
		REM announce completion
		echo.
		echo Installation of scripts is complete.
	) else (
		REM the folder does not exist
		REM display the error message
		echo ERROR: The folder %gimpScriptsFolder% does not exist. Please enter a valid folder name.
		REM display lack of completion
		echo.
		echo Scheme scripts were not installed.
	)
) else (
	REM a folder was not entered
	REM display the error message
	echo ERROR: The location of the "plugins" folder was not entered. Please edit line 6 of "update.bat" to add this information.
	REM display lack of completion
	echo.
	echo Scheme scripts were not installed.
)

REM pause to show status
pause