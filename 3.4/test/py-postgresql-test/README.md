## usage

Set the PG\_CONN\_STR environment variable as a postgresql URL connection string.

Example:

`docker run -e "PG_CONN_STR=pq://user:password@dbhost:5432/database?[sslmode]=require" -p 8080:8080 image_name`
