# Instructions for Running News Queries

  - Go to the folder in which you've saved this repository
  - Run the following commands to load up virtual machine:
```sh
$ vagrant up
$ vagrant ssh
```
- Once vagrant is loaded, use the following command to see the folder contents:
```sh
$ cd /vagrant
```
- To confirm you're in the right directory, type the following to see the contents of the directory and confirm you see news_db.py.
```sh
$ ls
```
- Run the following command to run the news queries and see the output:
```sh
$ python news_db.py
```
# Views

The first query for the "Top Three Most Popular Articles" uses the following "pathslug" view which was created in this way:
```
create view "pathslug" as select path, slug, title from articles inner join log on log.path like concat('%',articles.slug);
```

The second query for "Most Popular Article Authors" uses the following two views that were created using the following queries:
```
create view "authorslug" as select name, slug from articles, authors where articles.author = authors.id;
```
```
create view "authorpath" as select name, path from "authorslug","pathslug" where pathslug.slug = authorslug.slug;
```

Thank you for viewing this project!