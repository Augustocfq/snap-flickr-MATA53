# Analisando Grafos do SNAP: web-flickr (G114)

Trabalho prático de Teoria dos Grafos (MATA53, UFBA) sobre o grafo `web-flickr` do SNAP.

## Objetivo

Aplicar os conceitos da disciplina a um grafo real: tratar os dados, analisar a estrutura do grafo, implementar e cronometrar algoritmos estudados (BFS, DFS, Eulerianidade, Tarjan, Dijkstra, Bellman-Ford, Floyd-Warshall e Kruskal) e responder às perguntas sobre small-world, lei de potência e robustez. A análise e as respostas estão no relatório, `224215938.pdf`.

## Grafo

O grafo é o G114, determinado pela matrícula 224215938: o [`web-flickr`](https://snap.stanford.edu/data/web-flickr.html) do SNAP, construído por McAuley e Leskovec (ECCV 2012). Cada vértice é uma imagem do Flickr, e uma aresta liga duas imagens que compartilham metadados, como local, galeria, grupo, tags ou usuário. O grafo é não direcionado, e o SNAP declara 105.938 vértices e 2.316.948 arestas. O trabalho usa só a lista de arestas, `flickrEdges.txt.gz`.

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

Com o cache versionado no repositório, a execução leva cerca de 3 min. Sem ele, o cálculo completo leva cerca de 1h16 numa máquina com Intel Core i5-11320H e 16 GB de RAM, com pico de cerca de 7 GB de memória.

## Seções do notebook e do relatório

| Seção do `main.ipynb` | Seção do relatório | Tempo sem cache |
|---|---|---|
| Leitura do grafo | Metodologia › Pipeline de execução | < 1 min |
| Tratamento dos dados | Descrição do grafo original › Tratamento realizado | < 1 min |
| Medidas básicas e componentes | Resultados obtidos › Parte I › Medidas básicas e componentes conexas | < 1 min |
| Distribuição de graus | Resultados obtidos › Parte I › Distribuição de graus | < 1 min |
| Clusterização e triângulos | Resultados obtidos › Parte I › Clusterização e triângulos | 13 min |
| Diâmetro, raio e comprimento médio dos caminhos | Resultados obtidos › Parte I › Diâmetro, raio e comprimento médio dos caminhos e Metodologia › Cálculo das distâncias | 33 min |
| Visualização e cobertura da Parte I | Resultados obtidos › Parte I › Visualização e cobertura | < 1 min |
| Medição de tempo | Metodologia › Medição de tempo | < 1 min |
| BFS e DFS | Resultados obtidos › Parte II › Busca em largura e busca em profundidade | 1 min |
| Eulerianidade e Tarjan | Resultados obtidos › Parte II › Eulerianidade e algoritmo de Tarjan | 4 min |
| Dijkstra e Bellman-Ford | Resultados obtidos › Parte II › Dijkstra e Bellman-Ford | 10 min |
| Floyd-Warshall | Resultados obtidos › Parte II › Floyd-Warshall | 3 min |
| Árvore geradora mínima (Kruskal) | Resultados obtidos › Parte II › Árvore geradora mínima (Kruskal) | 2 min |
| Small-world | Resultados obtidos › Parte III › Small-world | 8 min |
| Lei de potência | Resultados obtidos › Parte III › Lei de potência | < 1 min |
| Robustez à remoção aleatória | Resultados obtidos › Parte III › Robustez à remoção aleatória | 1 min |
| Robustez a ataque direcionado | Resultados obtidos › Parte III › Robustez a ataque direcionado | < 1 min |

## Geração do relatório

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd -outdir=build -jobname=224215938 relatorio/main.tex
cp relatorio/build/224215938.pdf .
```

O relatório inclui as tabelas e as figuras de `results/`, então o notebook precisa ter sido executado antes. Os arquivos intermediários da compilação ficam em `relatorio/build/`.
