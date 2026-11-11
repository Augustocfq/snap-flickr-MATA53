# Analisando Grafos do SNAP: web-flickr (G114)

Trabalho prático de Teoria dos Grafos (MATA53, UFBA) sobre o grafo `web-flickr` do SNAP.

Os comandos abaixo são executados na raiz do repositório, em ordem. Seguidos num clone limpo, eles baixam o grafo, executam o `main.ipynb` inteiro, gravando nele a saída de todas as células, geram `data/processed/` e `results/` e compilam o relatório em `224215938.pdf`.

## Pré-requisitos

- Python 3.12 com o módulo `venv`
- `curl`
- TeX Live com `latexmk` e `pdflatex`. No Debian e no Ubuntu:

```bash
sudo apt install python3-venv curl latexmk texlive-full
```

## Instalação

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Download do grafo

```bash
curl -L --create-dirs -o data/raw/flickrEdges.txt.gz https://snap.stanford.edu/data/flickrEdges.txt.gz
```

## Execução do notebook

```bash
.venv/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.record_timing=False main.ipynb
```

O comando executa todas as células em ordem, num kernel novo, e grava as saídas no próprio `main.ipynb`, que pode ser aberto depois com `.venv/bin/jupyter lab main.ipynb`. A execução grava o grafo tratado em `data/processed/`, as tabelas em `results/tables/` e as figuras em `results/figures/`.

As etapas pesadas guardam o resultado em `data/cache/`, de modo que as execuções seguintes as leem em vez de recalcular. Para recalcular tudo, apague o cache antes de repetir o comando acima:

```bash
rm -rf data/cache
```

## Geração do relatório

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd -outdir=build -jobname=224215938 relatorio/main.tex
cp relatorio/build/224215938.pdf .
```

O relatório inclui as tabelas e as figuras de `results/`, então o notebook precisa ter sido executado antes. Os arquivos intermediários da compilação ficam em `relatorio/build/`.
