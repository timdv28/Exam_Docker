docker build -f Dockerfile.authent -t authent_image .
docker build -f Dockerfile.author -t author_image .
docker build -f Dockerfile.content -t content_image .
docker image pull datascientest/fastapi:1.0.0
docker-compose up