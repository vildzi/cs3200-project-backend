# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 


Video URL: https://northeastern-my.sharepoint.com/:v:/g/personal/dziugelis_v_northeastern_edu/EYftaKsplrRInSBWuomPMoABs3Ukl_rwdZiAKII_HY47ig?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=rKdx2p


Our product is be a library management system meant for library owners/managers as well as members of the library. This system contains a database of books held by the library, including their author, genre, and title. Keeps track of the book inventory of a library, including the number of books in stock, and where books are located in a shelf. Book holds will also be recorded, with data on return date. Only librarians can manage book details and perform actions such as adding books, updating stock numbers, and removing books. Users can take out loans on books if there is available stock remaining, and return them once their rental period is over.   
