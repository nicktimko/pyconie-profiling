# Python Profiling: Finding the Squeaky Wheel

Presented at PyCon Ireland 2018 - November 10th. Time for the presentation and trip sponsored by Telnyx.

* [Slides](https://drive.google.com/open?id=1t-tcFTgyaisuhdFh1YWvrsFM42uknejUBtqDJTP3lf0)

## Approximate Command History

```
# fibonacci
python fib.py 33
python -m cProfile fib.py 33

# huffman codes
python huffcodes.py corpora/whale.txt
python -m cProfile huffcodes.py corpora/whale.txt
python -m cProfile -s time huffcodes.py corpora/whale.txt

# with snakeviz
python -m cProfile -o huff.profile huffcodes.py corpora/whale.txt
snakeviz huff.profile

# asyncio strangeness
python -m cProfile -o ahuff.profile aiohuffcodes.py \
    http://www.gutenberg.org/cache/epub/28885/pg28885.txt
snakeviz ahuff.profile

# diffexpy
python -m cProfile -o gene.profile
snakeviz gene.profile
```

## Notebooks used

* [microbench-diffexpy.ipynb](./microbench-diffexpy.ipynb)
    * iterating on the `diffexpy` function quickly

* [snakeviz-huff.ipynb](./snakeviz-huff.ipynb)
    * can also do snakeviz from within IPyNB
