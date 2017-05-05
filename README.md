### SNP_analysis
Code to compare total genetic diversity in Humans vs Wheat 

# A word of warning
Almost all sequencing data is collected in a different way. I used an Ipython notebook (Data_munging.ipynb) to lightly munge the data before feeding it into a more consistent pipeline.

# Analyzing the data
entropy_calculators.py is a set of functions with unit test calculating average entropy for a species with a number of individuals and a number of SNPs. total_data_driver.py uses these functions to calculated the analysis for wheat and humans.
The wheat and human data comes in large csv files which must be downloaded separately [here](http://www.cerealsdb.uk.net/cerealgenomics/CerealsDB/kasp_mapped_snps.php)and [here](https://www.ncbi.nlm.nih.gov/pubmed/20643205)

# Plotting
swarm_visulization.py makes the pretty swarm plots. Note that it uses an inverse entropy calculation to approximate what a population of individuals with a given entropy score would look like. Granted, a single entropy score has a degenerate number of possible populations that could produce it, so I just found one solution that would work.
