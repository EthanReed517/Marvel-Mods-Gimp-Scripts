@ECHO OFF
REM **************************
REM * Section 0 - User Input *
REM **************************
REM enter the path to your plugins folder in AppData:
set appDataPluginFolder="C:\users\your_user\AppData\Roaming\GIMP\2.10\plug-ins"
REM enter the path to the GIMP installation:
set gimpInstallFolder="C:\Program Files\Gimp 2"


REM ******************************
REM * Section 1 - Main Execution *
REM ******************************
REM Do not modify anything below this line!
REM verify that the folder exists
if exist %appDataPluginFolder% (
	REM the folder exists
	REM copy the xcf templates to the "plugins" folder in GIMP's AppData folder
	REM move to the xcf folder
	cd %~dp0\"Supporting Templates"
	REM copy the .xcf files
	echo Copying supporting GIMP templates.
	if not exist %appDataPluginFolder%\"MarvelModsTemplates" (
		mkdir %appDataPluginFolder%\"MarvelModsTemplates"
	)
	for %%f in (*.xcf) do (
		copy >nul "%%f" %appDataPluginFolder%\"MarvelModsTemplates"
	)
	
	REM announce completion
	echo Installation of supporting GIMP templates is complete.
	echo.
	
	REM move to the folder of the script
	cd %~dp0

	REM copy python plugins to the "plugins" folder in GIMP's AppData folder
	echo Copying Python plugins . . .
	for %%f in ("Export Textures","Image Scaling","Skin Previews","Utilities") do (
		cd %~dp0\%%f
		for /r %%x in (*.py) do (
			copy >nul "%%x" %appDataPluginFolder%
		)
	)
	
	REM announce completion
	echo Installation of Python plugins is complete.
	echo.
	
) else (
	REM the folder does not exist
	REM display the error message
	echo ERROR: The folder %appDataPluginFolder% does not exist. Please enter a valid folder name in line 6 of this batch file.
	REM display lack of completion
	echo.
	echo Python plugins were not installed.
)
REM add a blank line as a spacer
echo.
REM set the path to the Python installation folder
set gimpPythonFolder=%gimpInstallFolder%"\lib\python2.7\site-packages"
REM verify that the folder exists
if exist %gimpPythonFolder% (
	REM the folder exists
	
	REM Copy the basic procedures module to GIMP's python installation
	echo Copying supporting Python modules . . .
	cd %~dp0\Supporting Modules
	for %%f in (Marvel_Mods_Basic_Gimp_Procedures, Marvel_Mods_Export_Previews, Marvel_Mods_Export_Textures) do (
		xcopy %%f %gimpInstallFolder%"\lib\python2.7\site-packages\%%f" /q /y /i
	)
	
	REM announce completion
	echo Installation of supporting Python modules is complete.
	echo.
) else (
	REM the folder does not exist
	REM display the error message
	echo ERROR: The folder %gimpPythonFolder% does not exist. Please enter a valid path to the GIMP installation in line 8 of this batch file.
	REM display lack of completion
	echo.
	echo Supporting Python modules were not installed.
)

REM add a blank line as a spacer
echo.
REM Set the path to the scripts folder
set gimpScriptsFolder=%gimpInstallFolder%"\share\gimp\2.0\scripts"
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
	echo Installation of scripts is complete.
	echo.
) else (
	REM the folder does not exist
	REM display the error message
	echo ERROR: The folder %gimpScriptsFolder% does not exist. Please enter a valid path to the GIMP installation in line 8 of this batch file.
	REM display lack of completion
	echo.
	echo Scheme scripts were not installed.
)

REM Check if the necessary dependencies are needed
if not exist C:\Windows\pngquant.exe (
	REM pngquant doesn't exist
	REM displa the error message
	echo WARNING: pngquant.exe does not exist in C:\Windows. This program is required for certain scripts to function. For more information, see the main README.md file included with the release.
	echo.
)
if not exist %appDataPluginFolder%\"gegl-python-fu & gegl_graph.py" (
	REM the GEGL script doesn't exist
	REM displa the error message
	echo WARNING: MareroQ's GEGL python script does not exist in %appDataPluginFolder%. This script is required for certain scripts to function. For more information, see the main README.md file included with the release.
	echo.
)


REM pause to show status
echo All processes complete.
pause