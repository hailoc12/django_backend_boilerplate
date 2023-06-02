docker run --name postgres -e POSTGRES_DB=embedbase -e POSTGRES_PASSWORD=localdb -p 5432:5432 -p 8080:8080 -d ankane/pgvector
