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

## Links

* [README.md](../README.md) for this example.
