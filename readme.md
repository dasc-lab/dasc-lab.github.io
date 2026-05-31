# DASC Lab Website


## Development
Install Hugo, following the steps at https://gohugo.io/installation/
This website was built using Hugo v0.161.1

To see the website locally, run
```
hugo server
```
and navigate to the URL, usually `http://localhost:1313/`.

After the changes have been made, commit them onto a new branch, and create a PR to merge the content into `main`.
The GitHub workflows will automatically deploy the new version of the website.

## Docker

You can also use Docker to do this (recommended). Simply run
```
docker compose build
```
to build the image, and then to run the container
```
This will build the image (if necessary) and start the server. It will print a clickable link to `http://localhost:1313/` directly in your terminal. Updates made to the local repo should automatically get rendered.

If you prefer to run the container in the background, use:
```bash
docker compose up -d
```
You can then view the logs to see the clickable link by running:
```bash
docker compose logs -f hugo
```

## Adding Content


### Adding a person

To add a new person, starting from the root directory, run
```
hugo new content people/id.md
```
where `id` must be replaced by the id you want to create.

Navigate to `/content/people/id.md` and edit the front matter.
After the front matter, you can add more details. These will be rendered on `dasc-lab.github.io/people/id` page.

### Adding a paper

Similarly, to add a paper, run
```
hugo new content papers/id.md
```
and then edit `/contents/papers/id.md`. Again, you can add more info after the front matter, to have it render on the individual page.

If you link the author id correctly, each author's page will be automatically updated to include all the papers too.

## Styles and Layout

This website uses bootstrap https://getbootstrap.com/ v5.3.3 to create styles.

To customize additional css, edit `/layouts/partials/style.html`.
To customize how the `person` and `papers` render, edit `/layouts/partials/person-card` or `/layouts/partials/paper-card`.


## TODO
- add search functionality
- add projects
- add news
- fix homepage
- add in maths functionality
