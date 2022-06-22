all: start

ROOT = server
PKG = $(ROOT)/pytchat

VENV = $(ROOT)/venv
VBIN = $(VENV)/bin

TEST = $(ROOT)/tests

$(VBIN)/python:
	python3 -m venv $(VENV)

	chmod +x $(VBIN)/activate
	./$(VBIN)/activate
	$(VBIN)/pip install -r $(ROOT)/requirements.txt
	$(VBIN)/pip install -e $(ROOT)


$(VBIN)/pytest: $(VBIN)/python
	$(VBIN)/pip install -r $(TEST)/requirements.txt
	$(VBIN)/pytest $(TEST)

start: $(VBIN)/python
	$(VBIN)/python $(PKG) $(ROOT)/.env

test: $(VBIN)/pytest

cov: $(VBIN)/pytest $(VBIN)/coverage
	$(VBIN)/pytest $(TEST) --cov=$(PKG)
	$(VBIN)/python -m coverage xml -o $(ROOT)/coverage.xml

clean:
	rm -rf $(ROOT)/venv
	rm -rf $(ROOT)/*.-egg-info
	rm -rf $(ROOT)/coverage.xml

.PHONY: all start clean test cov