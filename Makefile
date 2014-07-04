VER=v1

test:
	./docker_csrun.py testdata/sgVerify1.ini

image:
	docker build -t="tanmaykm/circuitscape:${VER}" .
