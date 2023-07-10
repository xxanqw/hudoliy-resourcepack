::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAtbWA2JAE+1EbsQ5+n//NaUp18LUfBycYzU1PqHI+9z
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+IeA==
::cxY6rQJ7JhzQF1fEqQJgZksaHUrSXA==
::ZQ05rAF9IBncCkqN+0xwdVsFAlbScjra
::ZQ05rAF9IAHYFVzEqQIYPR9bQA2bfFm/FboJ+uv+3+uEqUgPNA==
::eg0/rx1wNQPfEVWB+kM9LVsJDBSDP2D0A60ZiA==
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQKA36uE/Nsy7Ntgt1atHKmb
::dhA7uBVwLU+EWEGc9UwhP3s=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATEVotieEkHDByaPWWrEdU=
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFAtbWA2JAE+/Fb4I5/jH5/+DrUEUTa8tfZzUz6aNJfAS6U7YZZcu3TRfgM5s
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off

title Hudoliy

echo Packing files...

cd 7zip
.\7za.exe a pack.zip ..\pack\* > NUL:
move pack.zip ..\ > NUL:

cd ..
echo ===================================================
certutil -hashfile pack.zip SHA1
echo ===================================================
echo Done!
pause
