# CadLab

## Build It
Get [Miniconda][]. Install [anaconda-project][].

On OSX/Linux, run:
```bash
anaconda-project run build
anaconda-project run test
```

On Windows, run:
```bash
anaconda-project run build:win
anaconda-project run test:win
```

### cadlab
While still pre-`1.0`, JupyterLab's build chain has some negative externalities
for end users, namely an install- or run-time dependency on NodeJS and npmjs.org
when using any labextensions other than the built in set (e.g. Notebook, Terminal,
Console, Editor, etc.). Because, for the purposes of the workshop, we want to
get to the Good Stuff of running cadquery notebooks and not spend a bunch of time
debugging `nodejs` and `webpack`, we've added a few choice JupyterLab extensions:

- `@jupyterlab/toc`: a table of contents pane for Markdown headers
- `@jupyter-widgets/jupyterlab-manager`: because widgets are always good
- `bqplot`
- `jupyter-threejs`

...and wrapped them into a conda package which exposes some command, which can
do most of the things `jupyter lab` can do.

`cadlab` works like `jupyter lab`, while `cadlab-extension` works like
`jupyter labextension`. This isn't a toy installation: with the bundled `nodejs`,
an intrepid user can still install any of the [labextensions][] that are
compatible with the version `cadlab` was built with: as of writing, `0.35.x`.



[anaconda-project]: https://github.com/anaconda-platform/anaconda-project
[conda-forge]: https://github.com/conda-forge
[conda]: https://github.com/conda/conda
[labextensions]: https://www.npmjs.com/search?q=keywords:jupyterlab-extension
[Miniconda]: https://conda.io/miniconda.html
