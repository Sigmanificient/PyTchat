C_ROOT = client
S_ROOT = server

PKG = $(S_ROOT)/pytchat

PM = yarn --cwd $(C_ROOT)
PMR = $(PM) run
NM = $(C_ROOT)/node_modules

VENV = $(S_ROOT)/venv
VBIN = $(VENV)/bin

TEST = $(S_ROOT)/tests

S_PORT =

$(VBIN)/python:
	python3 -m venv $(VENV)

	chmod +x $(VBIN)/activate
	./$(VBIN)/activate
	$(VBIN)/pip install -r $(S_ROOT)/requirements.txt
	$(VBIN)/pip install -e $(S_ROOT)

$(VBIN)/pytest: $(VBIN)/python
	$(VBIN)/pip install -r $(TEST)/requirements.txt
	$(VBIN)/pytest $(TEST)

$(NM):
	$(PM) install

client: $(NM)
	$(PMR) serve

c_build: $(NM)
	$(PMR) build

server: $(VBIN)/python
	$(VBIN)/python $(PKG) $(S_PORT)

test: $(VBIN)/pytest

cov: $(VBIN)/pytest $(VBIN)/coverage
	$(VBIN)/pytest $(TEST) --cov=$(PKG)
	$(VBIN)/python -m coverage xml -o $(S_ROOT)/coverage.xml

clean:
	rm -rf $(S_ROOT)/venv
	rm -rf $(S_ROOT)/*.-egg-info
	rm -rf $(S_ROOT)/coverage.xml

.PHONY: all start clean test cov client server c_build