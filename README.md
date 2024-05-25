After compose with `docker compose up -d --build`

Run
```
docker exec -it vdt_db /bin/bash
```
```
psql -d vdt_db -U vdt_user
```
```
CREATE TABLE IF NOT EXISTS vdt_student(name VARCHAR(50), gender VARCHAR(10),university VARCHAR(255));
```
To create the required table
