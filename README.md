# UBC InfoVis Group Website

This is the repo that contains the UBC InfoVis Group website which uses Jekyll.

# Writing Content

To add content, simply edit one of the files in the content folder. For example, to edit the home page you would edit content/index.html. Once you push your changes to the repo, GitHub will automatically build and deploy the site using GitHub Actions based on the workflow defined in .github/workflows/build-deploy-jekyll.yml. Once this is done (it should take around three minutes) you can view the website at [ubc-infovis.github.io](ubc-infovis.github.io). If this looks correct, you can let the current web czar know that the real website at [cs.ubc.ca/group/infovis/](https://www.cs.ubc.ca/group/infovis/) is ready to be updated. The web czar can then upload the modified files from the Jekyll-generated `_site` folder into infovis folder on the CS department web server, located at `/ubc/cs/research/imager/project/infovis/website`.

# Local Testing

If you want to preview your changes before pushing, you will have to follow these steps:

1. Install Ruby, RubyGems, GCC, and Make: [https://jekyllrb.com/docs/installation/#guides](https://jekyllrb.com/docs/installation/#guides)
2. Install the necessary gems, ``cd`` into the directory, and run ``jekyll serve``: [https://jekyllrb.com/docs/#instructions](https://jekyllrb.com/docs/#instructions)
3. Navigate to [http://localhost:4000](http://localhost:4000)

# Git Refresher

To make changes to this repo, you will need to use git and GitHub. These steps assume you have git installed. There is an available GUI for using git called [GitHub Desktop](https://desktop.github.com/), but these steps are for the command line.

1. First, clone the repo: `git clone https://github.com/UBC-InfoVis/UBC-InfoVis.github.io.git`
2. If you already have a copy of the repo, go to the main branch and then pull any new changes: `git checkout main`, `git pull`
3. Check out a new branch to make your changes on: `git checkout -b <branch name>`
    - For this repo, use the following branch naming style: `<name>/<change>` where `<name>` is your name (just first name is fine) and `<change>` is a 2-4 word, dash-connected description of the change you are making. A change from Mara to update the styling of the People page might be made on a branch called `mara/prettify-people-page`.
4. Make your changes. You will likely want an IDE for this, and ideally you should test that nothing is broken and that your changes look as you expect by following the Local Testing steps above.
5. Check that your changes are saved: `git status` to see that the files are marked as modified, if necessary use `git diff <optional file name>` to see specifically what has been modified.
6. Add your changes: `git add <files to add>`
    - In some cases, you may want to add all the modified files. In that case you can use "`git add .`". However, make sure to double-check that you actually want to commit every file that you added. Sometimes an IDE file or other generated file that's specific to your instance will slip past the gitignore and be added, but we do not want those in the repo.
7. Commit your changes: `git commit -m "<commit message>"`
    - Your commit message should be a concise statement about what changes are included in the commit. A commit message for the sample change mentioned above could be `added styling for people page, cropped images to be same aspect ratio, changed order of member appearance`.
8. Push your changes: `git push`
    - The first time you push to your branch, the branch will not already exist on the server and you will need to make it. When you attempt to push, git will tell you that your branch does not exist on the server and will suggest a command that will push your changes to your 