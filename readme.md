# DASC Lab Website


## Development
Install Hugo, following the steps at https://gohugo.io/installation/
This website was built using Hugo v0.132.1

To see the website locally, run
```
hugo server
```
and navigate to the url, usually `http://localhost:1313/`. 

After the changes have been made, commit them onto a new branch, and create a PR to merge the content into `production`. 
The github workflows will automatically deploy the new version of the website. 

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

This website uses boostrap https://getbootstrap.com/ v5.3.3 to create styles. 

To customize additional css, edit `/layouts/partials/style.html`. 
To customize how the `person` and `papers` render, edit `/layouts/partials/person-card` or `/layouts/partials/paper-card`. 


## TODO
- add search functionality 
- add projects
- add news
- fix homepage
- add in maths functionality
