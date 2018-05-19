build:
	docker build -t muhsinali/catnip .

run: build
	docker run --rm -dp 8888:5000 muhsinali/catnip

push:
	docker push muhsinali/catnip
