#!/bin/bash
if python -V | grep '3\.7\.'; then
	echo 'Python is already installed, do you want to reinstall it?';
else
	if [ ! -d "/goinfre/miniconda" ]; then
		[ -f ~/miniconda.sh ] || curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh ~/miniconda.sh;
		bash ~/miniconda.sh -b -p "/goinfre/miniconda";
	fi
	echo 'Python has been installed.';
fi
