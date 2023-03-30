# UBC InfoVis Group Website

This is the repo that contains the UBC InfoVis Group website which uses Jekyll.

# Writing Content

To add content, simply edit one of the files in the content folder. For example, to edit the home page you would edit content/index.html. Once you push your changes to the repo, GitHub will automatically build and deploy the site using GitHub Actions based on the workflow defined in .github/workflows/build-deploy-jekyll.yml. Once this is done (it should only take around a minute) you can view the website at [ubc-infovis.github.io](ubc-infovis.github.io).

# Local Testing

If you want to preview your changes before pushing, you will have to follow these steps:

1. Install Ruby, RubyGems, GCC, and Make: [https://jekyllrb.com/docs/installation/#guides](https://jekyllrb.com/docs/installation/#guides)
2. Install the necessary gems, ``cd`` into the directory, and run ``jekyll serve``: [https://jekyllrb.com/docs/#instructions](https://jekyllrb.com/docs/#instructions)
3. Navigate to [http://localhost:4000](http://localhost:4000)