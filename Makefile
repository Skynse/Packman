gui:
	python3 makegui.py

run:
	python3 packman/packman.py

clean:
	rm packman/gui/mainwindow.py

deps:
	python3 -m pip install -r requirements.txt
