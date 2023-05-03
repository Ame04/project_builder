# Project builder

## Introduction
This project is made to generate a project skeleton to begin with.
Like than, with only one command you can begin to code or design on your project without thinking about its layout.

## Standard layout
Currently the layout will be the following :

```
├── project_name
     ├── (meca)
     ├── (elec)
     ├── (code)
     |    ├── data
     |    ├── doc
     |    ├── src
     |    ├── Readme.md
     ├── BOM
     └── Readme.md
```

A basic word will be put in both project readme and code readme.

A verification of the required environnement will be performed. For exemple, for the moment, in meca, only freecad projects will be handled.

## Next versions
- V2 : choice of the coding language and generation of a sqeleton for this language
- V3 : Generate a basic python CLI to run the code squeleton. To avoid having to go in the code folder to perform tasks.