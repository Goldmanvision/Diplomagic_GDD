[Setup]
AppName=Diplomagic Local UI
AppVersion=1.0.0
DefaultDirName={pf}\Diplomagic
DefaultGroupName=Diplomagic
OutputDir=dist
OutputBaseFilename=daps-installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\\bundle\\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\\Diplomagic"; Filename: "{app}\\daps.exe"
Name: "{group}\\Uninstall Diplomagic"; Filename: "{uninstallexe}"
