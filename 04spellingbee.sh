
# middle letter = r
# outer letters = oncaiz
# all other letters = bdefghjklmpqstuvwxy


# Checks to see if there are 50 results (there are)
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -c -E ".{4,7}"


# Gives the 50 answers to the spelling bee
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{4,7}"
