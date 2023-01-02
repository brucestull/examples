# Process

1. Start in project root directory.
    * `Get-Location`:
        * Sample console output:

            ```console
            PS C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component> Get-Location

            Path
            ----
            C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component

            PS C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component>
            ```

1. Inspect current directory contents:
    * The author has a `README.md` file and a `notes` directory:
    * `Get-ChildItem`:
        * Sample console output:

            ```console
            PS C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component> Get-ChildItem

                Directory:
            C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component

            Mode                 LastWriteTime         Length Name
            ----                 -------------         ------ ----
            d----            1/1/2023  4:41 PM                notes
            -a---            1/1/2023  4:49 PM           1057 README.md

            PS C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component>
            ```

    * [`README.md`](../README.md) has project information.
    * [`notes/process.md`](../notes/process.md), this document, has code changes throughout this example.

1. Use `create-react-app` to create a new React app:
    * `npx create-react-app my-react-app`:
    * Sample console output:

        ```console
        PS C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component> npx create-react-app my-react-app
        Need to install the following packages:
          create-react-app@5.0.1
        Ok to proceed? (y) y
        npm WARN deprecated tar@2.2.2: This version of tar is no longer supported, and will not receive security updates. Please upgrade asap.
        
        Creating a new React app in C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component\my-react-app.
        
        Installing packages. This might take a couple of minutes.
        Installing react, react-dom, and react-scripts with cra-template...
        
        
        added 1397 packages in 29s
        
        214 packages are looking for funding
          run `npm fund` for details
        
        Installing template dependencies using npm...
        
        added 71 packages in 14s
        
        226 packages are looking for funding
          run `npm fund` for details
        Removing template package using npm...
        
        
        removed 1 package, and audited 1468 packages in 2s
        
        226 packages are looking for funding
          run `npm fund` for details
        
        10 high severity vulnerabilities
        
        To address all issues (including breaking changes), run:
          npm audit fix --force
        
        Run `npm audit` for details.
        
        Success! Created my-react-app at C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component\my-react-app
        Inside that directory, you can run several commands:
        
          npm start
            Starts the development server.
        
          npm run build
            Bundles the app into static files for production.
        
          npm test
            Starts the test runner.
        
          npm run eject
            Removes this tool and copies build dependencies, configuration files
            and scripts into the app directory. If you do this, you can’t go back!
        
        We suggest that you begin by typing:
        
          cd my-react-app
          npm start
        
        Happy hacking!
        PS C:\Users\FlynntKnapp\Programming\examples\react\00-render-simple-react-component>
        ```

1. Remove all files from [`public/`](../my-react-app/public/) directory except the following:
    * `index.html`

1. Remove all files from [`src/`](../my-react-app/src/) directory except the following:
    * `index.js`

## Links

* [README.md](../README.md) for this example.
