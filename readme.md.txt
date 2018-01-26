Проект делал в Eclipce

запускать проект командой:
python3.5 ./searcher.py "\w+@[\w.-_]+" mytext.txt
или
cat mytext.txt | python3.5 ./searcher.py -l "\w+@[\w.-_]+"

запускать тесты командой:
python3.5 -m unittest tests.py