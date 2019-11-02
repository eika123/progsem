# installer pakkemanager chocolatey fra www.chocolatey.com
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))



# kjør deretter kommandoene under
### programmer til programmering i skolen
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install unxutils			# installerer en rekke unix-kommandoer (touch, ls, cd, mkdir, rm, rmdir, grep, cat, gzip etc.)
Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install clink			# bash-type autocompletion i windows cmd shell
# Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install anaconda3		# installer anaconda med python3-distribusjon
Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install cmder			# forbedret shell (optional)


conda install git                                                               # versjonskontroll
conda create -n envskole m2-base                                                # lager et virtuelt miljø
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install arduino        # arduino-ide
# Set-ExecutionPolicy Bypass -Scope Process -Foce; choco install fritzing       # software for utvikling av elektronikk



# diverse nyttig
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install pdfsam		# open source split, merge og rotering av pdf
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install vim			# vim editor (på windows! :-> )
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install emacs			# emacs editor (på windows! :-> )
#
## nettverkssniffing
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install wireshark
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install rawcap
#
## nettverksverktøy
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install curl
#
#
## run on upstart monitorering
#Set-ExcecutionPolicy Bypass -Scope Process -Force; choco install autoruns



# definer hotkeys for automatisering
# choco install autohotkey





