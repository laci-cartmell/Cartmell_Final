###### README ######

Laci Cartmell - lacijcartmell@gmail.com

Project: Accounting for possible endosymbiont contamination in bed bug sequences
 
Accounting for possible endosymbiont contamination is important for three main reasons. One, bed bugs are important human ectoparasites that have high insecticide 
resistance. Endosymbionts may provide added benefits such as increased vitamin uptake/product and reproductive success. One possible control method could be centered 
around an endosymbiont known as Wolbachia. It has been noted in bed bugs since 1921 (Arkwright) and is present in 83-100% of sampled populations (Sakamoto and Rasgon 2006). 
It was also identified by PCR in the cliff swallowbug, Cimex vicarius (Rasgon and Scott 2004). Two, wolbachia is found in a diverse range of of invertebrates 
(Sakamoto and Rasgon 2019), extending the implications of this research to multiple clades. Three, most insects likely have multiple bacterial endosymbionts living 
within them and many labs are beginning to work with ddRAD reads. However, there isn't a current method of detecting how much contamination comes from endosymbiont genomes. 
This project seeks to determine if we need to account for endosymbiont DNA in ddRAD studies of insects. 


Important notes:
- You will need to import Biopython before it will run successfully
      - the script "python.sbatch" was used to submit it to OSCER 
- This script requires that your input files end with .fq.gz. Example: ATL01-02-F.1.fq.gz
- This script assumes that your fastq files are in a directory within the same working directory as the script. 
- If your files are not fastq-illumina, then you will need to modify line #52 by replacing "fastq-illumina" with 
  the fastq format. More information here: https://biopython.org/wiki/SeqIO
     - Line #52: SeqIO.convert(file_name, "fastq-illumina", zipped, "fasta")

License
This software is provided for free: you can redistribute it and/or modify it under the terms of the GNU Public License as published by the Free Software Foundation. 
The author claims no liability nor resposibility for the functionality of this software.


15 Dec. 2020

